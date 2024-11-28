from utils import contac_df, low_stock_products, high_priority_restocking, generate_recommendations

low_stock = low_stock_products(5)

restocking = high_priority_restocking()

recommendations = generate_recommendations()

print('Low stock products:', low_stock)

print('Restocking:', restocking)

print('Recommendations:', recommendations)