import requests
import json
import pandas as pd
from dotenv import load_dotenv
import os

# Open Exchange Rates API
# https://docs.openexchangerates.org/reference/api-introduction


load_dotenv("./.env")

api_id = os.getenv("API_ID")

def get_data_target(target_date):
    """Get data from the API for the target date
    Args:
        target_date (str): Date format: YYYY-MM-DD
    
    Returns:
        dict: Data from the API for the target date
    
    Exceptions:
        Exception: Error message
    """

    try:
        url_target = f"https://openexchangerates.org/api/historical/{target_date}.json?app_id={api_id}&symbols=ARS,BOB,BRL,CLP,COP,CRC,CUP,XCD,USD,GTQ,HNL,MXN,NIO,PAB,PYG,PEN,DOP,UYU,VES"
        headers = {"accept": "application/json"}
        response_target = requests.get(url_target, headers=headers)
        response_target.raise_for_status()
        data = response_target.json()
        with open("./data/copy_api.json", "w") as json_file:
            json.dump(data, json_file)
        return data
    except Exception as e:
        return str(e)
    

def get_data_comparation(comparation_date):
    """Get data from the API for the comparation date
    
    Args:
        comparation_date (str): Date format: YYYY-MM-DD
    
    Returns:
        dict: Data from the API for the comparation date
    
    Exceptions:
        Exception: Error message
    """

    try:
        url_comparation = f"https://openexchangerates.org/api/historical/{comparation_date}.json?app_id={api_id}&symbols=ARS,BOB,BRL,CLP,COP,CRC,CUP,XCD,USD,GTQ,HNL,MXN,NIO,PAB,PYG,PEN,DOP,UYU,VES"
        headers = {"accept": "application/json"}
        response_comparation = requests.get(url_comparation, headers=headers)
        response_comparation.raise_for_status()
        data = response_comparation.json()
        with open("./data/copy_api.json", "w") as json_file:
            json.dump(data, json_file)
        return data
    except Exception as e:
        return str(e)
    

countries = {
    "ARS":"Argentina",
    "BOB":"Bolivia",
    "BRL":"Brazil",
    "CLP":"Chile",
    "COP":"Colombia",
    "CRC":"Costa Rica",
    "CUP":"Cuba",
    "XCD":"East Caribbean",
    "USD":"United States",
    "GTQ":"Guatemala",
    "HNL":"Honduras",
    "MXN":"Mexico",
    "NIO":"Nicaragua",
    "PAB":"Panama",
    "PYG":"Paraguay",
    "PEN":"Peru",
    "DOP":"Dominican Republic",
    "UYU":"Uruguay",
    "VES":"Venezuela"
}

def variation_price(df_target, df_comparation):
    """Calculate the variation (in local currency) of the price for each country between the target and comparation date and save the results in a JSON file
    
    Args:
        df_target (DataFrame): Data from the API for the target date
        df_comparation (DataFrame): Data from the API for the comparation date
    
    Returns:
        print: Results of the variation for each country
    
    Exceptions:
        Exception: Error message
    """

    try:
        results = {}
        for country in countries:
            if country == "USD":
                pass
            if df_target[country][0] > df_comparation[country][0]:
                results[countries[country]] = "DOWN"
            elif df_target[country][0] < df_comparation[country][0]:
                results[countries[country]] = "UP"
            else:
                results[countries[country]] = "EQUAL"
        with open("./data/variation_price.json", "w") as json_file:
            json.dump(results, json_file)
        return print(results)
    except Exception as e:
        return str(e)
    
def variation_price_top(df_target, df_comparation):
    """Calculate the variation (in local currency) of the price for each country between the target and comparation date and save the top 5 results in a JSON file

    Args:
        df_target (DataFrame): Data from the API for the target date
        df_comparation (DataFrame): Data from the API for the comparation date
    
    Returns:
        print: Results of the variation for each country
    
    Exceptions:
        Exception: Error message
    """
    
    try:
        results = {}
        for country in countries:
            if country == "USD":
                continue
            variation = df_target[country][0] - df_comparation[country][0]
            results[countries[country]] = round(variation, 4)
        results_order = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))
        results_order_up = dict(list(results_order.items())[:5])
        with open("./data/variation_price_top.json", "w") as json_file:
            json.dump(results_order_up, json_file)
        return print(results_order)
    except Exception as e:
        return str(e)
    

def product_variation_for_country(country_name, df_products, df_target, df_comparation):
    pass