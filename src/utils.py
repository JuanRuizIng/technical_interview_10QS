#API DOCUMENTATION: https://openfoodfacts.github.io/openfoodfacts-server/api/
# or, in my case: https://github.com/openfoodfacts/openfoodfacts-python

import openfoodfacts

def get_products_api(search_term):
    """ It returns a list of products from the OpenFoodFacts API 
    
    Args:
        search_term (str): The term to search for products
        
        Returns:
        list: A list of products
        
        Exceptions:
        Exception: If the search_term is not valid
    """
    try:
        api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0")
        result = api.product.text_search(search_term)
        return result
    except Exception as e:
        print(e)
        return "Something went wrong with the API"