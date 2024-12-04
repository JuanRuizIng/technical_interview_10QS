# 10EQS Data Integration Challenge: Report of Products

## Introduction
The appreciation of the U.S. dollar significantly impacts emerging markets, leading to increased import costs and reduced import volumes. A 10% rise in the dollar's value can decrease economic output in these economies by 1.9% within a year, with effects lasting over two years. [FONDO MONETARIO INTERNACIONAL](https://www.imf.org/en/Blogs/Articles/2023/07/19/emerging-market-economies-bear-the-brunt-of-a-stronger-dollar?utm)
This appreciation elevates the local currency prices of imports, especially commodities like oil and food, intensifying inflationary pressures. [ECONOFACT](https://econofact.org/global-repercussions-of-the-strong-dollar?utm) Consequently, countries such as Argentina and Turkey have experienced reduced import volumes due to the prohibitive costs associated with a stronger dollar. Additionally, the increased burden of servicing dollar-denominated debts further strains these economies, leading to decreased purchasing power and a slowdown in economic growth. 

To prevent this, I have created an application integrating external sources to see the market trend in different Latin American countries and review the possible impact on sales of the products taking into account the above context, thus helping to prepare for a decrease in orders or see metrics that can help to see the reason for a decline or increase in sales (depending on whether the dollar did more or less strong in Latin American countries).

## Data quality issues
1. The PDF data could not be accessed in its entirety, so that sometimes the columns were 'split' and not all the columns were visible, so at least the last columns had to be given an approximate name taking into account logic.

![image](https://github.com/user-attachments/assets/c136e965-acb6-4db2-9f0d-fa37f5321535)

2. There were not too many APIs that dealt with the products, so some that were candidates after I registered only gave you the food components of these products.
3. There was data that was effectively cleaned and did not respect the guidelines, such as 'out of the stock' in mostly numeric columns, which was transformed into 0, and dates, in yyyy/mm/dd format and not yyyy-mm-dd.

## Cleaned data summary
Our code is designed to help your business by consolidating and cleaning product data from different sources to provide accurate and actionable insights. Here's an overview of how the data cleaning process works:

1.  **Data Retrieval**:
    
    -   We start by fetching product data from two sources:
        -   An API that provides the latest currency information.
        -   A CSV file containing additional product data.
2.  **Standardizing Column Names**:
    
    -   We ensure that all column names are consistent by converting them to lowercase, removing extra spaces, and replacing spaces with underscores. This makes it easier to work with the data uniformly.
    -   
3.  **Cleaning Price Information**:
    
    -   We clean the `our_price` column by removing any currency symbols like `$` and commas.
    -   We then convert these prices into numerical format so that they can be used for calculations and analysis.
    
4.  **Handling Dates**:
    
    -   The `date_to_restock` column is converted into a standard date format. This ensures that we can accurately track and compare restocking dates.

5.  **Dealing with Missing or Incomplete Data**:
    
    -   Rows that are missing critical information (like product name, price, category, current stock, or supplier) are removed to maintain data integrity.
    -   For the `restock_threshold` column, any missing values are filled with zero to indicate no threshold specified.
    
8.  **Standardizing Stock Information**:
    
    -   Any products listed as "out of stock" in the `current_stock` column are replaced with a numerical zero.
    -   We convert the `current_stock` values into numbers to facilitate inventory calculations.

9.  **Uniform Text Formatting**:
    
    -   All text columns are converted to uppercase. This standardization helps in consistent data matching and reduces case-sensitivity issues.
    
10.  **Final Data Consolidation**:
    
    -   After cleaning both datasets, we combine them into a single, comprehensive dataset.
    -   This consolidated data is then used for generating valuable insights, such as identifying the variation of currency to respect USD.


**Benefits to Your Business**:

- Accurate Pricing Analysis: By integrating exchange rate data with product prices, we provide a clear view of how local costs fluctuate with currency changes. This helps identify overpriced or underpriced items in different markets.

- Efficient Inventory Management: The code highlights low-stock products and identifies restocking priorities, ensuring you address inventory gaps promptly and maintain steady supply chains.

- Market-Informed Decision Making: Real-time currency variations and product-specific price trends allow for strategic pricing adjustments, reducing the risk of missed sales and improving competitiveness.

This approach delivers actionable insights by combining clean, standardized internal data with external market trends, optimizing your pricing and stock management to boost overall performance.


## Business Insights

### **1. Price Variation by Country**

#### Insight:
Based on the comparison of exchange rates between target and comparison dates:
- Significant currency devaluation was observed in **Argentina (661.70)**, **Colombia (477.61)**, and **Paraguay (328.53)**, leading to higher local costs for imported products.
- For **Chile**, the smaller variation (94.49) suggests less impact on pricing.
- **Venezuela** saw minimal fluctuation (12.67), indicating relative stability.

#### Recommendation:
- **Adapt Pricing**: Adjust product pricing in countries with significant currency devaluation to maintain competitiveness without eroding margins.
- **Monitor Exchange Rates**: Continuously track rate fluctuations to anticipate cost changes and plan inventory replenishment effectively.

---

### **2. Product Price Variation in Colombia**

#### Insight:
The price of imported products in Colombia increased due to currency devaluation. Key products affected include:
- **Matcha Green Tea Powder**: The largest increase (**9,547.47 COP**).
- **Espresso Beans**: Increased by **8,114.63 COP**.
- **Decaf Coffee Beans**: Increased by **7,637.02 COP**.

#### Recommendation:
- **Targeted Discounts**: Offer strategic promotions on highly affected products to sustain sales volumes.
- **Local Sourcing**: Consider alternatives from local suppliers to reduce dependency on imports.

---

### **3. High Stock Costs**

#### Insight:
Products with significant price variations might lead to increased holding costs for inventory. Example:
- **Organic Coffee Beans**: Variation of **7,159.40 COP**, increasing cost implications for large stock levels.

#### Recommendation:
- **Stock Optimization**: Reduce inventory for products with high price sensitivity to avoid overstocking during unfavorable currency rates.

---

### **4. Market Opportunities**

#### Insight:
Stable or appreciating currencies, such as **Peru** and **Costa Rica**, could present opportunities for expanding market share with competitive pricing.

#### Recommendation:
- **Market Expansion**: Focus on these markets to boost sales and profitability during favorable exchange conditions.

---

### **5. Focus on Top Variations**

#### Insight:
The top five countries with the highest variation (e.g., Argentina, Colombia) could represent high-risk markets for import-dependent businesses.

#### Recommendation:
- **Risk Mitigation**: Diversify sourcing to hedge against currency risks and explore hedging financial instruments for these markets.

---

### **Next Steps**

1. **Currency Rate Monitoring**: Implement automated monitoring for real-time alerts on significant currency variations.
2. **Dynamic Pricing Models**: Integrate dynamic pricing strategies that respond to currency fluctuations.
3. **Product-Specific Strategy**: Develop tailored pricing and stocking strategies for high-variation products like **Matcha Green Tea** and **Espresso Beans**.

### Data References:
- **Top Variations**: `variation_price_top.json`
- **Country-Wide Changes**: `variation_price.json`
- **Product-Specific Changes**: `product_variation_colombia.json`
