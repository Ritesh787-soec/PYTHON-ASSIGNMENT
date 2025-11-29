def categorize_spending(percent):
    if percent < 30:
        return "LOW", "Good control!"
    elif percent < 70:
        return "MODERATE", "Be careful!"
    else:
        return "HIGH", "Financial Risk!"

try:
    # Input income
    income = float(input("Enter your monthly income: "))

    # Input expenses
    expenses = []
    n = int(input("How many expense entries? "))

    for i in range(n):
        amount = float(input(f"Enter expense {i+1}: "))
        expenses.append(amount)

    total_expense = sum(expenses)
    savings = income - total_expense

    percent_spent = (total_expense / income) * 100

    category, message = categorize_spending(percent_spent)

    print("\n------ FINANCE REPORT ------")
    print(f"Total Income     : ₹{income}")
    print(f"Total Expenses   : ₹{total_expense}")
    print(f"Savings          : ₹{savings}")
    print(f"Percent Spent    : {percent_spent:.2f}%")
    print(f"Spending Level   : {category}")
    print(f"Message          : {message}")
    print("----------------------------")

except ValueError:
    print("ERROR: Please enter numeric values only!")

except ZeroDivisionError:
    print("ERROR: Income cannot be zero!")

except Exception as e:
    print("Unexpected Error Occurred:", e)
