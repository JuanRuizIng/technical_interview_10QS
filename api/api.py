from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/products")
async def get_products_api():
    """ It returns a list of products from the OpenFoodFacts API 
    
    Args:
        
        Returns:
        list: A list of products
        
        Exceptions:
        Exception: If the search_term is not valid
    """
    try:
        data = pd.read_json("./data/products_simulation.json")
        data = data.fillna(999)
        return data.to_dict(orient="records")
    except Exception as e:
        print(e)
        return "Something went wrong with the API"