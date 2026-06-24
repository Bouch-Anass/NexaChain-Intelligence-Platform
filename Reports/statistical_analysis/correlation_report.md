# Correlation & Bivariate Analysis Report
**Project:** NexaChain Intelligence Platform
**Phase:** Week 2 - Statistical Analysis

This report presents the correlation across the master joined enterprise dataset. By identifying multicollinearity and strong predictors, we can refine our Feature Engineering strategy.

## 1. Pearson Correlation Matrix (Top Features)
A correlation coefficient near `1.0` indicates a strong positive linear relationship, while `-1.0` indicates a strong negative relationship. Values near `0` indicate no linear relationship.

| Feature | `order_quantity_x` | `unit_price_usd_x` | `order_value_usd_x` | `discount_pct_x` | `cost_of_goods_usd_x` | `gross_margin_usd_x` | `profit_margin_pct_x` | `delivery_delay_days_x` | `data_entry_error` | `order_quantity_y` | `unit_price_usd_y` | `order_value_usd_y` | `discount_pct_y` | `cost_of_goods_usd_y` | `gross_margin_usd_y` | `profit_margin_pct_y` | `delivery_delay_days_y` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **order_quantity_x** | 1.00 | -0.00 | 0.33 | 0.00 | 0.33 | 0.32 | 0.01 | 0.00 | nan | **1.00 (High)** | -0.00 | 0.33 | 0.00 | 0.33 | 0.32 | 0.01 | 0.00 | 
| **unit_price_usd_x** | -0.00 | 1.00 | 0.51 | 0.00 | 0.52 | 0.47 | -0.00 | 0.00 | nan | -0.00 | **1.00 (High)** | 0.51 | 0.00 | 0.52 | 0.47 | -0.00 | 0.00 | 
| **order_value_usd_x** | 0.33 | 0.51 | 1.00 | -0.01 | **0.99 (High)** | **0.97 (High)** | 0.01 | 0.00 | nan | 0.33 | 0.51 | **1.00 (High)** | -0.01 | **0.99 (High)** | **0.97 (High)** | 0.01 | 0.00 | 
| **discount_pct_x** | 0.00 | 0.00 | -0.01 | 1.00 | -0.01 | -0.01 | -0.00 | -0.00 | nan | 0.00 | 0.00 | -0.01 | **1.00 (High)** | -0.01 | -0.01 | -0.00 | -0.00 | 
| **cost_of_goods_usd_x** | 0.33 | 0.52 | **0.99 (High)** | -0.01 | 1.00 | **0.93 (High)** | -0.02 | 0.00 | nan | 0.33 | 0.52 | **0.99 (High)** | -0.01 | **1.00 (High)** | **0.93 (High)** | -0.02 | 0.00 | 
| **gross_margin_usd_x** | 0.32 | 0.47 | **0.97 (High)** | -0.01 | **0.93 (High)** | 1.00 | 0.05 | 0.00 | nan | 0.32 | 0.47 | **0.97 (High)** | -0.01 | **0.93 (High)** | **1.00 (High)** | 0.05 | 0.00 | 
| **profit_margin_pct_x** | 0.01 | -0.00 | 0.01 | -0.00 | -0.02 | 0.05 | 1.00 | -0.00 | nan | 0.01 | -0.00 | 0.01 | -0.00 | -0.02 | 0.05 | **1.00 (High)** | -0.00 | 
| **delivery_delay_days_x** | 0.00 | 0.00 | 0.00 | -0.00 | 0.00 | 0.00 | -0.00 | 1.00 | nan | 0.00 | 0.00 | 0.00 | -0.00 | 0.00 | 0.00 | -0.00 | **1.00 (High)** | 
| **data_entry_error** | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| **order_quantity_y** | **1.00 (High)** | -0.00 | 0.33 | 0.00 | 0.33 | 0.32 | 0.01 | 0.00 | nan | 1.00 | -0.00 | 0.33 | 0.00 | 0.33 | 0.32 | 0.01 | 0.00 | 
| **unit_price_usd_y** | -0.00 | **1.00 (High)** | 0.51 | 0.00 | 0.52 | 0.47 | -0.00 | 0.00 | nan | -0.00 | 1.00 | 0.51 | 0.00 | 0.52 | 0.47 | -0.00 | 0.00 | 
| **order_value_usd_y** | 0.33 | 0.51 | **1.00 (High)** | -0.01 | **0.99 (High)** | **0.97 (High)** | 0.01 | 0.00 | nan | 0.33 | 0.51 | 1.00 | -0.01 | **0.99 (High)** | **0.97 (High)** | 0.01 | 0.00 | 
| **discount_pct_y** | 0.00 | 0.00 | -0.01 | **1.00 (High)** | -0.01 | -0.01 | -0.00 | -0.00 | nan | 0.00 | 0.00 | -0.01 | 1.00 | -0.01 | -0.01 | -0.00 | -0.00 | 
| **cost_of_goods_usd_y** | 0.33 | 0.52 | **0.99 (High)** | -0.01 | **1.00 (High)** | **0.93 (High)** | -0.02 | 0.00 | nan | 0.33 | 0.52 | **0.99 (High)** | -0.01 | 1.00 | **0.93 (High)** | -0.02 | 0.00 | 
| **gross_margin_usd_y** | 0.32 | 0.47 | **0.97 (High)** | -0.01 | **0.93 (High)** | **1.00 (High)** | 0.05 | 0.00 | nan | 0.32 | 0.47 | **0.97 (High)** | -0.01 | **0.93 (High)** | 1.00 | 0.05 | 0.00 | 
| **profit_margin_pct_y** | 0.01 | -0.00 | 0.01 | -0.00 | -0.02 | 0.05 | **1.00 (High)** | -0.00 | nan | 0.01 | -0.00 | 0.01 | -0.00 | -0.02 | 0.05 | 1.00 | -0.00 | 
| **delivery_delay_days_y** | 0.00 | 0.00 | 0.00 | -0.00 | 0.00 | 0.00 | -0.00 | **1.00 (High)** | nan | 0.00 | 0.00 | 0.00 | -0.00 | 0.00 | 0.00 | -0.00 | 1.00 | 

## 2. Key Insights & Multicollinearity Warning
> [!IMPORTANT]
> Variables showing correlation > 0.8 should be monitored for multicollinearity before being fed into regression models.

### Target Variable Proxies
