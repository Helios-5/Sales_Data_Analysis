# 📊 SALES DATA ANALYSIS: Monthly Revenue Trend

import pandas as pd
import matplotlib.pyplot as plt

# 🔹 Step 1: Load the sales dataset
# Make sure 'sample_sales_data.csv' is in the same directory
df = pd.read_csv('sample_sales_data.csv', parse_dates=['Order_Date'])
df.dropna(how='all', inplace=True)  # removes blank lines

# 🔹 Step 2: Create a 'Month' column from the 'Order_Date'
df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)

# 🔹 Step 3: Group data by month and calculate total revenue
monthly_sales = df.groupby('Month')['Revenue'].sum()

# 🔹 Step 4: Plot the monthly revenue trend
plt.figure(figsize=(10, 5))                          # Set plot size
monthly_sales.plot(kind='line', marker='o')          # Line plot with circle markers
plt.title("Monthly Revenue Trend")                   # Title of the chart
plt.xlabel("Month")                                  # X-axis label
plt.ylabel("Revenue")                                # Y-axis label
plt.grid(True)                                       # Add grid for better readability
plt.tight_layout()                                   # Adjust layout to prevent clipping
plt.savefig("monthly_revenue_trend.png")             # Save the plot as an image file
plt.close()                                          # Close the plot to free memory
