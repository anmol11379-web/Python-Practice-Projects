class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")

    def display(self):
        print(f"\nAccount No: {self.account_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Balance: {self.balance}")

def main():
    account_number = input("Enter account number: ")
    holder_name = input("Enter account holder name: ")
    account = BankAccount(account_number, holder_name)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Account Details")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.display()
        elif choice == '4':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
