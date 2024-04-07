items = [
    {'Date': '2024-01-01', 'Description': 'Walmart', 'Amount (USD)': 35.20, 'Category': 'Groceries'},
    {'Date': '2024-01-02', 'Description': 'Shell Gas Station', 'Amount (USD)': 45.00, 'Category': 'Transport'},
    {'Date': '2024-01-03', 'Description': 'Netflix', 'Amount (USD)': 15.99, 'Category': 'Entertainment'},
    {'Date': '2024-01-04', 'Description': 'Starbucks', 'Amount (USD)': 4.50, 'Category': 'Eating Out'},
    {'Date': '2024-01-05', 'Description': 'Verizon Wireless', 'Amount (USD)': 60.00, 'Category': 'Utilities'},
    {'Date': '2024-01-06', 'Description': 'Target', 'Amount (USD)': 85.00, 'Category': 'Shopping'},
    {'Date': '2024-01-07', 'Description': 'Whole Foods', 'Amount (USD)': 70.30, 'Category': 'Groceries'},
    {'Date': '2024-01-08', 'Description': 'AMC Theatres', 'Amount (USD)': 25.00, 'Category': 'Entertainment'},
    {'Date': '2024-01-09', 'Description': 'Spotify', 'Amount (USD)': 9.99, 'Category': 'Entertainment'},
    {'Date': '2024-01-10', 'Description': 'Chick-fil-A', 'Amount (USD)': 18.40, 'Category': 'Eating Out'},
    {'Date': '2024-01-11', 'Description': 'ExxonMobil', 'Amount (USD)': 50.00, 'Category': 'Transport'},
]

# Sum the data by 'Category'
category_totals = {}
for item in items:
    category = item['Category']
    if category not in category_totals:
        category_totals[category] = 0
    category_totals[category] += item['Amount (USD)']

# Print the results
for category, total in category_totals.items():
    print(f'{category}: ${total:.2f}')