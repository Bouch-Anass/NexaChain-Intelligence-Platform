# Procurement Cost Prediction Report

## Business Problem
Procurement costs often fluctuate due to supplier performance variations, transportation modalities, regional differences, and purchasing behavior. Without early visibility, procurement teams struggle to optimize supplier selection or negotiate better contracts before purchase orders are issued.

## Objective
The objective of this module is to develop a predictive machine learning model to estimate the `procurement_cost_usd` (Invoice Cost) using operational features available prior to purchase execution.

## Methodology
1. **Data Integration**: We merged `orders_cleaned.csv`, `vendors_cleaned.csv`, and `financials_cleaned.csv` to create a consolidated view of operations, supplier performance, and procurement costs.
2. **Feature Engineering**: Features included `product_category`, `order_quantity`, `region`, `vendor_tier`, `vris_score`, `defect_rate_pct`, and `shipment_mode`. Missing values were imputed (median for numeric, most frequent for categorical).
3. **Model Selection**: We compared a baseline `Linear Regression` against an advanced `Random Forest Regressor`. 
4. **Evaluation**: Models were evaluated using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² Score.

## Model Evaluation Results
- **Random Forest Regressor** outperformed the baseline Linear Regression model, capturing non-linear relationships such as the interaction between volume (order quantity) and vendor risk profiles.
- Feature importance analysis indicates that `order_quantity` and `product_category` are primary drivers, but `vendor_tier` significantly influences cost variance.

## Executive Recommendations
1. **Pre-Purchase Cost Estimation**: Integrate this predictive model into the procurement approval workflow. Flag any purchase requests where the predicted cost significantly exceeds historical averages for manual review.
2. **Supplier Optimization**: Since vendor tiers impact cost, prioritize Tier-1 vendors for high-volume orders where they exhibit lower predicted procurement costs.
3. **Continuous Monitoring**: Retrain the model quarterly as new supplier performance data and market conditions evolve.
