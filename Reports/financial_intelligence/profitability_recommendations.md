# Profitability Prediction Model - Business Recommendations

## Business Problem
Analysing profitability after sales have been completed is a reactive approach. To proactively optimize financial health, executives require early visibility into expected order profitability (Gross Margin Percentage) before products are shipped or delivered.

## Objective
Develop a predictive model capable of estimating the `gross_margin_pct` of an order using information available prior to shipment, empowering the business to flag unprofitable transactions.

## Model Methodology (Enterprise Standard)
1. **Target Standardisation**: We utilized the ratio of gross margin USD to order value USD, converting `profit_margin_pct` into our expected `gross_margin_pct`.
2. **Data Merging**: We enriched the `orders_cleaned.csv` operational data with supplier risk and performance indicators from `vendors_cleaned.csv` and logistical cost baselines from `financials_cleaned.csv`.
3. **Feature Engineering**: Features such as `discount_pct`, `customer_segment`, `region`, `vendor_tier`, `shipment_mode`, and expected `logistics_cost_usd` were used. Numerical features were imputed with median values and scaled; categorical features were imputed and one-hot encoded.
4. **Model Comparison**: We trained and evaluated both a Linear Regression baseline and a Random Forest Regressor using `scikit-learn`.

## Insights & Interpretation
- **Model Performance**: Tree-based models (Random Forest) provided superior R² scores and lower RMSE, effectively capturing non-linear pricing effects and discounting structures.
- **Drivers of Profitability**: Feature importance analysis confirms that pre-shipment variables—notably `discount_pct`, `order_quantity`, and `logistics_cost_usd`—are the dominant drivers of the final gross margin. High discounts combined with premium `shipment_mode` heavily erode margins.

## Executive Recommendations
1. **Proactive Intervention Workflow**:
   - Integrate the model into the order processing system.
   - Orders predicted to yield a gross margin below the enterprise threshold (e.g., < 20%) should trigger an automated alert for sales/finance review before fulfillment.
2. **Dynamic Pricing & Discounting**:
   - Limit allowable discount percentages for specific customer segments that historically drive high logistics costs.
   - Adjust shipping options dynamically: If an order is predicted to be low-margin, default the shipment mode to a standard/cheaper logistical tier.
3. **Supplier Selection**:
   - Re-route unprofitable predictions to alternate vendors (e.g., Tier-1 vendors with lower defect rates) to salvage margins.

## Limitations
- The model currently relies on historical average logistical costs. Unexpected macroeconomic supply chain disruptions after an order is placed might alter the true profitability.

## Future Improvements
- Integrate real-time API freight quoting data to replace static logistical estimates.
- Explore hyperparameter optimization frameworks like Optuna to further boost predictive accuracy in future iterations.
