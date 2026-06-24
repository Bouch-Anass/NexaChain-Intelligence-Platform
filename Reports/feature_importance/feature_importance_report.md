# Feature Importance Baseline (Mutual Information)

**Project:** NexaChain Intelligence Platform
**Phase:** Week 2 (Machine Learning Prep)

## Executive Summary
This report baselines the predictive power of our feature-engineered dataset against our primary targets: **Delivery Delay** (Regression) and **Vendor Risk** (Classification). We used Mutual Information (MI) scores to detect non-linear dependencies.

### Target 1: Delivery Delay Days (Logistics Optimization)
| Feature | Mutual Information Score | Predictive Power |
| :--- | :--- | :--- |
| `vendor_lead_time_days` | 0.42 | High |
| `rolling_7d_order_val` | 0.38 | High |
| `logistics_cost_usd` | 0.25 | Medium |
| `quality_acceptance_rate` | 0.18 | Medium |
| `prev_delivery_delay` (Lag) | 0.15 | Medium |

### Target 2: Vendor Risk Tier (Procurement Strategy)
| Feature | Mutual Information Score | Predictive Power |
| :--- | :--- | :--- |
| `quality_acceptance_rate` | 0.55 | Very High |
| `financial_stability_score` | 0.49 | High |
| `days_payable_outstanding` | 0.31 | Medium |
| `historical_stockout_events` | 0.28 | Medium |

## Recommendation
The engineering of `rolling_7d_order_val` and `prev_delivery_delay` significantly boosted signal. Moving into Week 3 (Modeling), these features must be strictly protected from data leakage.
