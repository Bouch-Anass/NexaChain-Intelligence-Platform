import pandas as pd
import numpy as np
import os

def create_master_dataset(cleaned_dir):
    try:
        orders = pd.read_csv(os.path.join(cleaned_dir, 'orders_cleaned.csv'))
        inventory = pd.read_csv(os.path.join(cleaned_dir, 'inventory_cleaned.csv'))
        logistics = pd.read_csv(os.path.join(cleaned_dir, 'logistics_cleaned.csv'))
        vendors = pd.read_csv(os.path.join(cleaned_dir, 'vendors_cleaned.csv'))
        
        # Merge orders & logistics on order_id
        master = pd.merge(orders, logistics, on='order_id', how='left')
        
        # Merge inventory & vendors on vendor_id
        inv_ven = pd.merge(inventory, vendors, on='vendor_id', how='left')
        
        # Merge master with inv_ven on product_id
        # Wait, if orders has product_id:
        if 'product_id' in master.columns and 'product_id' in inv_ven.columns:
            master = pd.merge(master, inv_ven, on='product_id', how='left')
            
        return master
    except Exception as e:
        print(f"Error merging datasets: {e}")
        return None

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cleaned_dir = os.path.join(script_dir, r"..\Data\cleaned")
    report_dir = os.path.join(script_dir, r"..\Reports\statistical_analysis")
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, 'correlation_report.md')
    
    master_df = create_master_dataset(cleaned_dir)
    if master_df is None:
        return
        
    numerics = master_df.select_dtypes(include=[np.number]).columns
    # Filter out IDs and flags
    features = [c for c in numerics if not c.endswith('_id') and not c.endswith('_flag')]
    
    # Take top 15 most populated/variable features for simplicity
    df_features = master_df[features].dropna()
    
    # Calculate Pearson
    pearson_corr = df_features.corr(method='pearson')
    
    with open(report_path, 'w') as f:
        f.write("# Correlation & Bivariate Analysis Report\n")
        f.write("**Project:** NexaChain Intelligence Platform\n")
        f.write("**Phase:** Week 2 - Statistical Analysis\n\n")
        f.write("This report presents the correlation across the master joined enterprise dataset. By identifying multicollinearity and strong predictors, we can refine our Feature Engineering strategy.\n\n")
        
        f.write("## 1. Pearson Correlation Matrix (Top Features)\n")
        f.write("A correlation coefficient near `1.0` indicates a strong positive linear relationship, while `-1.0` indicates a strong negative relationship. Values near `0` indicate no linear relationship.\n\n")
        
        # Convert matrix to Markdown Table
        f.write("| Feature | " + " | ".join([f"`{c}`" for c in pearson_corr.columns]) + " |\n")
        f.write("| :--- | " + " | ".join([":---:" for _ in pearson_corr.columns]) + " |\n")
        
        for idx in pearson_corr.index:
            row_str = f"| **{idx}** | "
            for col in pearson_corr.columns:
                val = pearson_corr.loc[idx, col]
                if val >= 0.7 and idx != col:
                    row_str += f"**{val:.2f} (High)** | "
                elif val <= -0.7 and idx != col:
                    row_str += f"**{val:.2f} (Low)** | "
                else:
                    row_str += f"{val:.2f} | "
            f.write(row_str + "\n")
            
        f.write("\n## 2. Key Insights & Multicollinearity Warning\n")
        f.write("> [!IMPORTANT]\n")
        f.write("> Variables showing correlation > 0.8 should be monitored for multicollinearity before being fed into regression models.\n\n")
        
        f.write("### Target Variable Proxies\n")
        if 'delivery_delay_days' in pearson_corr.columns:
            target = pearson_corr['delivery_delay_days'].sort_values(ascending=False)
            f.write("Top predictors for **delivery_delay_days**:\n")
            for k, v in target.items():
                if k != 'delivery_delay_days' and abs(v) > 0.1:
                    f.write(f"- `{k}`: {v:.2f}\n")
        
if __name__ == "__main__":
    main()
    print("Correlation Analysis Complete!")
