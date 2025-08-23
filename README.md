# 📊 Sales Data Analysis & Interactive Dashboard 
💡 Overview

In this project, I analyzed sales datasets and extracted key insights , and created various types of data visualizations,  such as - time series charts, bar charts  , scatter Chart etc. Also created an interactive dashboard that allows users to filter and visualize data in real-time . 

🎯 Objectives 

Identify sales trends over time, including seasonal patterns and year-month analysis
Analyze performance by region, category, and segment
Find and analyze top-selling products for better inventory and marketing strategy
🔍 Dataset Source and Structure

Source of Dataset

📦 The dataset has been taken from Kaggle.

🔗 Dataset Link

https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting
---
📊 Structure of Dataset

This dataset contains 9800 rows and 18 columns. Each column provides different types of information about sales transactions, customers, products, and shipping details.

1. Row ID - Unique number for each record.

2. Order ID - Each order has a different ID.

3. Order Date - Date Ordered.

4. Ship Date - Order shipment date.

5. Ship Mode - Shipping method (e.g., Standard, Express).

6. Customer ID - Unique ID for each customer.

7. Customer Name - Name of the customer.

8. Segment - Customer group or segment (e.g., Consumer, Corporate).

9. Country - Name of the country.

10. City - Name of the city.

11. State - Name of the state or province.

12. Postal Code - Postal or ZIP code.

13. Region - Region or division (e.g., East, West).

13. Product ID - Unique ID for each product.

14. Category - Main product category (e.g., Furniture, Technology).

15. Sub-Category - Sub-category of the product (e.g., Chairs, Phones).

16. Product Name - Name of the product.

17. Sales - Amount of sales in currency.




🧹 Data Cleaning & Preprocessing

One of the most important steps in a successful data analysis project is data cleaning and preprocessing. Most data never arrives in a perfectly organized state. Datasets contain errors, missing values, duplicates, and data in incorrect formats.
The cleaning and pre-processing performed in this project is explained step by step below:

1️⃣ ❓ Missing Values Handling

Missing (null) values in a dataset can cause 
problems during analysis. Missing values need to be managed.

🔎 Step 1: Finding Missing Values
Code : df.isnull().sum()
There are 11 missing values in the Postal Code column.

✍️ Step 2: Fill Missing values 
Missing postal code values have been filled based on the corresponding city


check "Burlington" city Postal Code 


 "Burlington" city and "Vermont" State Postal Code is missing


"Burlington" city and "Vermont" State and "East" Region Postal Code is-054080


 now fill missin postal code with  "054080" and


Filled null values are filled as string type. Now we need to convert the values from string type to float

2️⃣  🗓️ Date Formatting

📝 The "Order Date" column has been converted into a separate element for easier analysis and visualization.
📊 Added three new columns:

Year – Extracted the year from the order date

Month – Extracted the month from the order date

YearMonth – Combined year and month for time-series analysis

3️⃣ 🍂 Seasonal Analysis Column

📝 Created a new column from the "Month" to categorize each order into seasons (Spring, Summer, Autumn(Fall) , Winter) .
we haven't any seasonal columns , so i will  Create a new column 'Season' based on the 'Month' column


Using a 'season' function to assign seasons


December, January, February - Winter


March, April, May - Spring


June, July, August -Summer


September, October, November -Autumn (Fall)

📈 Analysis & Visualization

Identify How Much Dataset Have Numerical and categorical columns

 Insight and Observation

 Data set Have 4 numerical features - 'Unnamed: 0', 'Row ID', 'Postal Code', 'Sales'
Data set Have 15 categorical features - 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State', 'Region', 'Product ID', 'Category', 'Sub-Category', 'Product Name'
1. Customer Lifetime Value (CLV) — Total customer spend?  (Analysis)

    Top 5 Coustomer Spend (Visualization)

2. Total Sales  (Analysis)

3. Average Sales per Order  (Analysis)

4. Highest and lowest selling products  (Analysis)

    Top 5 Highest Selling Products  (Visualization)

    Top 5 Lowest Selling Products  (Visualization)

5. Top-selling categories and sub-categories  (Analysis)

    Top-3 selling categories  (Visualization)

    Top-5 selling Sub-Categories  (Visualization)

 6. Which products sell best in which region?  (Analysis)


7. Sales comparison by customer segment  (Analysis)

    Sales comparison by customer segment showing by Pie Chart  (Visualization)

 8. Sales trends over time (month)  (Analysis)

     which Year-Month Have Best Sales (Time Series Analysis)  (Visualization)

9. Sales trends over time (Year)  (Analysis)

     Which Year Have Best Sales (Time Series Analysis)  (Visualization)

 10. Which products sell the most at what time (seasonal Sales) ?  (Analysis)

       Best Selling Products by Season  (Visualization)

11. Category and region-wise comparative analysis  (Analysis)

      Category and Region-wise Comparative Analysis  (Visualization)

12. Total Coustomers  (Analysis)


13.How many customers are repeat buyers?  (Analysis)

14. top 5 repeat coustomer  (Analysis)

     Top 5 Repeat Customers showing by bar chart  (Visualization)



 📈 Interactive Dashboard 
 
💡Overview
Created an interactive sales dashboard to analyze customer and product performance. Users can filter data by Oder Date,  Region, State, City  and visualize sales trends etc.

Key Features ✨

📌 🗓 Date Range Filter : Ability to select order date data for a specific period.

📌 🌍 Region, State, City Filter : Location-based data filte

📌Sales Growth Card: Shows the increase or decrease in sales for the current month compared to the previous month.

📌  📈 Category & Ship Mode Analysis By Sales

📌 Sales Trends (Monthly, Yearly, Seasonal)

📌 Interactive Charts: Line, Bar, Pie, Choropleth

📌 Downloadable Reports

📌📥 CSV Download: Ability to download data for each chart and table.

📌 Summary Table: Summary of important sales information.

📌 Filter Data Download

🛠 Tools & Technologies

🐍 Python — Data Processing & Analysis

🎨 Streamlit — Interactive dashboard

📑 Pandas — Data Handling

📊 Plotly , Scaborn , Matplotlib — Data Visualization

📄 CSV — Export & Download Feature


Outcome :

📈 Helped visualize sales trends, identify high-performing products, and understand customer behavior to support business decisions.

Project Objectives:

This analysis and dashboard will help businesses make quick decisions about sales trends, high-selling product categories, and geographically based sales.
