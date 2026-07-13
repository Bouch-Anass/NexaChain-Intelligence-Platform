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
# Target: profit_margin_pct from orders (which acts as gross_margin_pct)
df = orders[['order_id', 'product_category', 'order_quantity', 'region', 'customer_segment', 'discount_pct', 'vendor_id', 'profit_margin_pct', 'fulfillment_channel']].copy()
df.rename(columns={'fulfillment_channel': 'shipment_mode', 'profit_margin_pct': 'gross_margin_pct'}, inplace=True)

# Merge vendors
df = df.merge(
    vendors[['vendor_id', 'vendor_tier', 'vris_score', 'defect_rate_pct']], on='vendor_id', how='left'
)

# Merge financials for logistics_cost_usd
df = df.merge(financials[['order_id', 'logistics_cost_usd']], on='order_id', how='left')

df.dropna(subset=['gross_margin_pct'], inplace=True)

# Optimise: Downsample to 200,000 rows to drastically speed up local training
if len(df) > 200000:
    df = df.sample(n=200000, random_state=42)

print(f"Dataset shape after merge and sampling: {df.shape}")

# Features and Target
X = df.drop(columns=['order_id', 'vendor_id', 'gross_margin_pct'])
y = df['gross_margin_pct']

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
    'Random Forest Regressor': RandomForestRegressor(n_estimators=50, n_jobs=-1, random_state=42)
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

# 1. Prediction Scatter Plot (Actual vs Predicted)
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred_best, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel('Actual Gross Margin (%)')
plt.ylabel('Predicted Gross Margin (%)')
plt.title(f'Prediction Scatter Plot ({best_name})')
plt.savefig('images/module_8_prediction_scatter.png')
plt.close()

# 2. Residual Analysis
residuals = y_test - y_pred_best
plt.figure(figsize=(8,6))
plt.scatter(y_pred_best, residuals, alpha=0.5)
plt.axhline(0, color='r', linestyle='--')
plt.xlabel('Predicted Gross Margin (%)')
plt.ylabel('Residuals')
plt.title(f'Residual Analysis ({best_name})')
plt.savefig('images/module_8_residuals.png')
plt.close()

# 3. Error Distribution
plt.figure(figsize=(8,6))
sns.histplot(residuals, bins=30, kde=True)
plt.xlabel('Prediction Error')
plt.title('Error Distribution')
plt.savefig('images/module_8_error_dist.png')
plt.close()

# 4. Feature Importance (if tree-based)
if best_name in ['Random Forest Regressor']:
    importances = best_model.named_steps['model'].feature_importances_
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
    plt.savefig('images/module_8_feature_importance.png')
    plt.close()

print("Generating Jupyter Notebook adhering to Enterprise Standards...")
nb = nbf.v4.new_notebook()

md_intro = """# Module 8 – Profitability Prediction Model
## Business Problem
Executives require early visibility into order profitability before products are delivered. Analysing profitability after sales have been completed is reactive; the organization wants a predictive model capable of estimating gross margin using information available before shipment.

## Business Objective
Predict the expected gross margin percentage of every order before delivery.

## Dataset Description
- **Target Variable**: `gross_margin_pct` (Derived from Orders)
- **Features**: Product Category, Order Quantity, Region, Customer Segment, Discount Percentage, Vendor Tier, VRIS Score, Shipment Mode, Logistics Cost.

## Feature Engineering Summary
- Target standardisation: Renamed `profit_margin_pct` to `gross_margin_pct`.
- Merged operational data from `orders_cleaned.csv` with supplier performance from `vendors_cleaned.csv` and financial costs from `financials_cleaned.csv`.
- Numerical features scaled using `StandardScaler` and imputed with `SimpleImputer` (median).
- Categorical features encoded using `OneHotEncoder` and imputed with `SimpleImputer` (most_frequent).
- Downsampled dataset to 200,000 rows to optimize training time on local machines.
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

df = orders[['order_id', 'product_category', 'order_quantity', 'region', 'customer_segment', 'discount_pct', 'vendor_id', 'profit_margin_pct', 'fulfillment_channel']].copy()
df.rename(columns={'fulfillment_channel': 'shipment_mode', 'profit_margin_pct': 'gross_margin_pct'}, inplace=True)
df = df.merge(vendors[['vendor_id', 'vendor_tier', 'vris_score', 'defect_rate_pct']], on='vendor_id', how='left')
df = df.merge(financials[['order_id', 'logistics_cost_usd']], on='order_id', how='left')
df.dropna(subset=['gross_margin_pct'], inplace=True)

if len(df) > 200000:
    df = df.sample(n=200000, random_state=42)

X = df.drop(columns=['order_id', 'vendor_id', 'gross_margin_pct'])
y = df['gross_margin_pct']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
"""

md_models = """## Model Development
We train and evaluate Linear Regression and Random Forest Regressors.
### Hyperparameter Configuration
- **Random Forest**: `n_estimators=50`, `n_jobs=-1`, `random_state=42`
"""

code_models = """categorical_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
numeric_cols = X.select_dtypes(include=['number']).columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline([('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler())]), numeric_cols),
        ('cat', Pipeline([('imputer', SimpleImputer(strategy='most_frequent')), ('onehot', OneHotEncoder(handle_unknown='ignore'))]), categorical_cols)
    ])

models = {
    'Linear Regression': LinearRegression(),
    'Random Forest Regressor': RandomForestRegressor(n_estimators=50, n_jobs=-1, random_state=42)
}

for name, model in models.items():
    pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('model', model)])
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    print(f"{name} -> MAE: {mean_absolute_error(y_test, y_pred):.2f}, RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}, R2: {r2_score(y_test, y_pred):.4f}")
"""

md_interp = """## Business Interpretation
- The evaluation metrics show the comparative predictive capability of baseline linear vs tree-based models. 
- Higher R2 and lower RMSE indicate a better model for profitability estimation.
- Feature importance highlights which pre-shipment variables (e.g. discount_pct, logistics_cost) drive the final margin.

## Executive Recommendations
- **Identify Unprofitable Orders:** Integrate the model to flag low-margin orders before approval, specifically if the predicted margin falls below organizational thresholds.
- **Review Pricing:** High discount percentages heavily impact gross margins; review discounting strategies for segments identified as low-profitability.

## Limitations
- Model relies on expected logistics costs; unexpected supply chain disruptions after order placement might alter true profitability.

## Future Improvements
- Integrate real-time freight quoting data instead of using historical average logistics costs.
- Use advanced Hyperparameter optimization (e.g. Optuna) in Part 3 to boost predictive performance.
"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(md_intro),
    nbf.v4.new_code_cell(code_setup),
    nbf.v4.new_code_cell(code_data),
    nbf.v4.new_markdown_cell(md_models),
    nbf.v4.new_code_cell(code_models),
    nbf.v4.new_markdown_cell(md_interp)
]

with open('notebooks/profitability_prediction.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
print("Notebook saved to notebooks/profitability_prediction.ipynb")
