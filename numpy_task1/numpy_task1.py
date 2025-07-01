import numpy as np

data = np.array([
    ['2025-01-01', 22, 65, 15, 2.5],
    ['2025-01-02', 25, 70, 10, 0.0],
    ['2025-01-03', 20, 60, 20, 5.0],
    ['2025-01-04', 18, 55, 25, 12.0],
    ['2025-01-05', 24, 75, 5, 0.0]
], dtype=object)

# 1. Average Temperature
temperature = data[:, 1].astype(float)
print("1. Average Temperature:", np.mean(temperature))

# 2. Maximum Humidity
humidity = data[:, 2].astype(float)
print("2. Maximum Humidity:", np.max(humidity))

# 3. Day with Maximum Wind Speed
wind_speed = data[:, 3].astype(float)
max_wind_index = np.argmax(wind_speed)
print("3. Day with Maximum Wind Speed:", data[max_wind_index, 0])

# 4. Total Rainfall
rainfall = data[:, 4].astype(float)
print("4. Total Rainfall:", np.sum(rainfall))

# 5. Days with Temperature Above 22°C
days_above_22 = data[temperature > 22]
print("5. Days with Temperature Above 22°C:", days_above_22[:, 0])

# 6. Average Wind Speed on Humid Days (Humidity > 60%)
humid_days = humidity > 60
avg_wind_humid = np.mean(wind_speed[humid_days])
print("6. Average Wind Speed on Humid Days:", avg_wind_humid)

# 7. Day with Highest Rainfall
max_rain_index = np.argmax(rainfall)
print("7. Day with Highest Rainfall:", data[max_rain_index, 0])

# 8. Variance in Temperature
print("8. Variance in Temperature:", np.var(temperature))

# 9. Standard Deviation of Humidity
print("9. Standard Deviation of Humidity:", np.std(humidity))

# 10. Filter Data for Days with Wind Speed > 10 km/h
filtered_data_wind = data[wind_speed > 10]
print("10. Days with Wind Speed > 10 km/h:\n", filtered_data_wind)

# 11. Rainfall Normalized to a 0-1 Range
min_rain = np.min(rainfall)
max_rain = np.max(rainfall)
rain_normalized = (rainfall - min_rain) / (max_rain - min_rain)
print("11. Rainfall Normalized (0-1 Range):")
for i, val in enumerate(rain_normalized):
    print(f"  Day {i+1}: {val:.2f}")


# 12. Correlation Between Temperature and Humidity
correlation = np.corrcoef(temperature, humidity)[0, 1]
print("12. Correlation Between Temperature and Humidity:", correlation)

# 13. Cumulative Rainfall
cumulative_rain = np.cumsum(rainfall)
print("13. Cumulative Rainfall:", cumulative_rain)

# 14. Identify Calm Days (Wind Speed < 10 km/h)
calm_days = data[wind_speed < 10]
print("14. Calm Days (Wind Speed < 10 km/h):", calm_days[:, 0])

# 15. Days Without Rainfall
dry_days = data[rainfall == 0.0]
print("15. Days Without Rainfall:", dry_days[:, 0])