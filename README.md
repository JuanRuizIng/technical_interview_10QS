# 10EQS Data Integration Challenge: Product Pricing Insights

**Created by Juan Andrés Ruiz Muñoz**  
GitHub: [@JuanRuizIng](https://github.com/JuanRuizIng)

## Overview ✨

This repository contains the solution for the **10EQS Data Integration Challenge**, designed to help a small business owner monitor their product pricing in relation to market conditions. The solution includes a pipeline for integrating internal product data with external market information and generating actionable business insights.

The repository is structured to ensure a seamless experience, from setting up the environment to running the analysis and obtaining insights.

---

## Goals 🎯

The objective is to:

1. **Process Internal Data**: Read and clean the provided `products.csv` dataset.  
2. **Integrate External Data**: Incorporate data from an external source (chosen API) to compare internal pricing with market trends. The API was [Open Exchange Rates API](https://docs.openexchangerates.org/reference/api-introduction).
3. **Generate Insights**: The insights generated include exchange rate analysis to identify currency trends, top variations to prioritize markets, and product price comparisons in local currencies. These insights guide pricing adjustments, promotional strategies, and resource allocation to align with market conditions.
4. **Document Findings**: Summarize key insights in a business-friendly format.  

---

## Repository Structure 📂

```plaintext
├── README.md           # Setup & analysis documentation
├── data/
|   ├── product_variation_colombia.json      #JSON with the variation products in Colombia (in local currency)
|   ├── variation_price.json        # JSON with variation (in local currency) of the price for each country
|   ├── variation_price_top.json    # JSON with the variation (in local currency) of the price for each country and save the top 5 results
│   └── products.csv    # Internal product data
├── src/
│   ├── analysis.py     # Main script for generating insights
│   └── utils.py        # Helper functions for data cleaning and the functions to compare prices for different dates
├── requirements.txt    # Python dependencies
└── report.md           # Generated insights report
```

## Running the code ⏯️

> [!NOTE]
> Notebook are omitted.

#### Clone the repository:

Execute the following command to clone the repository:

```bash
https://github.com/JuanRuizIng/technical_interview_10QS.git
```

#### Install dependencies:

1. Create venv

```bash
python -m venv venv
```

2. Run requirements

```bash
pip install -r requirements.txt
```

#### To generated the reports:
```bash
python .\src\analysis.py <path_of_you_csv_file>
```

In my case:

```bash
python .\src\analysis.py C:\Users\LENOVO\Documents\GitHub\technical_interview_10QS\data\products.csv
```


## Limitation 💢
In my case, the biggest limitation I found was that there were no APIs dealing with the products there, and if there were, it had only nutrient contents, i.e., it did not allow me to compare prices. So, the solution was search for an API to measure the exchange rate from dollars to different currencies in latin america.

## Time spent on each component ⏲️
* Discovering the API: 80 minutes
* Performing data extraction, transformation and loading functions (report functions): 40 minutes
