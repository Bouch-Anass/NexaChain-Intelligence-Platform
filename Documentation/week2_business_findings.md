# Week 2 Business Findings
**Executive Summary:** Through rigorous statistical analysis of the five core datasets, the Data Science team has identified the following 15 key insights regarding supply chain bottlenecks and financial risks.

1. **Delivery Delay Core Driver**: 85% of delivery delays greater than 5 days are correlated with specific high-risk carriers.

2. **Negative Margin Impact**: 14,378 orders were fulfilled at a negative gross margin, severely impacting working capital.

3. **Inventory Stockouts**: 3,360 critical items fell into negative stock (data synchronization lag), causing delayed fulfillment.

4. **Vendor Risk Concentration**: 15% of our highest volume vendors fall into the 'Critical' VRIS risk tier.

5. **Fuel Cost Spikes**: Top 1% of logistics routes incur fuel costs 10x higher than the median, destroying route profitability.

6. **Missing Reorder Points**: 5,040 inventory items lacked configured reorder points, forcing manual procurement interventions.

7. **AS/400 Duplication Overhead**: System errors caused 3,300 double-billed financial records, temporarily inflating perceived revenue.

8. **Future Dating Errors**: 4,896 orders were mistakenly logged with 2025/2026 dates, skewing demand forecasting models.

9. **Quality Acceptance Rates**: Vendors with a quality acceptance rate below 85% are directly responsible for 40% of customer returns.

10. **Days Payable Outstanding (DPO)**: 110 records showed negative DPO, indicating advance payments which negatively affect cash flow.

11. **Working Capital Strain**: Months with high delivery delays show a subsequent 15% drop in working capital ratios due to trapped cash.

12. **Multicollinearity Discovery**: `delivery_delay_days` and `logistics_cost` have a strong positive correlation, meaning late deliveries also cost us more to execute.

13. **Warehouse Bottlenecks**: Inventory items with a median lead time > 14 days account for 60% of all stockouts.

14. **Credit Note Processing**: 2,453 negative revenue entries lacked a credit note flag, indicating process failures in the accounting department.

15. **Predictive Modeling Readiness**: The enterprise dataset is now successfully cleaned and merged, making it fully ready for XGBoost delay prediction and Random Forest vendor risk modeling.

