class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} has been deposited.")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive number.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn.")

def main():
    atm = ATM()

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            atm.check_balance()

        elif choice == '2':
            try:
                amount = float(input("Enter the amount to deposit: "))
                atm.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '3':
            try:
                amount = float(input("Enter the amount to withdraw: "))
                atm.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '4':
            print("Exiting ATM. Thank you for using our services.")
            break

        else:
            print("Invalid option. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()
