# Salifort Motors Employee Turnover Analysis

Predictive analysis of employee turnover at Salifort Motors using Python, machine learning, and HR analytics.

## Overview

This capstone explores workforce data to identify the factors driving employee attrition and to support proactive retention strategies. The project combines data cleaning, exploratory analysis, feature engineering, and predictive modeling to deliver business-ready insights for HR and leadership.

## Business Problem

Employee turnover is a costly challenge for organizations, affecting productivity, morale, and hiring costs. At Salifort Motors, the analysis focuses on identifying the workload and engagement patterns most associated with attrition so leaders can intervene before valued employees leave.

## Objectives

- analyze employee data to find retention-risk drivers
- assess workload, satisfaction, and project-related signals
- build and evaluate a predictive model for turnover risk
- communicate findings in a clear, actionable format for stakeholders

## Key Findings

The analysis surfaced several strong predictors of turnover:

- excessive monthly working hours
- high project volume and workload imbalance
- low satisfaction and engagement signals
- under-utilization and mismatch between employee capacity and assigned work

## Modeling Approach

The workflow includes:

- data cleaning and validation
- feature engineering and transformation
- exploratory analysis and pattern detection
- model training and evaluation
- business interpretation of model results

## Results

The final Random Forest model achieved strong predictive performance on the test set:

- Accuracy: 98.6%
- Precision: 99.1%
- Recall: 92.2%
- F1-Score: 95.5%

These results indicate the model is highly effective at identifying at-risk employees while keeping false positives low.

## Business Recommendations

- establish workload caps and review monthly hour trends
- monitor employees assigned to very low or very high project counts
- conduct regular engagement check-ins for higher-risk employees
- deploy the model as an early-warning system for HR retention strategies

## Repository Structure

```text
advanced-data-analysis-capstone/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   └── project_summary.md
├── notebooks/
│   └── analysis.ipynb
├── results/
│   └── charts/
├── src/
│   ├── __init__.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── modeling.py
│   ├── utils.py
│   └── Activity_ Course 7 Salifort Motors project lab.ipynb
└── .gitignore
```

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/Gafardauda/salifort-motor-project.git
cd salifort-motor-project
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Launch Jupyter Notebook:

```bash
jupyter notebook
```

## Project Files

- [docs/project_summary.md](docs/project_summary.md) — executive summary of the capstone
- [notebooks/analysis.ipynb](notebooks/analysis.ipynb) — exploratory analysis and modeling workflow
- [src/data_cleaning.py](src/data_cleaning.py) — data cleaning utilities
- [src/feature_engineering.py](src/feature_engineering.py) — feature creation logic
- [src/modeling.py](src/modeling.py) — modeling helpers

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contributing

Contributions and feedback are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Project Summary

The project highlights a clear retention strategy for Salifort Motors: reduce burnout, improve workload balancing, and use predictive analytics to identify employees most at risk before they exit. This combination of operational and analytical intervention is the foundation of a stronger, more resilient workforce strategy.
