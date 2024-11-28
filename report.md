# # 10EQS Data Integration Challenge: Report of Products

## Data quality issues
1. The PDF data could not be accessed in its entirety, so that sometimes the columns were 'split' and not all the columns were visible, so at least the last columns had to be given an approximate name taking into account logic.

(I edit this camp for the image but in the markdown editor of github)

2. There were not too many APIs that dealt with the products, so some that were candidates after I registered only gave you the food components of these products.
3. There was data that was effectively cleaned and did not respect the guidelines, such as 'out of the stock' in mostly numeric columns, which was transformed into 0, and dates, in yyyy/mm/dd format and not yyyy-mm-dd.

## Cleaned data summary
Our code is designed to help your business by consolidating and cleaning product data from different sources to provide accurate and actionable insights. Here's an overview of how the data cleaning process works:

1.  **Data Retrieval**:
    
    -   We start by fetching product data from two sources:
        -   An internal API (`http://localhost:8000/products`) that provides the latest product information.
        -   A CSV file containing additional product data.
2.  **Standardizing Column Names**:
    
    -   We ensure that all column names are consistent by converting them to lowercase, removing extra spaces, and replacing spaces with underscores. This makes it easier to work with the data uniformly.
3.  **Merging Duplicate Columns**:
    
    -   Sometimes, the same information might be labeled differently in different data sources (e.g., `product_name` and `product_name_`). We combine these columns to avoid duplication and ensure that all data for a particular field is in one place.
4.  **Cleaning Price Information**:
    
    -   We clean the `our_price` column by removing any currency symbols like `$` and commas.
    -   We then convert these prices into numerical format so that they can be used for calculations and analysis.
5.  **Handling Dates**:
    
    -   The `date_to_restock` column is converted into a standard date format. This ensures that we can accurately track and compare restocking dates.
6.  **Removing Duplicate Entries**:
    
    -   We eliminate any duplicate product entries based on `product_name`, `date_to_restock`, and `supplier`. This prevents redundant data from skewing our analysis.
7.  **Dealing with Missing or Incomplete Data**:
    
    -   Rows that are missing critical information (like product name, price, category, current stock, or supplier) are removed to maintain data integrity.
    -   For the `restock_threshold` column, any missing values are filled with zero to indicate no threshold specified.
8.  **Standardizing Stock Information**:
    
    -   Any products listed as "out of stock" in the `current_stock` column are replaced with a numerical zero.
    -   We convert the `current_stock` values into numbers to facilitate inventory calculations.
9.  **Uniform Text Formatting**:
    
    -   All text columns are converted to uppercase. This standardization helps in consistent data matching and reduces case-sensitivity issues.
10.  **Final Data Consolidation**:
    
    -   After cleaning both datasets, we combine them into a single, comprehensive dataset.
    -   This consolidated data is then used for generating valuable insights, such as identifying low-stock products, detecting price outliers, and prioritizing restocking.

**Benefits to Your Business**:

-   **Accurate Pricing Analysis**: By cleaning and standardizing price data, we can more accurately identify products that are overpriced or underpriced compared to market trends.
-   **Efficient Inventory Management**: Cleaning stock data allows us to pinpoint products that are low in stock or need urgent restocking, helping you avoid stockouts and lost sales.
-   **Consistent Data for Decision Making**: Standardized and clean data ensures that all subsequent analyses and reports are based on reliable information, leading to better-informed business decisions.

By ensuring the data is clean and consistent, we provide a solid foundation for generating actionable insights that can help optimize pricing strategies, improve inventory management, and ultimately enhance overall business performance.

## Business insights

### **1. Low Stock Products**

#### Insight:

Several products have dangerously low stock levels, which could lead to missed sales opportunities if not addressed promptly. Key products identified include:

-   **Mint Tea (25 bags)**: Stock level is **0**, below the restocking threshold of **12**.
-   **Yerba Mate Loose Leaf (1lb)**: Stock is consistently low across multiple dates.

#### Recommendation:

-   **Immediate Restocking**: Prioritize restocking these products to avoid stockouts, especially those with strong sales potential like Mint Tea and Yerba Mate.
-   **Demand Forecasting**: Use historical sales data to predict future demand and optimize inventory management.

----------

### **2. High-Priority Restocking**

#### Insight:

Products such as **Chamomile Tea (30 bags)** and **Matcha Green Tea Powder (4oz)** have current stock levels close to or below their restocking thresholds. Some, like Matcha Green Tea Powder, have a significantly high restocking threshold (**999 units**), indicating potential errors or overestimation in threshold settings.

#### Recommendation:

-   **Validate Thresholds**: Review and adjust restocking thresholds to ensure they align with actual sales trends and storage capacity.
-   **Scheduled Restocking**: Implement a restocking schedule for products nearing their thresholds, focusing on high-demand items like Chamomile Tea.

----------

### **3. Price Outliers**

#### Insight:

The product **Rooibos Tea (40 sachets)** has a significantly higher price (**999**) than others in the same category, which may deter customers or indicate data entry errors. It should be remembered that **999** is entered as **999** when an entry is unknown.

#### Recommendation:

-   **Correct Pricing Errors**: Verify and correct the price of Rooibos Tea to align with market standards.
-   **Competitive Pricing Analysis**: Regularly review pricing strategies to ensure competitiveness and customer appeal.

----------

### **4. Inventory Trends**

#### Insight:

-   Products like **Mint Tea** and **Chamomile Tea** repeatedly appear in low-stock or restocking lists across different years, indicating consistent high demand or poor inventory planning.

#### Recommendation:

-   **Stock Buffering**: Maintain higher buffer stock for products with recurring low-stock issues.
-   **Promotional Insights**: Analyze sales trends to determine if promotions or seasonal demand spikes are causing these shortages and adjust restocking plans accordingly.

----------

### **5. Supplier Insights**

#### Insight:

The data reveals dependency on certain suppliers, such as **Bean Brothers** and **Tea Time Imports**, for high-demand products.

#### Recommendation:

-   **Diversify Suppliers**: Build relationships with alternative suppliers to mitigate risks of supply chain disruptions.
-   **Supplier Performance Metrics**: Track supplier reliability to ensure timely deliveries for high-priority products.

----------

### **6. Actionable Data Cleansing and Validation**

#### Insight:

Issues like "out of stock" values and inconsistent restocking thresholds indicate potential lapses in data entry and management.

#### Recommendation:

-   **Automate Data Validation**: Implement automated systems to catch errors like unrealistic prices or missing stock values.
-   **Staff Training**: Train staff on accurate data entry practices to minimize discrepancies.

----------

### **Next Steps**

1.  **Develop a dashboard**: We must build a real-time inventory dashboard to monitor stock levels, prices and replenishment schedules. This can be done with tools such as Apache Kafka.
2.  **Analyze sales trends**: Use sales data to correlate stock levels with revenue and identify the most profitable products.
3.  **Streamline replenishment**: Collaborate with suppliers to ensure just-in-time replenishment of high-demand products.