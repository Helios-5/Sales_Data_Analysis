import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sample_sales_data.csv', parse_dates=['Order_Date'])
df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)

monthly_sales = df.groupby('Month')['Revenue'].sum()
monthly_sales.plot(kind='line', marker='o', figsize=(10,5))
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_revenue_trend.png")
plt.close()

# SALES DATA ANALYSIS