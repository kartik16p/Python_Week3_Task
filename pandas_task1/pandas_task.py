import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# --- Task 1: Data Preprocessing ---

employees = pd.read_csv("employees.csv")
sales = pd.read_csv("sales.csv")
targets = pd.read_csv("targets.csv")

sales['Date'] = pd.to_datetime(sales['Date'])
sales['Month'] = sales['Date'].dt.to_period('M').astype(str)
sales['Total_Sale'] = sales['Units_Sold'] * sales['Unit_Price'] * (1 - sales['Discount (%)'] / 100)

print("\nTask 1: Total Sale Calculated")
print(sales[['Employee_ID', 'Product', 'Units_Sold', 'Unit_Price', 'Discount (%)', 'Total_Sale']])

merged = pd.merge(sales, employees, on='Employee_ID', how='left')
final_df = pd.merge(merged, targets, on=['Employee_ID', 'Month'], how='left')

print("\nTask 1: Merged Dataset Preview")
print(final_df.head())

# --- Task 2: Employee Performance Analysis ---

monthly_sales = final_df.groupby(['Employee_ID', 'Month'])['Total_Sale'].sum().reset_index()
monthly_sales.columns = ['Employee_ID', 'Month', 'Actual_Sales']
performance = pd.merge(monthly_sales, targets, on=['Employee_ID', 'Month'], how='left')
performance['Target_Met'] = np.where(performance['Actual_Sales'] >= performance['Target_Amount'], 'Yes', 'No')
performance['Performance_Score'] = (performance['Actual_Sales'] / performance['Target_Amount']) * 100
final_df = pd.merge(final_df, performance[['Employee_ID', 'Month', 'Target_Met', 'Performance_Score']], on=['Employee_ID', 'Month'], how='left')

print("\nTask 2: Employee Performance Summary")
print(performance[['Employee_ID', 'Month', 'Actual_Sales', 'Target_Amount', 'Target_Met', 'Performance_Score']])

# --- Task 3: Regional and Department Insights ---

region_sales = final_df.groupby('Region')['Total_Sale'].sum()
region_percent = (region_sales / region_sales.sum() * 100).round(2)
print("\nTask 3: Region-wise Sales Contribution (%)")
print(region_percent)

status_count = employees.groupby(['Department', 'Status'])['Employee_ID'].count().unstack(fill_value=0)
print("\nTask 3: Department-wise Active vs Resigned Count")
print(status_count)

attrition = employees[employees['Status'] == 'Resigned'].groupby('Department').size()
if not attrition.empty:
    highest_attrition_dept = attrition.idxmax()
    print(f"\nTask 3: Department with Highest Attrition: {highest_attrition_dept}")
else:
    print("\nTask 3: No Resigned Employees in Dataset")

# --- Task 4: Time Series Analysis ---

monthly_trend = final_df.groupby('Month')['Total_Sale'].sum().sort_index()
print("\nTask 4: Monthly Total Sales Trend")
print(monthly_trend)

monthly_rolling = monthly_trend.rolling(window=3, min_periods=1).mean()
pct_change = monthly_trend.pct_change()
anomalies = pct_change[pct_change < -0.20].index.tolist()
print("\nTask 4: Anomaly Months (>20% drop):")
print(anomalies if anomalies else "No anomalies detected")

# --- Task 5: Advanced Reporting ---

pivot_table = final_df.pivot_table(values='Total_Sale', index='Employee_ID', columns='Month', aggfunc='sum', fill_value=0)
print("\nTask 5: Pivot Table - Total Sales per Employee per Month")
print(pivot_table)

product_corr = final_df.groupby('Product')[['Units_Sold', 'Total_Sale']].sum().corr()
sns.heatmap(product_corr, annot=True, cmap="coolwarm")
plt.title("Correlation: Units Sold vs Total Sale")
plt.savefig("heatmap_correlation.png")
plt.close()

performance_summary = performance[['Employee_ID', 'Performance_Score']].drop_duplicates()
performance_summary['Performance_Category'] = pd.cut(
    performance_summary['Performance_Score'],
    bins=[-np.inf, 89.99, 119.99, np.inf],
    labels=['Underperformer', 'Good', 'Top Performer']
)

print("\nTask 5: Employee Performance Categories")
print(performance_summary)

# --- Task 6: Export ---

final_df.to_csv("performance_report.csv", index=False)
performance_summary.to_csv("employee_scores.csv", index=False)

print("\nTask 6: Files Exported Successfully")
print("   - performance_report.csv")
print("   - employee_scores.csv")
print("   - heatmap_correlation.png")
