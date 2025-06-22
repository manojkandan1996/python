import json
from datetime import datetime
import os

DATA_FILE = 'budget.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def add_expense():
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    amount = float(input("Amount: ₹"))
    description = input("Description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    data = load_data()
    data.append(expense)
    save_data(data)
    print("✅ Expense added!")

def view_summary():
    data = load_data()
    total = 0
    summary = {}

    for item in data:
        total += item["amount"]
        cat = item["category"]
        summary[cat] = summary.get(cat, 0) + item["amount"]

    print("\n====== Monthly Summary ======")
    print(f"Total Spent: ₹{total:.2f}")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt:.2f}")
    print("=============================\n")

# Main Interface
while True:
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Exit")

    choice = input("Choose an option: ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_summary()
    elif choice == '3':
        break
    else:
        print("Invalid option. Try again.")