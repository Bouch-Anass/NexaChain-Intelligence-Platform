# Enterprise Data Cleaning Report
**Project:** NexaChain Intelligence Platform
**Sprint:** Week 2 (Deep Data Cleaning)

## 1. Executive Summary
This document serves as the official record for the data engineering and cleaning pipeline applied to the five core enterprise datasets. All data quality issues identified during the Week 1 Data Profiling phase have been successfully remediated. Cleaned datasets are now available in the `Data/cleaned/` directory and are ready for Statistical Analysis and Machine Learning.

## 2. Before vs After Statistics
| Dataset | Original Rows | Cleaned Rows | Duplicates Removed | Missing Imputed | Outliers/Invalids Handled |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Orders** | 125,660 | 122,000 | 3,660 (Order IDs) | 0 | 2,453 Negative Order Values, 4,896 Future Dates |
| **Inventory** | 56,000 | 56,000 | 0 | 5,040 (Reorder Pt / Lead Time) | 3,360 Negative Stock Values |
| **Vendors** | 22,080 | 22,080 | 0 | 5,962 (Risk/Quality Scores) | 110 Negative DPO Values |
| **Logistics** | 125,660 | 125,660 | 0 | 0 | Top 1% Extreme Fuel Cost Outliers |
| **Financials** | 69,300 | 66,000 | 3,300 (AS/400 Duplicates) | 9,240 (Risk/WC Ratios) | 14,378 Negative Margins Flagged |

## 3. Transformation Rules & Business Justification

### 3.1 Orders Dataset (`clean_orders.py`)
* **Duplicates:** 3,660 duplicate `order_id` values resulting from double-posting were removed.
* **Date Capping:** 4,896 orders mistakenly stamped with future dates (2025-2026) were capped at the maximum valid operational date (`2024-12-31`).
* **Text Standardization:** `order_status` fields were stripped of whitespace and converted to Title Case to fix system inconsistencies (e.g., 'Ship.' -> 'Shipped').
* **Invalid Records:** 2,453 records had a negative `order_value_usd`. Since there was no credit note flag, these were classified as data entry errors and replaced with NULL to prevent skewed revenue forecasting.

### 3.2 Inventory Dataset (`clean_inventory.py`)
* **Missing Values:** `reorder_point` and `vendor_lead_time_days` had significant NULL rates. These were imputed using the dataset median to ensure downstream inventory optimization algorithms do not fail.
* **Invalid Records:** 3,360 records showed a negative `stock_on_hand`. As physical stock cannot drop below zero, these were converted to 0 and flagged with `stock_error_flag = 1`.

### 3.3 Vendors Dataset (`clean_vendors.py`)
* **Missing Values:** Critical vendor intelligence metrics (`financial_stability_score`, `quality_acceptance_rate`, `vris_score`) were missing for newer vendors. These were imputed with medians to allow the Machine Learning models to baseline them as "Average Risk".
* **Invalid Records:** Negative values in `days_payable_outstanding` were floored to 0.

### 3.4 Logistics Dataset (`clean_logistics.py`)
* **Outlier Handling:** `fuel_cost_usd` contained extreme outliers (up to 10x normal cost) due to sensor/logging errors. These were capped at the 99th percentile to prevent distortion of logistics profitability models.

### 3.5 Financials Dataset (`clean_financials.py`)
* **Duplicates:** 3,300 exact duplicate rows caused by AS/400 reconciliation issues were safely dropped.
* **Invalid Margins:** 14,378 records with negative `gross_profit_usd` were kept (as these represent true loss orders) but were explicitly flagged with `is_loss_order = 1` for immediate visibility.

## 4. GitHub Compliance Status
✅ All 5 cleaning scripts pushed to respective feature branches (`feature/clean-orders`, etc.)
✅ Output datasets successfully written to `Data/cleaned/`
✅ Code contains error handling, logging, and functional decomposition.
