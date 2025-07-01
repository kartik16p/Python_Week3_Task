import pandas as pd

# employees.csv
employees_data = {
    "Employee_ID": ["E001", "E002"],
    "Name": ["Alice", "Bob"],
    "Department": ["Sales", "Sales"],
    "Join_Date": ["2020-01-10", "2019-06-15"],
    "Region": ["North", "South"],
    "Status": ["Active", "Resigned"]
}

employees_df = pd.DataFrame(employees_data)
employees_df.to_csv("employees.csv", index=False)

# sales.csv
sales_data = {
    "Order_ID": ["O1001", "O1002"],
    "Date": ["2023-01-15", "2023-01-20"],
    "Employee_ID": ["E001", "E002"],
    "Product": ["Laptop", "Tablet"],
    "Units_Sold": [5, 3],
    "Unit_Price": [50000, 20000],
    "Discount (%)": [10, 0]
}

sales_df = pd.DataFrame(sales_data)
sales_df.to_csv("sales.csv", index=False)

# targets.csv
targets_data = {
    "Employee_ID": ["E001", "E002"],
    "Month": ["2023-01", "2023-01"],
    "Target_Amount": [200000, 100000]
}

targets_df = pd.DataFrame(targets_data)
targets_df.to_csv("targets.csv", index=False)
