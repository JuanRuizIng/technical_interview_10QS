import requests
import pandas as pd

def get_products_api():
    """ It returns a list of products from the FastAPI API 
    
    Args:
        Returns:
        list: A list of JSON with products
        
        Exceptions:
        Exception: If the API is not available

        Output:
        pd.DataFrame: A DataFrame with the products
    """
    try:
        request = requests.get("http://localhost:8000/products")
        result = request.json()
        df = pd.DataFrame(result)
        return df
    except Exception as e:
        print(e)
        return "Something went wrong with the API"

def general_cleaning_data(df):
    """ It cleans the all DataFrames 
    
    Args:
        df (pd.DataFrame): A DataFrame with the products
        
    Returns:
        pd.DataFrame: A cleaned DataFrame
    """
    df = df.dropna()
    df = df.drop_duplicates()
    return df