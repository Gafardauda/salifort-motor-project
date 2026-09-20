# Salifort Motors Employee Turnover Analysis

A portfolio-ready data analysis project focused on understanding employee attrition at Salifort Motors and using machine learning to identify retention risk.

## Overview

This capstone analyzes workforce data to uncover the patterns behind employee turnover and translate those findings into practical business recommendations. The project combines data cleaning, exploratory analysis, feature engineering, and predictive modeling to support HR and leadership decision-making.

## Business Problem

Employee turnover is costly for organizations, affecting productivity, morale, and hiring costs. At Salifort Motors, the analysis focuses on identifying which employee behaviors and workload patterns are most associated with attrition and which employees may need intervention before deciding to leave.

## Objectives

- analyze employee data and identify turnover drivers
- assess workload, satisfaction, and project-related signals
- build and evaluate a predictive retention model
- communicate findings in a clear, actionable format for stakeholders

## Key Findings

The analysis identified several strong indicators of turnover risk:

- excessive monthly working hours
- high project volume and workload imbalance
- low satisfaction or reduced engagement signals
- under-utilization and misalignment between workload and employee capacity

## Modeling Approach

The workflow includes:

- data cleaning and validation
- feature engineering and transformation
- exploratory analysis and pattern detection
- model training and evaluation
- business interpretation of the results

## Results

The final Random Forest model achieved strong performance on the test set:

- Accuracy: 98.6%
- Precision: 99.1%
- Recall: 92.2%
- F1-Score: 95.5%

These metrics demonstrate the model's effectiveness in identifying employees at high risk of turnover while limiting false positives.

## Business Recommendations

- Introduce workload caps and review monthly hour trends
- Monitor employees assigned to very low or very high project counts
- Use periodic engagement check-ins for higher-risk employees
- Deploy the model as an early-warning system for HR retention strategies

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
git clone https://github.com/<your-username>/advanced-data-analysis-capstone.git
cd advanced-data-analysis-capstone
```

2. Create a virtual environment:

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
- [notebooks/analysis.ipynb](notebooks/analysis.ipynb) — full exploratory analysis and modeling workflow
- [src/data_cleaning.py](src/data_cleaning.py) — data cleaning utilities
- [src/feature_engineering.py](src/feature_engineering.py) — feature creation logic
- [src/modeling.py](src/modeling.py) — modeling helpers

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contributing

Contributions and feedback are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Publish to GitHub

Once you are ready to publish the project, run:

```bash
git add .
git commit -m "Initial capstone project setup"
git branch -M main
git remote add origin https://github.com/<your-username>/advanced-data-analysis-capstone.git
git push -u origin main
```

This repo is now structured as a clean, portfolio-ready public project.
