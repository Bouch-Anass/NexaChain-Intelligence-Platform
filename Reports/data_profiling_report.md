# Initial Data Profiling & Quality Assessment Report
**Project:** NexaChain Intelligence Platform
**Phase:** Task 3 - Data Quality Assessment

## 1. Executive Summary
This report summarizes the initial data profiling conducted on the 5 core NexaChain datasets (`orders.csv`, `inventory.csv`, `vendors.csv`, `logistics.csv`, `financials.csv`). The profiling targeted structural inconsistencies, missing values, duplicates, outliers, and invalid records to prepare the data for downstream Machine Learning tasks.

---

## 2. Orders Dataset (`orders.csv`)
* **Total Records:** 125,660
* **Duplicates:** 0 exact duplicate rows found (Note: The metadata indicates ~3,600 duplicate `order_id` values with different timestamps simulating ERP double-posting. These require deduplication based on `last_modified_date`).
* **Missing Values:**
  * `profit_margin_pct`: 6,283 records (5.00%) - Intentional NULLs.
  * `actual_delivery_date`: 50,072 records (39.85%) - Expected for 'Pending' and non-Delivered orders.
* **Invalid Records & Outliers:**
  * `order_value_usd`: 2,513 records (2.00%) contain negative values. These are likely credit notes or data entry errors mixed into the main table and must be flagged/separated.
  * Future Dates: ~4% of `order_date` values are in the 2025-2026 range due to batch processing errors.

## 3. Inventory Dataset (`inventory.csv`)
* **Total Records:** 56,000
* **Duplicates:** 0 exact duplicate rows.
* **Missing Values:**
  * `reorder_point`: 2,240 records (4.00%). Must be imputed using the lead time and average demand formula.
  * `vendor_lead_time_days`: 2,800 records (5.00%).
* **Invalid Records & Outliers:**
  * `stock_on_hand`: 3,360 records (6.00%) contain negative stock values. This is physically impossible and represents a critical system integration issue that must be flagged.

## 4. Vendors Dataset (`vendors.csv`)
* **Total Records:** 22,080
* **Duplicates:** 0 exact duplicate rows.
* **Missing Values:**
  * `financial_stability_score`: 2,650 records (12.00%). Should be imputed using the sector median.
  * `quality_acceptance_rate`: 1,766 records (8.00%).
  * `vris_score`: 1,546 records (7.00%).
* **Invalid Records & Outliers:**
  * `days_payable_outstanding`: 110 records (0.50%) have negative values.
  * *Referential Integrity:* ~1% of `product_id`s in the Orders table map to non-existent Vendor records.

## 5. Logistics Dataset (`logistics.csv`)
* **Total Records:** 125,660
* **Duplicates:** 0 exact duplicate rows (Note: Metadata flags ~3% duplicate `shipment_id`s from OTM integration errors).
* **Missing Values:**
  * `actual_delivery_date`: ~4% are NULL for shipments marked as 'Delivered'.
  * `delay_reason`: 121,913 records (97.02%) - Expected, as this is only populated for late shipments.
* **Invalid Records & Outliers:**
  * `fuel_cost_usd`: Metadata identifies ~6% extreme outliers (10x normal cost) requiring capping or transformation.

## 6. Financials Dataset (`financials.csv`)
* **Total Records:** 69,300
* **Duplicates:** 3,300 exact duplicate rows. These require immediate deduplication to prevent double-counting revenue/expenses.
* **Missing Values:**
  * `working_capital_ratio`: 4,167 records (6.01%).
  * `financial_risk_score`: 5,522 records (7.97%).
* **Invalid Records & Outliers:**
  * Negative Revenue/Margin: `gross_profit_usd` has 15,116 negative records (21.81%) and `ebitda_usd` has 17,147 negative records (24.74%). While some represent true loss orders, these must be validated against `order_value` and `cost_of_goods`.

---
## Next Steps (Remediation Strategy)
1. **Deduplicate:** Remove the 3,300 duplicate rows in `financials.csv` and deduplicate `orders.csv` on `order_id`.
2. **Impute/Handle NULLs:** Use historical averages for `reorder_point` and sector medians for `financial_stability_score`.
3. **Filter Invalids:** Flag and isolate the negative `stock_on_hand` and `order_value_usd` rows from Machine Learning training datasets.
