import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nbformat as nbf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os

# Create directories if they don't exist
os.makedirs('images', exist_ok=True)
os.makedirs('notebooks', exist_ok=True)
os.makedirs('reports/financial_intelligence', exist_ok=True)

print("Loading datasets...")
orders = pd.read_csv('Data/cleaned/orders_cleaned.csv')
vendors = pd.read_csv('Data/cleaned/vendors_cleaned.csv')
logistics = pd.read_csv('Data/cleaned/logistics_cleaned.csv')
financials = pd.read_csv('Data/cleaned/financials_cleaned.csv')

print("Merging datasets...")
# Target: procurement_cost_usd from financials
df = orders[['order_id', 'product_category', 'order_quantity', 'region', 'vendor_id']].merge(
    financials[['order_id', 'procurement_cost_usd']], on='order_id', how='inner'
)

# Merge vendors
df = df.merge(
    vendors[['vendor_id', 'vendor_tier', 'vris_score', 'defect_rate_pct']], on='vendor_id', how='left'
)

# Merge logistics for shipment_mode (if available, else we skip or check columns)
if 'shipment_mode' in logistics.columns:
    df = df.merge(logistics[['order_id', 'shipment_mode']], on='order_id', how='left')
else:
    # If not in logistics, maybe fulfillment_channel from orders
    if 'fulfillment_channel' in orders.columns:
        df = df.merge(orders[['order_id', 'fulfillment_channel']], on='order_id', how='left')
        df.rename(columns={'fulfillment_channel': 'shipment_mode'}, inplace=True)

df.dropna(subset=['procurement_cost_usd'], inplace=True)

print(f"Dataset shape after merge: {df.shape}")

# Features and Target
X = df.drop(columns=['order_id', 'vendor_id', 'procurement_cost_usd'])
y = df['procurement_cost_usd']

# Preprocessing
categorical_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
numeric_cols = X.select_dtypes(include=['number']).columns.tolist()

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training models...")
models = {
    'Linear Regression': LinearRegression(),
    'Random Forest Regressor': RandomForestRegressor(n_estimators=100, random_state=42)
}

results = []
best_model = None
best_r2 = -float('inf')
best_name = ""

for name, model in models.items():
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('model', model)])
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    results.append({'Model': name, 'MAE': mae, 'RMSE': rmse, 'R2': r2})
    print(f"{name} -> MAE: {mae:.2f}, RMSE: {rmse:.2f}, R2: {r2:.4f}")
    
    if r2 > best_r2:
        best_r2 = r2
        best_model = pipeline
        best_name = name

print(f"\nBest Model: {best_name}")

# Visualizations with Best Model
y_pred_best = best_model.predict(X_test)

# 1. Actual vs Predicted
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred_best, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel('Actual Procurement Cost (USD)')
plt.ylabel('Predicted Procurement Cost (USD)')
plt.title(f'Actual vs Predicted ({best_name})')
plt.savefig('images/module_7_actual_vs_predicted.png')
plt.close()

# 2. Residual Plot
residuals = y_test - y_pred_best
plt.figure(figsize=(8,6))
plt.scatter(y_pred_best, residuals, alpha=0.5)
plt.axhline(0, color='r', linestyle='--')
plt.xlabel('Predicted Procurement Cost (USD)')
plt.ylabel('Residuals')
plt.title(f'Residual Plot ({best_name})')
plt.savefig('images/module_7_residuals.png')
plt.close()

# 3. Error Distribution
plt.figure(figsize=(8,6))
sns.histplot(residuals, bins=30, kde=True)
plt.xlabel('Prediction Error')
plt.title('Error Distribution')
plt.savefig('images/module_7_error_dist.png')
plt.close()

# 4. Feature Importance (if tree-based)
if best_name in ['Random Forest Regressor']:
    importances = best_model.named_steps['model'].feature_importances_
    # Get feature names after one-hot encoding
    cat_encoder = best_model.named_steps['preprocessor'].named_transformers_['cat'].named_steps['onehot']
    cat_features = cat_encoder.get_feature_names_out(categorical_cols)
    feature_names = numeric_cols + list(cat_features)
    
    feat_imp = pd.Series(importances, index=feature_names).sort_values(ascending=False).head(10)
    
    plt.figure(figsize=(10,6))
    feat_imp.plot(kind='bar')
    plt.title('Top 10 Feature Importances')
    plt.ylabel('Importance Score')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('images/module_7_feature_importance.png')
    plt.close()

print("Generating Jupyter Notebook...")
nb = nbf.v4.new_notebook()

md_intro = """# Module 7 – Procurement Cost Prediction
## Business Problem
Procurement costs fluctuate because of supplier performance, transportation costs, inventory levels, purchasing behaviour, and market conditions. Predicting procurement costs before purchase orders are issued allows procurement teams to negotiate better contracts and optimize supplier selection.

## Business Objective
Predict procurement invoice cost using operational features available before purchase execution.

## Dataset Description
- **Target Variable**: `procurement_cost_usd`
- **Features**: Product Category, Order Quantity, Region, Vendor Tier, VRIS Score, Defect Rate, Shipment Mode.
"""

code_setup = """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
"""

code_data = """orders = pd.read_csv('../Data/cleaned/orders_cleaned.csv')
vendors = pd.read_csv('../Data/cleaned/vendors_cleaned.csv')
financials = pd.read_csv('../Data/cleaned/financials_cleaned.csv')

df = orders[['order_id', 'product_category', 'order_quantity', 'region', 'vendor_id', 'fulfillment_channel']].merge(
    financials[['order_id', 'procurement_cost_usd']], on='order_id', how='inner'
)
df = df.merge(vendors[['vendor_id', 'vendor_tier', 'vris_score', 'defect_rate_pct']], on='vendor_id', how='left')
df.dropna(subset=['procurement_cost_usd'], inplace=True)
df.rename(columns={'fulfillment_channel': 'shipment_mode'}, inplace=True)

X = df.drop(columns=['order_id', 'vendor_id', 'procurement_cost_usd'])
y = df['procurement_cost_usd']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
"""

md_models = "## Model Development and Evaluation"

code_models = """categorical_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
numeric_cols = X.select_dtypes(include=['number']).columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline([('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler())]), numeric_cols),
        ('cat', Pipeline([('imputer', SimpleImputer(strategy='most_frequent')), ('onehot', OneHotEncoder(handle_unknown='ignore'))]), categorical_cols)
    ])

models = {
    'Linear Regression': LinearRegression(),
    'Random Forest Regressor': RandomForestRegressor(n_estimators=100, random_state=42)
}

for name, model in models.items():
    pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('model', model)])
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    print(f"{name} -> MAE: {mean_absolute_error(y_test, y_pred):.2f}, RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}, R2: {r2_score(y_test, y_pred):.4f}")
"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(md_intro),
    nbf.v4.new_code_cell(code_setup),
    nbf.v4.new_code_cell(code_data),
    nbf.v4.new_markdown_cell(md_models),
    nbf.v4.new_code_cell(code_models)
]

with open('notebooks/procurement_cost_prediction.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
print("Notebook saved to notebooks/procurement_cost_prediction.ipynb")
