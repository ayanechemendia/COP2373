# ============================================
# BankAcct Class Definition
# ============================================

class BankAcct:
    """
    A class to represent a bank account.
    """

    def __init__(self, name, account_number, amount, interest_rate):
        """
        Initialize account with name, account number, balance, and interest rate.
        """
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate


    # ============================================
    # Deposit Method
    # ============================================

    def deposit(self, value):
        """
        Add money to the account.
        """
        if value > 0:
            self.amount += value
        else:
            print("Deposit amount must be positive.")


    # ============================================
    # Withdraw Method
    # ============================================

    def withdraw(self, value):
        """
        Remove money from the account.
        """
        if value > 0 and value <= self.amount:
            self.amount -= value
        else:
            print("Invalid withdrawal amount.")


    # ============================================
    # Adjust Interest Rate
    # ============================================

    def adjust_interest_rate(self, new_rate):
        """
        Change the interest rate.
        """
        if new_rate >= 0:
            self.interest_rate = new_rate
        else:
            print("Interest rate must be non-negative.")


    # ============================================
    # Get Balance
    # ============================================

    def get_balance(self):
        """
        Return the current balance.
        """
        return self.amount


    # ============================================
    # Calculate Interest
    # ============================================

    def calculate_interest(self, days):
        """
        Calculate interest based on number of days.
        Formula: interest = balance * rate * (days / 365)
        """
        interest = self.amount * self.interest_rate * (days / 365)
        return interest


    # ============================================
    # String Method
    # ============================================

    def __str__(self):
        """
        Display account information.
        """
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate:.2%}")


# ============================================
# Test Function
# ============================================

def test_bank_account():
    """
    Function to test the BankAcct class.
    """

    print("=== Creating Account ===")
    acct = BankAcct("John Doe", "123456", 1000.00, 0.05)
    print(acct)


    print("\n=== Deposit $500 ===")
    acct.deposit(500)
    print("Balance:", acct.get_balance())


    print("\n=== Withdraw $200 ===")
    acct.withdraw(200)
    print("Balance:", acct.get_balance())


    print("\n=== Adjust Interest Rate to 3% ===")
    acct.adjust_interest_rate(0.03)
    print(acct)


    print("\n=== Calculate Interest for 30 days ===")
    interest = acct.calculate_interest(30)
    print(f"Interest for 30 days: ${interest:.2f}")


    print("\n=== Final Account Info ===")
    print(acct)


# ============================================
# Main Function
# ============================================

def main():
    test_bank_account()


# Run program
if __name__ == "__main__":
    main()