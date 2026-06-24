# Univariate Analysis Report
**Project:** NexaChain Intelligence Platform
**Phase:** Week 2 - Statistical Analysis

This report provides a comprehensive statistical breakdown of all numerical variables across the cleaned enterprise datasets. It includes the calculation of central tendency, dispersion, and shape (skewness/kurtosis) for future predictive modeling.

## Dataset: `financials_cleaned.csv`
### Variable: `fiscal_week`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 26.4691 |
| **Median** | 26.0000 |
| **Min** | 1 |
| **Max** | 53 |
| **Range** | 52 |
| **Variance** | 227.3870 |
| **Std Dev** | 15.0794 |
| **Skewness** | 0.0067 |
| **Kurtosis** | -1.2055 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `fiscal_year`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 2,022.5005 |
| **Median** | 2,023.0000 |
| **Min** | 2,021 |
| **Max** | 2,024 |
| **Range** | 3 |
| **Variance** | 1.2486 |
| **Std Dev** | 1.1174 |
| **Skewness** | -0.0025 |
| **Kurtosis** | -1.3585 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `revenue_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 20,044.0168 |
| **Median** | 0.0000 |
| **Min** | 0.0000 |
| **Max** | 7,556,744.3300 |
| **Range** | 7,556,744.3300 |
| **Variance** | 11,669,445,908.7253 |
| **Std Dev** | 108,025.2096 |
| **Skewness** | 24.8481 |
| **Kurtosis** | 1,103.7675 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `procurement_cost_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 7,167.3758 |
| **Median** | 0.0000 |
| **Min** | 0.0000 |
| **Max** | 2,017,344.4100 |
| **Range** | 2,017,344.4100 |
| **Variance** | 1,460,376,597.0501 |
| **Std Dev** | 38,214.8740 |
| **Skewness** | 18.0789 |
| **Kurtosis** | 557.0124 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `logistics_cost_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 455.1671 |
| **Median** | 0.0000 |
| **Min** | 0.0000 |
| **Max** | 191,220.0600 |
| **Range** | 191,220.0600 |
| **Variance** | 7,555,337.5178 |
| **Std Dev** | 2,748.6974 |
| **Skewness** | 19.7801 |
| **Kurtosis** | 744.7456 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `operational_cost_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 486.8795 |
| **Median** | 0.0000 |
| **Min** | 0.0000 |
| **Max** | 122,943.2800 |
| **Range** | 122,943.2800 |
| **Variance** | 5,990,695.2613 |
| **Std Dev** | 2,447.5897 |
| **Skewness** | 12.2130 |
| **Kurtosis** | 278.3311 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `sla_penalty_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 771.9263 |
| **Median** | 0.0000 |
| **Min** | 0.0000 |
| **Max** | 129,083.6200 |
| **Range** | 129,083.6200 |
| **Variance** | 22,783,797.4301 |
| **Std Dev** | 4,773.2376 |
| **Skewness** | 9.3041 |
| **Kurtosis** | 115.3704 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `gross_profit_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 19,101.9702 |
| **Median** | 0.0000 |
| **Min** | -191,220.0600 |
| **Max** | 7,556,744.3300 |
| **Range** | 7,747,964.3900 |
| **Variance** | 11,720,314,079.8431 |
| **Std Dev** | 108,260.3994 |
| **Skewness** | 24.7105 |
| **Kurtosis** | 1,095.0422 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `ebitda_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 17,628.0579 |
| **Median** | 0.0000 |
| **Min** | -351,507.1300 |
| **Max** | 7,556,744.3300 |
| **Range** | 7,908,251.4600 |
| **Variance** | 11,920,099,210.6232 |
| **Std Dev** | 109,179.2069 |
| **Skewness** | 24.1085 |
| **Kurtosis** | 1,059.8862 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `accounts_receivable_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 121,388.0602 |
| **Median** | 59,558.7450 |
| **Min** | 274.7100 |
| **Max** | 6,752,605.8500 |
| **Range** | 6,752,331.1400 |
| **Variance** | 43,476,577,631.1462 |
| **Std Dev** | 208,510.3778 |
| **Skewness** | 7.6053 |
| **Kurtosis** | 114.1858 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `accounts_payable_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 90,357.3487 |
| **Median** | 48,871.3850 |
| **Min** | 346.2200 |
| **Max** | 5,720,145.0600 |
| **Range** | 5,719,798.8400 |
| **Variance** | 19,813,592,940.9205 |
| **Std Dev** | 140,760.7649 |
| **Skewness** | 8.0017 |
| **Kurtosis** | 150.4716 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `inventory_value_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 162,976.7514 |
| **Median** | 98,998.2800 |
| **Min** | 1,321.8500 |
| **Max** | 6,595,673.2300 |
| **Range** | 6,594,351.3800 |
| **Variance** | 46,433,743,735.6275 |
| **Std Dev** | 215,484.9037 |
| **Skewness** | 6.0678 |
| **Kurtosis** | 79.7090 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `working_capital_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 194,007.4629 |
| **Median** | 131,863.3550 |
| **Min** | -5,563,289.6700 |
| **Max** | 7,042,804.8500 |
| **Range** | 12,606,094.5200 |
| **Variance** | 109,986,374,834.5252 |
| **Std Dev** | 331,641.9377 |
| **Skewness** | 2.9598 |
| **Kurtosis** | 36.7322 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `working_capital_ratio`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 10.2794 |
| **Median** | 4.0794 |
| **Min** | 0.0174 |
| **Max** | 1,560.6880 |
| **Range** | 1,560.6706 |
| **Variance** | 620.2648 |
| **Std Dev** | 24.9051 |
| **Skewness** | 14.1304 |
| **Kurtosis** | 438.2131 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `cash_flow_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 47,092.7078 |
| **Median** | 47,067.6950 |
| **Min** | -3,435,768.6500 |
| **Max** | 3,442,270.1800 |
| **Range** | 6,878,038.8300 |
| **Variance** | 638,744,771,130.5895 |
| **Std Dev** | 799,215.0969 |
| **Skewness** | -0.0010 |
| **Kurtosis** | 0.0029 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `cash_position_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 1,372,890.0745 |
| **Median** | 439,661.4700 |
| **Min** | 315.0300 |
| **Max** | 758,409,832.6000 |
| **Range** | 758,409,517.5700 |
| **Variance** | 23,050,177,616,587.9297 |
| **Std Dev** | 4,801,060.0513 |
| **Skewness** | 68.0385 |
| **Kurtosis** | 9,625.0506 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `days_sales_outstanding`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 57.9932 |
| **Median** | 58.0700 |
| **Min** | 4.3900 |
| **Max** | 109.9600 |
| **Range** | 105.5700 |
| **Variance** | 143.9630 |
| **Std Dev** | 11.9985 |
| **Skewness** | 0.0019 |
| **Kurtosis** | 0.0104 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `days_payable_outstanding`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 67.9121 |
| **Median** | 67.8600 |
| **Min** | 1.1300 |
| **Max** | 130.5100 |
| **Range** | 129.3800 |
| **Variance** | 224.6293 |
| **Std Dev** | 14.9876 |
| **Skewness** | 0.0084 |
| **Kurtosis** | 0.0104 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `cash_conversion_cycle`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 35.1454 |
| **Median** | 35.2400 |
| **Min** | -62.5900 |
| **Max** | 125.8800 |
| **Range** | 188.4700 |
| **Variance** | 467.7579 |
| **Std Dev** | 21.6277 |
| **Skewness** | -0.0072 |
| **Kurtosis** | 0.0078 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `financial_risk_score`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 24.3526 |
| **Median** | 23.1600 |
| **Min** | 20.0000 |
| **Max** | 56.9800 |
| **Range** | 36.9800 |
| **Variance** | 21.5145 |
| **Std Dev** | 4.6384 |
| **Skewness** | 1.7960 |
| **Kurtosis** | 3.7585 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `is_loss_order`
| Metric | Value |
| :--- | :--- |
| **Count** | 66,000 |
| **Mean** | 0.2178 |
| **Median** | 0.0000 |
| **Min** | 0 |
| **Max** | 1 |
| **Range** | 1 |
| **Variance** | 0.1704 |
| **Std Dev** | 0.4128 |
| **Skewness** | 1.3671 |
| **Kurtosis** | -0.1310 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

## Dataset: `inventory_cleaned.csv`
### Variable: `stock_on_hand`
| Metric | Value |
| :--- | :--- |
| **Count** | 56,000 |
| **Mean** | 435.5407 |
| **Median** | 132.0000 |
| **Min** | 0 |
| **Max** | 66,101 |
| **Range** | 66,101 |
| **Variance** | 1,508,934.0183 |
| **Std Dev** | 1,228.3868 |
| **Skewness** | 14.1793 |
| **Kurtosis** | 394.8720 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `units_reserved`
| Metric | Value |
| :--- | :--- |
| **Count** | 56,000 |
| **Mean** | 91.8577 |
| **Median** | 23.0000 |
| **Min** | 0 |
| **Max** | 18,200 |
| **Range** | 18,200 |
| **Variance** | 88,801.1091 |
| **Std Dev** | 297.9951 |
| **Skewness** | 18.3614 |
| **Kurtosis** | 668.4870 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `available_stock`
| Metric | Value |
| :--- | :--- |
| **Count** | 56,000 |
| **Mean** | 373.1229 |
| **Median** | 118.0000 |
| **Min** | 0 |
| **Max** | 57,081 |
| **Range** | 57,081 |
| **Variance** | 1,064,586.3205 |
| **Std Dev** | 1,031.7879 |
| **Skewness** | 13.9762 |
| **Kurtosis** | 390.1805 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `reorder_point`
| Metric | Value |
| :--- | :--- |
| **Count** | 56,000 |
| **Mean** | 647.8814 |
| **Median** | 327.6000 |
| **Min** | 6.0000 |
| **Max** | 21,168.0000 |
| **Range** | 21,162.0000 |
| **Variance** | 1,066,136.1419 |
| **Std Dev** | 1,032.5387 |
| **Skewness** | 5.5415 |
| **Kurtosis** | 51.6758 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `reorder_quantity`
| Metric | Value |
| :--- | :--- |
| **Count** | 56,000 |
| **Mean** | 1,103.0577 |
| **Median** | 546.0000 |
| **Min** | 10 |
| **Max** | 40,180 |
| **Range** | 40,170 |
| **Variance** | 3,133,644.7363 |
| **Std Dev** | 1,770.2104 |
| **Skewness** | 5.6436 |
| **Kurtosis** | 55.5777 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `safety_stock_units`
| Metric | Value |
| :--- | :--- |
| **Count** | 56,000 |
| **Mean** | 125.4356 |
| **Median** | 70.0000 |
| **Min** | 3 |
| **Max** | 3,697 |
| **Range** | 3,694 |
| **Variance** | 32,985.7191 |
| **Std Dev** | 181.6197 |
| **Skewness** | 5.3017 |
| **Kurtosis** | 49.9682 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `max_stock_level`
| Metric | Value |
| :--- | :--- |
| **Count** | 56,000 |
| **Mean** | 2,867.6174 |
| **Median** | 1,419.0000 |
| **Min** | 26 |
| **Max** | 104,468 |
| **Range** | 104,442 |
| **Variance** | 21,183,522.9312 |
| **Std Dev** | 4,602.5561 |
| **Skewness** | 5.6436 |
| **Kurtosis** | 55.5774 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `days_of_supply`
| Metric | Value |
| :--- | :--- |
| **Count** | 56,000 |
| **Mean** | 119.0757 |
| **Median** | 22.2500 |
| **Min** | 0.0000 |
| **Max** | 30,571.0000 |
| **Range** | 30,571.0000 |
| **Variance** | 237,128.6385 |
| **Std Dev** | 486.9586 |
| **Skewness** | 22.1215 |
| **Kurtosis** | 875.9196 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `vendor_lead_time_days`
| Metric | Value |
| :--- | :--- |
| **Count** | 56,000 |
| **Mean** | 47.4406 |
| **Median** | 48.0000 |
| **Min** | 5.0000 |
| **Max** | 90.0000 |
| **Range** | 85.0000 |
| **Variance** | 582.4004 |
| **Std Dev** | 24.1330 |
| **Skewness** | -0.0028 |
| **Kurtosis** | -1.0971 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `stock_age_days`
| Metric | Value |
| :--- | :--- |
| **Count** | 56,000 |
| **Mean** | 365.0256 |
| **Median** | 366.0000 |
| **Min** | 0 |
| **Max** | 730 |
| **Range** | 730 |
| **Variance** | 44,446.6609 |
| **Std Dev** | 210.8238 |
| **Skewness** | -0.0018 |
| **Kurtosis** | -1.2017 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `holding_cost_rate_pct`
| Metric | Value |
| :--- | :--- |
| **Count** | 56,000 |
| **Mean** | 3.0365 |
| **Median** | 2.8100 |
| **Min** | 1.0000 |
| **Max** | 20.2500 |
| **Range** | 19.2500 |
| **Variance** | 4.2720 |
| **Std Dev** | 2.0669 |
| **Skewness** | 4.6036 |
| **Kurtosis** | 28.5790 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `unit_cost_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 56,000 |
| **Mean** | 67.6425 |
| **Median** | 33.2600 |
| **Min** | 0.2300 |
| **Max** | 5,332.3200 |
| **Range** | 5,332.0900 |
| **Variance** | 13,960.4301 |
| **Std Dev** | 118.1543 |
| **Skewness** | 8.2973 |
| **Kurtosis** | 153.3240 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `total_inventory_value_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 56,000 |
| **Mean** | 32,197.8900 |
| **Median** | 4,885.7100 |
| **Min** | 0.0000 |
| **Max** | 49,860,887.0400 |
| **Range** | 49,860,887.0400 |
| **Variance** | 73,260,916,929.5415 |
| **Std Dev** | 270,667.5395 |
| **Skewness** | 122.4205 |
| **Kurtosis** | 21,099.9828 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

## Dataset: `logistics_cleaned.csv`
### Variable: `order_quantity`
| Metric | Value |
| :--- | :--- |
| **Count** | 125,660 |
| **Mean** | 40.7447 |
| **Median** | 20.0000 |
| **Min** | 1 |
| **Max** | 4,336 |
| **Range** | 4,335 |
| **Variance** | 5,138.2654 |
| **Std Dev** | 71.6817 |
| **Skewness** | 9.5252 |
| **Kurtosis** | 255.0554 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `unit_price_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 125,660 |
| **Mean** | 278.6052 |
| **Median** | 90.3050 |
| **Min** | 0.1600 |
| **Max** | 84,387.2900 |
| **Range** | 84,387.1300 |
| **Variance** | 691,682.7543 |
| **Std Dev** | 831.6747 |
| **Skewness** | 26.3628 |
| **Kurtosis** | 1,604.1614 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `order_value_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 125,660 |
| **Mean** | 9,483.3651 |
| **Median** | 1,446.7100 |
| **Min** | -1,228,295.6600 |
| **Max** | 3,923,386.1500 |
| **Range** | 5,151,681.8100 |
| **Variance** | 2,525,679,756.9924 |
| **Std Dev** | 50,256.1415 |
| **Skewness** | 30.0198 |
| **Kurtosis** | 1,599.9769 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `discount_pct`
| Metric | Value |
| :--- | :--- |
| **Count** | 125,660 |
| **Mean** | 12.5187 |
| **Median** | 12.5600 |
| **Min** | 0.0000 |
| **Max** | 25.0000 |
| **Range** | 25.0000 |
| **Variance** | 51.9500 |
| **Std Dev** | 7.2076 |
| **Skewness** | -0.0056 |
| **Kurtosis** | -1.1983 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `cost_of_goods_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 125,660 |
| **Mean** | 6,084.6508 |
| **Median** | 923.3900 |
| **Min** | 0.2000 |
| **Max** | 2,781,869.1900 |
| **Range** | 2,781,868.9900 |
| **Variance** | 977,144,678.0341 |
| **Std Dev** | 31,259.3135 |
| **Skewness** | 30.7393 |
| **Kurtosis** | 1,623.2121 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `gross_margin_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 125,660 |
| **Mean** | 3,806.1206 |
| **Median** | 565.8350 |
| **Min** | 0.1500 |
| **Max** | 1,959,901.7900 |
| **Range** | 1,959,901.6400 |
| **Variance** | 394,916,376.2845 |
| **Std Dev** | 19,872.5030 |
| **Skewness** | 34.3945 |
| **Kurtosis** | 2,124.4021 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `profit_margin_pct`
| Metric | Value |
| :--- | :--- |
| **Count** | 119,377 |
| **Mean** | 38.4703 |
| **Median** | 38.4600 |
| **Min** | 21.9900 |
| **Max** | 55.0000 |
| **Range** | 33.0100 |
| **Variance** | 90.3013 |
| **Std Dev** | 9.5027 |
| **Skewness** | 0.0028 |
| **Kurtosis** | -1.1942 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `delivery_delay_days`
| Metric | Value |
| :--- | :--- |
| **Count** | 75,588 |
| **Mean** | -0.0280 |
| **Median** | 0.0000 |
| **Min** | -35.0000 |
| **Max** | 37.0000 |
| **Range** | 72.0000 |
| **Variance** | 58.2999 |
| **Std Dev** | 7.6354 |
| **Skewness** | 0.0025 |
| **Kurtosis** | 0.2252 |

> **Observation:** This variable has a relatively symmetrical distribution.

## Dataset: `orders_cleaned.csv`
### Variable: `order_quantity`
| Metric | Value |
| :--- | :--- |
| **Count** | 122,000 |
| **Mean** | 40.6936 |
| **Median** | 20.0000 |
| **Min** | 1 |
| **Max** | 4,336 |
| **Range** | 4,335 |
| **Variance** | 5,140.9696 |
| **Std Dev** | 71.7006 |
| **Skewness** | 9.6546 |
| **Kurtosis** | 261.3638 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `unit_price_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 122,000 |
| **Mean** | 278.4738 |
| **Median** | 90.4450 |
| **Min** | 0.1600 |
| **Max** | 84,387.2900 |
| **Range** | 84,387.1300 |
| **Variance** | 689,317.1939 |
| **Std Dev** | 830.2513 |
| **Skewness** | 26.7343 |
| **Kurtosis** | 1,649.3522 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `order_value_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 119,547 |
| **Mean** | 9,879.8673 |
| **Median** | 1,515.1400 |
| **Min** | 0.3500 |
| **Max** | 3,923,386.1500 |
| **Range** | 3,923,385.8000 |
| **Variance** | 2,549,963,871.4122 |
| **Std Dev** | 50,497.1670 |
| **Skewness** | 31.2231 |
| **Kurtosis** | 1,640.3871 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `discount_pct`
| Metric | Value |
| :--- | :--- |
| **Count** | 122,000 |
| **Mean** | 12.5211 |
| **Median** | 12.5600 |
| **Min** | 0.0000 |
| **Max** | 25.0000 |
| **Range** | 25.0000 |
| **Variance** | 51.9520 |
| **Std Dev** | 7.2078 |
| **Skewness** | -0.0053 |
| **Kurtosis** | -1.1982 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `cost_of_goods_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 122,000 |
| **Mean** | 6,083.9077 |
| **Median** | 922.8800 |
| **Min** | 0.2000 |
| **Max** | 2,781,869.1900 |
| **Range** | 2,781,868.9900 |
| **Variance** | 988,540,102.9007 |
| **Std Dev** | 31,441.0576 |
| **Skewness** | 30.9578 |
| **Kurtosis** | 1,631.8087 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `gross_margin_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 122,000 |
| **Mean** | 3,804.4216 |
| **Median** | 565.6450 |
| **Min** | 0.1500 |
| **Max** | 1,959,901.7900 |
| **Range** | 1,959,901.6400 |
| **Variance** | 398,688,746.6925 |
| **Std Dev** | 19,967.1918 |
| **Skewness** | 34.7078 |
| **Kurtosis** | 2,143.8726 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `profit_margin_pct`
| Metric | Value |
| :--- | :--- |
| **Count** | 115,899 |
| **Mean** | 38.4691 |
| **Median** | 38.4600 |
| **Min** | 21.9900 |
| **Max** | 55.0000 |
| **Range** | 33.0100 |
| **Variance** | 90.3502 |
| **Std Dev** | 9.5053 |
| **Skewness** | 0.0029 |
| **Kurtosis** | -1.1952 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `delivery_delay_days`
| Metric | Value |
| :--- | :--- |
| **Count** | 73,368 |
| **Mean** | -0.0288 |
| **Median** | 0.0000 |
| **Min** | -35.0000 |
| **Max** | 37.0000 |
| **Range** | 72.0000 |
| **Variance** | 58.3400 |
| **Std Dev** | 7.6381 |
| **Skewness** | 0.0051 |
| **Kurtosis** | 0.2210 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `data_entry_error`
| Metric | Value |
| :--- | :--- |
| **Count** | 122,000 |
| **Mean** | 0.0201 |
| **Median** | 0.0000 |
| **Min** | 0 |
| **Max** | 1 |
| **Range** | 1 |
| **Variance** | 0.0197 |
| **Std Dev** | 0.1404 |
| **Skewness** | 6.8379 |
| **Kurtosis** | 44.7574 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

## Dataset: `vendors_cleaned.csv`
### Variable: `on_time_delivery_rate`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 79.4919 |
| **Median** | 78.9700 |
| **Min** | 45.7200 |
| **Max** | 100.0000 |
| **Range** | 54.2800 |
| **Variance** | 100.2877 |
| **Std Dev** | 10.0144 |
| **Skewness** | 0.1051 |
| **Kurtosis** | -0.4221 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `quality_acceptance_rate`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 79.4523 |
| **Median** | 78.5500 |
| **Min** | 50.4000 |
| **Max** | 100.0000 |
| **Range** | 49.6000 |
| **Variance** | 69.8949 |
| **Std Dev** | 8.3603 |
| **Skewness** | 0.3993 |
| **Kurtosis** | -0.0440 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `quality_rejection_count`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 2.0490 |
| **Median** | 2.0000 |
| **Min** | 0 |
| **Max** | 10 |
| **Range** | 10 |
| **Variance** | 2.7873 |
| **Std Dev** | 1.6695 |
| **Skewness** | 0.8313 |
| **Kurtosis** | 0.5719 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `defect_rate_pct`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 0.1634 |
| **Median** | 0.0990 |
| **Min** | 0.0000 |
| **Max** | 1.8940 |
| **Range** | 1.8940 |
| **Variance** | 0.0361 |
| **Std Dev** | 0.1899 |
| **Skewness** | 2.3594 |
| **Kurtosis** | 7.9290 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `lead_time_avg_days`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 33.4672 |
| **Median** | 32.6900 |
| **Min** | 3.8600 |
| **Max** | 89.3900 |
| **Range** | 85.5300 |
| **Variance** | 274.2464 |
| **Std Dev** | 16.5604 |
| **Skewness** | 0.2447 |
| **Kurtosis** | -0.8505 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `lead_time_variance_days`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 2.6709 |
| **Median** | 1.8700 |
| **Min** | 0.0000 |
| **Max** | 23.0700 |
| **Range** | 23.0700 |
| **Variance** | 6.6056 |
| **Std Dev** | 2.5701 |
| **Skewness** | 1.6936 |
| **Kurtosis** | 3.6971 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `contract_lead_time_days`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 33.5072 |
| **Median** | 33.0000 |
| **Min** | 7 |
| **Max** | 60 |
| **Range** | 53 |
| **Variance** | 244.2622 |
| **Std Dev** | 15.6289 |
| **Skewness** | 0.0064 |
| **Kurtosis** | -1.1979 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `procurement_spend_usd`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 68,792.4735 |
| **Median** | 22,180.5050 |
| **Min** | 42.4300 |
| **Max** | 10,416,080.7200 |
| **Range** | 10,416,038.2900 |
| **Variance** | 42,708,656,134.7633 |
| **Std Dev** | 206,660.7271 |
| **Skewness** | 18.0135 |
| **Kurtosis** | 573.9914 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `purchase_order_count`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 12.0387 |
| **Median** | 12.0000 |
| **Min** | 1 |
| **Max** | 28 |
| **Range** | 27 |
| **Variance** | 12.0989 |
| **Std Dev** | 3.4783 |
| **Skewness** | 0.2679 |
| **Kurtosis** | 0.0076 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `invoice_accuracy_rate`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 91.9180 |
| **Median** | 92.0200 |
| **Min** | 67.9000 |
| **Max** | 100.0000 |
| **Range** | 32.1000 |
| **Variance** | 22.6820 |
| **Std Dev** | 4.7626 |
| **Skewness** | -0.2675 |
| **Kurtosis** | -0.2879 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `payment_terms_days`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 61.5652 |
| **Median** | 60.0000 |
| **Min** | 15 |
| **Max** | 120 |
| **Range** | 105 |
| **Variance** | 1,295.7610 |
| **Std Dev** | 35.9967 |
| **Skewness** | 0.3650 |
| **Kurtosis** | -1.1490 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `days_payable_outstanding`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 61.6002 |
| **Median** | 54.8900 |
| **Min** | -0.0000 |
| **Max** | 149.5300 |
| **Range** | 149.5300 |
| **Variance** | 1,357.4222 |
| **Std Dev** | 36.8432 |
| **Skewness** | 0.3425 |
| **Kurtosis** | -1.0473 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `concentration_risk_pct`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 23.6660 |
| **Median** | 23.6600 |
| **Min** | 2.0000 |
| **Max** | 45.0000 |
| **Range** | 43.0000 |
| **Variance** | 155.6849 |
| **Std Dev** | 12.4774 |
| **Skewness** | -0.0129 |
| **Kurtosis** | -1.2103 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `financial_stability_score`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 64.5854 |
| **Median** | 64.8500 |
| **Min** | 10.0000 |
| **Max** | 100.0000 |
| **Range** | 90.0000 |
| **Variance** | 326.5079 |
| **Std Dev** | 18.0695 |
| **Skewness** | -0.1758 |
| **Kurtosis** | -0.0514 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `esg_compliance_score`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 59.7945 |
| **Median** | 59.7650 |
| **Min** | 20.0000 |
| **Max** | 100.0000 |
| **Range** | 80.0000 |
| **Variance** | 223.1160 |
| **Std Dev** | 14.9371 |
| **Skewness** | 0.0073 |
| **Kurtosis** | -0.1694 |

> **Observation:** This variable has a relatively symmetrical distribution.

### Variable: `past_disruption_count`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 0.2948 |
| **Median** | 0.0000 |
| **Min** | 0 |
| **Max** | 5 |
| **Range** | 5 |
| **Variance** | 0.2913 |
| **Std Dev** | 0.5397 |
| **Skewness** | 1.8513 |
| **Kurtosis** | 3.6587 |

> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.

### Variable: `vris_score`
| Metric | Value |
| :--- | :--- |
| **Count** | 22,080 |
| **Mean** | 75.3090 |
| **Median** | 75.2400 |
| **Min** | 53.2700 |
| **Max** | 95.4800 |
| **Range** | 42.2100 |
| **Variance** | 31.9715 |
| **Std Dev** | 5.6543 |
| **Skewness** | 0.0727 |
| **Kurtosis** | 0.0695 |

> **Observation:** This variable has a relatively symmetrical distribution.

