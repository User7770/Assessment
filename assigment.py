class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account {self.account_number}, Balance: ${self.balance:.2f}"


def main():
    # Create an account
    account_number = input("Enter your account number: ")
    initial_balance = float(input("Enter initial balance: "))
    account = BankAccount(account_number, initial_balance)

    while True:
        print("\nBanking Options:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == 3:
            print(f"Current balance: ${account.get_balance():.2f}")
        elif choice == 4:
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
