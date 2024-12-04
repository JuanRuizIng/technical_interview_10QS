import requests
import json
import pandas as pd
from dotenv import load_dotenv
import os

# Open Exchange Rates API
# https://docs.openexchangerates.org/reference/api-introduction


load_dotenv("./.env")

api_id = os.getenv("API_ID")


def general_cleaning_data(df):
    """ It cleans the original DataFrame 
    
    Args:
        df (pd.DataFrame): A DataFrame with the products
        
    Returns:
        pd.DataFrame: A cleaned DataFrame
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    if 'product_name' in df.columns and 'product_name_' in df.columns:
        df['product_name'] = df['product_name'].combine_first(df['product_name_'])
        df = df.drop(columns=['product_name_'])

    if 'date_to_restock' in df.columns and 'date_to_restock_' in df.columns:
        df['date_to_restock'] = df['date_to_restock'].combine_first(df['date_to_restock_'])
        df = df.drop(columns=['date_to_restock_'])
    
    if 'supplier' in df.columns and 'supplier_' in df.columns:
        df['supplier'] = df['supplier'].combine_first(df['supplier_'])
        df = df.drop(columns=['supplier_'])
    
    df['our_price'] = df['our_price'].replace({'\$': '', ',': ''}, regex=True).astype(float, errors='ignore')

    df['date_to_restock'] = pd.to_datetime(df['date_to_restock'], errors='coerce')

    df = df.drop_duplicates(subset=['product_name', 'date_to_restock', 'supplier'])

    df = df.dropna(subset=['product_name', 'our_price', 'category', 'current_stock', 'supplier'])

    df['current_stock'] = df['current_stock'].replace('out of stock', 0)
    
    df['current_stock'] = pd.to_numeric(df['current_stock'], errors='coerce')

    # Convert all string columns to uppercase
    str_cols = df.select_dtypes(include=['object']).columns
    df[str_cols] = df[str_cols].apply(lambda x: x.str.upper())

    df['restock_threshold'] = df['restock_threshold'].fillna(0).astype(int)

    return df


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
    """
    Calculate the price variation of products in a specific country in local currency with respect to USD.

    Args:
        country_name (str): Name of the country to analyze (e.g., 'Colombia').
        df_products (pd.DataFrame): DataFrame with product details including prices in USD.
        df_target (pd.DataFrame): Data from the API for the target date.
        df_comparation (pd.DataFrame): Data from the API for the comparation date.
    
    Returns:
        dict: Product price variations in local currency.
    
    Exceptions:
        Exception: Error message.
    """
    try:
        # Get the currency symbol for the specified country
        currency_symbol = None
        for code, name in countries.items():
            if name.lower() == country_name.lower():
                currency_symbol = code
                break

        if not currency_symbol:
            raise ValueError(f"Country '{country_name}' is not in the supported list.")

        # Fetch exchange rates for the country
        rate_target = df_target[currency_symbol].values[0]
        rate_comparation = df_comparation[currency_symbol].values[0]

        # Check for missing or invalid rates
        if pd.isna(rate_target) or pd.isna(rate_comparation):
            raise ValueError(f"Exchange rates for {country_name} are missing.")

        # Calculate the local price variations for each product
        product_variations = {}
        for index, row in df_products.iterrows():
            price_usd = float(str(row['our_price']).replace('$', '').strip())
            price_local_target = price_usd * rate_target
            price_local_comparation = price_usd * rate_comparation
            variation = round(price_local_target - price_local_comparation, 2)

            product_variations[row['product_name']] = {
                "price_target_date": round(price_local_target, 2),
                "price_comparation_date": round(price_local_comparation, 2),
                "variation": variation
            }

        # Save the results to a JSON file
        with open(f"./data/product_variation_{country_name.lower()}.json", "w") as json_file:
            json.dump(product_variations, json_file, indent=4)

        return product_variations

    except Exception as e:
        return str(e)

