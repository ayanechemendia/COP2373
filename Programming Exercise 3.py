"""
Programming Exercise 3
COP 2373 Programming Exercise
Author: Ayan Echemendia-Carranza
"""

from functools import reduce


def get_expenses():
    """
    Prompts the user to enter expense types and amounts.
    Returns a list of dictionaries containing expense data.
    """

    expenses = []

    print("Enter your monthly expenses.")
    print("Type 'done' when finished.\n")

    while True:

        expense_type = input("Enter expense type: ")

        if expense_type.lower() == "done":
            break

        amount = float(input("Enter expense amount: $"))

        expense = {
            "type": expense_type,
            "amount": amount
        }

        expenses.append(expense)

        print()

    return expenses


def calculate_total(expenses):
    """
    Uses reduce to calculate total expense amount.
    Returns total.
    """

    total = reduce(lambda acc, expense: acc + expense["amount"], expenses, 0)

    return total


def find_highest(expenses):
    """
    Uses reduce to find highest expense.
    Returns the highest expense dictionary.
    """

    highest = reduce(
        lambda x, y: x if x["amount"] > y["amount"] else y,
        expenses
    )

    return highest


def find_lowest(expenses):
    """
    Uses reduce to find lowest expense.
    Returns the lowest expense dictionary.
    """

    lowest = reduce(
        lambda x, y: x if x["amount"] < y["amount"] else y,
        expenses
    )

    return lowest


def display_results(expenses):
    """
    Displays total, highest, and lowest expenses.
    """

    if len(expenses) == 0:
        print("No expenses entered.")
        return

    total = calculate_total(expenses)
    highest = find_highest(expenses)
    lowest = find_lowest(expenses)

    print("\n----- Expense Summary -----")
    print(f"Total Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest['type']} - ${highest['amount']:.2f}")
    print(f"Lowest Expense: {lowest['type']} - ${lowest['amount']:.2f}")


def main():
    """
    Main function that runs the program.
    """

    expenses = get_expenses()

    display_results(expenses)


if __name__ == "__main__":
    main()
