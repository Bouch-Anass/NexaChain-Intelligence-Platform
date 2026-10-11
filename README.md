# NexaChain Intelligence Platform

**Supply-chain data preparation and exploratory analytics with Python.**

NexaChain explores how orders, inventory, logistics, vendor and financial data can support supply-chain decisions. This repository contains data-cleaning scripts, statistical analyses and written reports, forming the analytical foundation for future predictive modeling.

## Explore the project

- [Business context and objectives](Documentation/project_understanding.md)
- [Dataset overview](Reports/dataset_understanding.md)
- [Data-quality assessment](Reports/data_profiling_report.md)
- [Cleaning decisions](Reports/data_cleaning_report.md)
- [Correlation analysis](Reports/statistical_analysis/correlation_report.md)
- [Univariate analysis PDF](Reports/statistical_analysis/univariate_analysis.pdf)

## What is implemented

| Area | Work included |
| --- | --- |
| Data preparation | Separate cleaning scripts for orders, inventory, logistics, vendors and financials |
| Quality checks | Duplicate handling, date validation, category standardization and numeric-value checks |
| Exploratory analysis | Univariate summaries and Pearson correlations across joined datasets |
| Vendor analysis | Rule-based segmentation using the existing vendor risk score |
| Financial analysis | Monthly gross-profit aggregation |
| Reporting | Markdown reports and Python scripts for PDF generation |

**Current scope:** the committed work covers preparation, exploration and reporting. Trained prediction models, deployed services, dashboards and an MLOps pipeline are not included in this version.

## Tools

Python · pandas · NumPy · Git

The [environment notes](Documentation/Environment_Setup_Confirmation.md) record Python 3.11, pandas 2.2.3 and NumPy 2.0.2. Dependencies used by individual PDF generators should be checked in their imports.

## Repository guide

| Folder | Contents |
| --- | --- |
| [Data](Data) | Source CSV files and cleaned copies |
| [scripts](scripts) | Cleaning, analysis and PDF-generation scripts |
| [Notebooks](Notebooks) | Data-profiling Python script |
| [Reports](Reports) | Data-quality, statistical and financial outputs |
| [Documentation](Documentation) | Business context, environment notes and working findings |

## Run a cleaning example

The existing scripts use Windows-style paths. From the repository root on Windows, with Python installed:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install pandas==2.2.3 numpy==2.0.2
.\.venv\Scripts\python.exe scripts\clean_orders.py
```

This example reads `Data/orders.csv` and rewrites `Data/cleaned/orders_cleaned.csv`. Review the script's cleaning rules before rerunning it. Other analyses use the cleaned datasets already included in the repository.

These commands document the inspected code and environment notes; they have not been execution-tested as part of this documentation update.

## Interpretation and limitations

- The narrative findings produced by `generate_business_findings()` in `scripts/business_discovery.py` are hardcoded. Their percentages and causal statements require independent calculation and validation before use as measured results.
- Vendor risk tiers are rule-based bins of an existing score, not predictions from a trained model.
- The financial script aggregates gross profit; this is not a full cash-flow statement.
- Correlations are exploratory associations and do not establish causation.
- Some scripts contain Windows-specific paths. Cross-platform execution requires path cleanup.

## Next steps

- Replace narrative constants with reproducible calculations.
- Validate joins and cleaning assumptions with automated checks.
- Standardize paths and dependency management.
- Establish forecasting and risk-model baselines with documented evaluation.
