import csv
import matplotlib.pyplot as plt
month_number = []
total_profit = []
products = {
    'facecream': [],
    'facewash': [],
    'toothpaste': [],
    'bathingsoap': [],
    'shampoo': [],
    'moisturizer': []
}
total_sales = {
    'facecream': 0,
    'facewash': 0,
    'toothpaste': 0,
    'bathingsoap': 0,
    'shampoo': 0,
    'moisturizer': 0
}
csv_file = "abc.csv" 
with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        month_number.append(int(row["month_number"]))
        total_profit.append(float(row["total_profit"]))
        for product, value in products.items():
            value.append(int(row[product]))
            total_sales[product] += int(row[product])

total_profit_all_months = sum(total_profit)
plt.figure(figsize=(12, 6))
plt.plot(month_number, total_profit, marker='o', linestyle='--', color='red', linewidth=3, label='Total Profit')
plt.title("Monthly Total Profit")
plt.xlabel("Month Number")
plt.ylabel("Sold Units Number")
plt.grid(True)
plt.legend(loc='lower right')
plt.figure(figsize=(12, 6))
for product, values in products.items():
    plt.plot(month_number, values, label=product)
plt.title("Units Sold Per Month for Each Product")
plt.xlabel("Month Number")
plt.ylabel("Units Sold")
plt.grid(True)
plt.legend()
plt.figure(figsize=(8, 8))
product_names = list(total_sales.keys())
total_sales_values = list(total_sales.values())
plt.pie(total_sales_values, labels=product_names, autopct='%1.1f%%', startangle=140)
plt.title("Total Sales Data for Last Year by Product")
plt.axis('equal')
print("Total profit for all months:", total_profit_all_months)
plt.show()