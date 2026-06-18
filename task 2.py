import csv

def add_expense():
    description = input("Enter Expense Description: ")
    amount = float(input("Enter Amount: ₹"))

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([description, amount])

    print("Expense Added Successfully!")

def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            print("\n----- All Expenses -----")
            for row in reader:
                print(f"Item: {row[0]} | Amount: ₹{row[1]}")

    except FileNotFoundError:
        print("No Expenses Found!")

def total_expenses():
    total = 0

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                total += float(row[1])

        print(f"\nTotal Expenses: ₹{total}")

    except FileNotFoundError:
        print("No Expenses Found!")

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = input("Enter Your Choice (1-4): ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        print("Thank You for Using Expense Tracker!")
        break

    else:
        print("Invalid Choice! Please Try Again.")