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
2. **Integrate External Data**: Incorporate data from an external source (chosen API) to compare internal pricing with market trends. For difficulties, I have created my own API with FastAPI.
3. **Generate Insights**: Provide actionable recommendations based on price comparisons, stock levels, and market trends.  
4. **Document Findings**: Summarize key insights in a business-friendly format.  

---

## Repository Structure 📂

```plaintext
├── README.md           # Setup & analysis documentation
├── data/
|   ├── products_simulation.json      #API JSON simulation
│   └── products.csv    # Internal product data
├── src/
|   ├── analysis.ipynb     #The notebook with the most organized graphics and view the pre-final process.
│   ├── analysis.py     # Main script for generating insights
│   └── utils.py        # Helper functions for data cleaning and analysis
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

#### To start the docker container:

1. Start the containers
```bash
docker compose up -d
```

#### To generated the recommendations and system alerts:
```bash
python .\src\analysis.py <path_of_you_csv_file>
```

In my case:

```bash
python .\src\analysis.py C:\Users\LENOVO\Documents\GitHub\technical_interview_10QS\data\products.csv
```


## Limitation 💢
In my case, the biggest limitation I found was that there were no APIs dealing with the products there, and if there were, it had only nutrient contents, i.e., it did not allow me to compare prices. So, the solution was to create and manipulate my own API and make other people not to worry about running it using docker.

## Time spent on each component ⏲️
* Discovering the API: 50 minutes
* Making my own API with FastAPI: 20 minutes
* Performing data extraction, transformation and loading functions (alerting and recommendation functions): 30 minutes
* EDA: 15 minutes
* Dockerizing: 15 minutes
