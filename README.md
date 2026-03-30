# Carbon Emissions Analysis

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![License](https://img.shields.io/badge/License-MIT-green)

An in-depth data analysis exploring the relationship between global CO₂ concentrations and temperature anomalies, with predictive modeling and climate pattern clustering.

## Overview

Climate change is one of the most critical challenges of our time, with rising carbon emissions playing a pivotal role in driving global temperature anomalies. This analysis investigates the relationship between CO₂ concentrations and temperature changes using historical data from 1958-2024.

## Features

- **Data Exploration**: Load and analyze temperature and CO₂ datasets
- **Statistical Analysis**: Calculate mean, median, and variance for both datasets
- **Time-Series Visualization**: Interactive charts showing temperature and CO₂ trends over time
- **Correlation Analysis**: Pearson and Spearman correlation coefficients
- **Granger Causality Testing**: Investigate causal relationships between CO₂ and temperature
- **Lagged Effects Analysis**: OLS regression with lagged CO₂ variables
- **Climate Pattern Clustering**: K-Means clustering to identify distinct climate periods
- **Predictive Modeling**: Linear regression with "what-if" scenarios

## Datasets

| Dataset | Description | Time Range |
|---------|-------------|------------|
| `temperature.csv` | Annual temperature anomalies (°C) by country | 1961-2022 |
| `carbon_emmission.csv` | Monthly global CO₂ concentrations (ppm) | 1958-2024 |

## Key Findings

- **Strong Correlation**: 0.96 correlation between CO₂ and temperature change
- **Trend Analysis**: CO₂ increases at 0.32 ppm/year; temperature rises 0.03°C/year
- **R² = 0.949**: 94.9% of temperature variance explained by CO₂ levels
- **Seasonal Variation**: CO₂ peaks in May, lowest in September

## What-If Scenarios

| Scenario | Predicted Temperature Change (°C) |
|----------|-----------------------------------|
| CO₂ +10% | +1.09 |
| CO₂ -10% | -0.06 |
| CO₂ +20% | +1.66 |
| CO₂ -20% | -0.63 |

## Installation

```bash
# Clone the repository
git clone https://github.com/saddamchandio/Carbon-Emissions-Analysis.git

# Navigate to the project directory
cd Carbon-Emissions-Analysis

# Install required packages
pip install pandas numpy plotly scikit-learn statsmodels scipy
```

## Usage

Open the Jupyter notebook:

```bash
jupyter notebook CarbonEmissions.ipynb
```

Or view the rendered analysis on GitHub.

## Technologies Used

- **Python 3.13**
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Plotly** - Interactive visualizations
- **Scikit-learn** - Machine learning (K-Means, Linear Regression)
- **Statsmodels** - Statistical analysis
- **SciPy** - Scientific computing

## Project Structure

```
Carbon-Emissions-Analysis/
├── data/
│   ├── carbon_emmission.csv
│   └── temperature.csv
├── CarbonEmissions.ipynb
└── README.md
```

## Author

**By Engr. Saddam Hussain**, Data Scientist of Energy Systems and Agentic AI Engineer

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

*This analysis provides valuable insights into the connection between carbon emissions and climate change, supporting data-driven approaches for sustainable policy-making.*
