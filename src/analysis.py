from utils import get_data_comparation, get_data_target, variation_price, variation_price_top, product_variation_for_country
import pandas as pd

target_date = "2024-12-01" # Date format: YYYY-MM-DD
comparation_date = "2024-11-30" # Date format: YYYY-MM-DD

data_target = get_data_target(target_date)
data_comparation = get_data_comparation(comparation_date)


df_products = pd.read_csv("./data/products.csv")
df_target = pd.DataFrame(data_target["rates"], index=[0])
df_comparation = pd.DataFrame(data_comparation["rates"], index=[0])


variation_price(df_target, df_comparation)
variation_price_top(df_target, df_comparation)

#product_variation_for_country("Colombia", df_products, df_target, df_comparation)