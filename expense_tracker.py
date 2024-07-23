import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load expenses
def load_expenses(file_path):
    return pd.read_csv(file_path)

# Add a new expense
def add_expense(file_path, date, category, amount, description):
    new_expense = {'Date': date, 'Category': category, 'Amount': amount, 'Description': description}
    df = pd.read_csv(file_path)
    df = df.append(new_expense, ignore_index=True)
    df.to_csv(file_path, index=False)
    print("Expense added successfully.")

# View all expenses
def view_expenses(df):
    print(df)

# Analyze expenses by category
def analyze_expenses(df):
    summary = df.groupby('Category')['Amount'].sum()
    print(summary)
    summary.plot(kind='bar')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.title('Expenses by Category')
    plt.show()

def main():
    file_path = 'expenses.csv'
    df = load_expenses(file_path)

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_expense(file_path, date, category, amount, description)
            df = load_expenses(file_path)  # Reload expenses after adding new one
        elif choice == '2':
            view_expenses(df)
        elif choice == '3':
            analyze_expenses(df)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
