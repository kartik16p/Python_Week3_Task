import numpy as np

data = np.array([
    [101, 20, 50, 1000, 1, 5],
    [102, 15, 30, 450, 1, 10],
    [103, 10, 20, 200, 2, 0],
    [101, 25, 50, 1250, 3, 0],
    [102, 30, 30, 900, 1, 5],
    [104, 40, 60, 2400, 2, 15]
], dtype=float)

# 1. Total Revenue by Region
regions = data[:, 4].astype(int)
revenues = data[:, 3]
print("1. Total Revenue by Region:")
for region in np.unique(regions):
    total_rev = np.sum(revenues[regions == region])
    print(f"   Region {region}: {total_rev}")

# 2. Average Discount Offered
discounts = data[:, 5]
print("2. Average Discount Offered:", np.mean(discounts))

# 3. Product with the Highest Revenue
product_ids = data[:, 0].astype(int)
revenue_per_product = {}
for i in range(len(data)):
    pid = int(product_ids[i])
    revenue_per_product[pid] = revenue_per_product.get(pid, 0) + revenues[i]
max_revenue_product = max(revenue_per_product, key=revenue_per_product.get)
print("3. Product with the Highest Revenue:", max_revenue_product)

# 4. Total Units Sold Across All Products
units_sold = data[:, 1]
print("4. Total Units Sold Across All Products:", np.sum(units_sold))

# 5. Revenue Lost Due to Discounts
unit_price = data[:, 2]
discount_loss = (discounts / 100) * unit_price * units_sold
print("5. Revenue Lost Due to Discounts:", np.sum(discount_loss))

# 6. Products Sold in Region 1
products_region_1 = data[regions == 1][:, 0].astype(int)
print("6. Products Sold in Region 1:", np.unique(products_region_1))

# 7. Correlation Between Units Sold and Revenue
print("7. Correlation Between Units Sold and Revenue:",
      np.corrcoef(units_sold, revenues)[0, 1])

# 8. Total Revenue for Each Product
print("8. Total Revenue for Each Product:")
for pid in np.unique(product_ids):
    total = np.sum(revenues[product_ids == pid])
    print(f"   Product {int(pid)}: {total}")

# 9. Find Products with Discounts Greater Than 10%
products_discount_gt_10 = data[discounts > 10][:, 0].astype(int)
print("9. Products with Discounts Greater Than 10%:", np.unique(products_discount_gt_10))

# 10. Identify Region with Maximum Units Sold
units_by_region = {}
for i in range(len(data)):
    region = int(regions[i])
    units_by_region[region] = units_by_region.get(region, 0) + units_sold[i]
max_region = max(units_by_region, key=units_by_region.get)
print("10. Region with Maximum Units Sold:", max_region)

# 11. Normalize Revenue to a 0-1 Scale
min_rev = np.min(revenues)
max_rev = np.max(revenues)
revenue_normalized = (revenues - min_rev) / (max_rev - min_rev)

print("11. Revenue Normalized (0-1 Scale):")
for i, val in enumerate(revenue_normalized, start=1):
    print(f"   Day {i}: {val:.2f}")


# 12. Average Units Sold Per Product
print("12. Average Units Sold Per Product:")
for pid in np.unique(product_ids):
    avg_units = np.mean(units_sold[product_ids == pid])
    print(f"   Product {int(pid)}: {avg_units}")

# 13. Products with Revenue Greater Than $1000
products_rev_gt_1000 = data[revenues > 1000][:, 0].astype(int)
print("13. Products with Revenue > $1000:", np.unique(products_rev_gt_1000))

# 14. Cumulative Revenue
cumulative_revenue = np.cumsum(revenues)
print("14. Cumulative Revenue:")
print("   ", cumulative_revenue.astype(int))

# 15. Compute Total Revenue After a Hypothetical 20% Price Increase
unit_price_increased = unit_price * 1.2
revenue_after_increase = unit_price_increased * units_sold
print("15. Total Revenue After 20% Price Increase:", np.sum(revenue_after_increase))