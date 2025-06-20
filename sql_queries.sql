-- Monthly Revenue Trend
SELECT DATE_FORMAT(Order_Date, '%Y-%m') AS Month, SUM(Revenue) AS Total_Revenue
FROM sales_data
GROUP BY Month
ORDER BY Month;

-- Revenue by Category
SELECT Category, SUM(Revenue) AS Category_Revenue
FROM sales_data
GROUP BY Category
ORDER BY Category_Revenue DESC;

-- Top Products by Revenue
SELECT Product_ID, SUM(Revenue) AS Product_Revenue
FROM sales_data
GROUP BY Product_ID
ORDER BY Product_Revenue DESC
LIMIT 10;

-- Region-wise Sales
SELECT Region, SUM(Revenue) AS Region_Revenue
FROM sales_data
GROUP BY Region
ORDER BY Region_Revenue DESC;
