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


def contac_df():
    """ It concatenates two DataFrames 
    
    Args:
        df1 (pd.DataFrame): A DataFrame with the products
        df2 (pd.DataFrame): A DataFrame with the products
        
    Returns:
        pd.DataFrame: A concatenated DataFrame
    """
    df1 = get_products_api()
    df1 = general_cleaning_data(df1)
    df2 = pd.read_csv("./data/products.csv")
    df2 = general_cleaning_data(df2)
    result = pd.concat([df1, df2])
    return result


def low_stock_products(threshold):
    """ It returns the products with low stock
    
    Args:
        threshold (int): The threshold to consider a product with low stock
        
    Returns:
        pd.DataFrame: A DataFrame with the products with low stock
    """
    df = contac_df()
    low_stock = df[df['current_stock'] <= threshold]
    return low_stock

def high_priority_restocking():
    """ It returns the products with high priority to restock

    Args:
        None
    
    Returns:
        pd.DataFrame: A DataFrame with the products with high priority to restock
    """
    df = contac_df()
    restock_needed = df[(df['current_stock'] <= df['restock_threshold'])]
    return restock_needed

def detect_price_outliers():
    """ It detects the outliers in a column for offers

    Args:
        None
    
    Returns:
        pd.DataFrame: A DataFrame with the outliers
    """

    column = 'our_price'
    df = contac_df()

    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

def generate_recommendations():
    """ It generates recommendations based on the DataFrame
    
    Args:
        None
        
    Returns:
        dict: A dictionary with the recommendations
    """
    df = contac_df()

    price_outliers = detect_price_outliers()
    low_stock = low_stock_products(10)
    high_restock = high_priority_restocking()

    recommendations = {
        "price_outliers": price_outliers,
        "low_stock_products": low_stock,
        "high_priority_restocking": high_restock
    }
    return recommendations

#result = get_products_api()
#result = general_cleaning_data(result)
#df = contac_df()
#print(df)