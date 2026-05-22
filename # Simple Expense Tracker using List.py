# Simple Expense Tracker using List

expenses = []

# Function to add expense
def add_expense():
    date = input("Enter Date: ")
    item = input("Enter Expense Name: ")
    amount = float(input("Enter Amount: "))

    expense = {
        "date": date,
        "item": item,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense Added Successfully!\n")

# Function to show expenses
def show_expenses():
    if len(expenses) == 0:
        print("No Expenses Found.\n")
        return

    print("\n----- Expense List -----")
    
    for i in range(len(expenses)):
        print("Date :", expenses[i]["date"])
        print("Item :", expenses[i]["item"])
        print("Amount : ₹", expenses[i]["amount"])
        print("------------------------")

# Function to calculate total expense
def total_expense():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("\nTotal Expense = ₹", total)
    print()

# Main Program
while True:
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice\n")