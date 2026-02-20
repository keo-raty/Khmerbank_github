# Base class
class Khmerbank:
    def __init__(self, name, phone, password, secret, balance):
        self.name = name
        self.phone = phone
        self.password = password
        self.secret = secret
        self.balance = balance
        print(f"\n--- Account Created: {self.name} ---")

    def check_balance(self):
        print(f"\n--- Account Information ---")
        print(f"Account Name: {self.name} | Balance: ${self.balance}")

    def withdraw(self):
        print("\n--- Withdraw ---")
        input_secret = input("Input Secret Number: ")

        if input_secret == str(self.secret):
            amount = float(input("Amount: "))
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Withdraw Successful! Your Balance: ${self.balance}")
            else:
                print("Not enough money!")
        else:
            print("Wrong secret number!")

    def deposit(self):
        print("\n--- Deposit ---")
        input_phone = input("Input your Phone Number: ")
        input_pass = input("Input your Password: ")

        if input_phone == self.phone and input_pass == str(self.password):
            amount = float(input("Amount: "))
            if amount > 0:
                self.balance += amount
                print(f"Deposit Successful! New Balance: ${self.balance}")
            else:
                print("Amount must be greater than 0")
        else:
            print("Error: Wrong phone or password!")

    def transfer(self, receiver):
        print("\n--- Transfer Money ---")
        input_secret = input("Input Secret Number: ")

        if input_secret == str(self.secret):
            amount = float(input("Amount to transfer: "))
            if 0 < amount <= self.balance:
                self.balance -= amount
                receiver.balance += amount
                print("Transfer Successful!")
                print(f"Your Balance: ${self.balance}")
                print(f"{receiver.name} Balance: ${receiver.balance}")
            else:
                print("Not enough money!")
        else:
            print("Wrong secret number!")


# SavingAccount inherits Khmerbank
class SavingAccount(Khmerbank):
    def __init__(self, name, phone, password, secret, balance):
        super().__init__(name, phone, password, secret, balance)
        print(f"--- Saving Account Ready: {self.name} ---")

    def calculate_interest(self):
        interest = 10
        self.balance += interest
        print("\n--- Interest Applied ---")
        print(f"Added: ${interest}   ----   New Balance: ${self.balance}")


# StudentBankAccount inherits Khmerbank
class StudentBankAccount(Khmerbank):
    def __init__(self, name, phone, password, secret, balance):
        super().__init__(name, phone, password, secret, balance)
        print(f"--- Student Account Ready: {self.name} ---")

    def withdraw(self):
        print("\n--- Student Withdraw ---")
        input_secret = input("Input Secret Number: ")

        if input_secret == str(self.secret):
            amount = float(input("Amount: "))
            if amount > 500:
                print("You cannot withdraw more than $500 at once!")
            elif 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Withdraw Successful! Your Balance: ${self.balance}")
            else:
                print("Not enough money!")
        else:
            print("Wrong secret number!")


# PremiumSaving inherits SavingAccount
class PremiumSaving(SavingAccount):
    def __init__(self, name, phone, password, secret, balance):
        super().__init__(name, phone, password, secret, balance)
        print(f"--- Premium Saving Account Ready: {self.name} ---")

    def deposit(self):
        print("\n--- Premium Deposit ---")
        input_phone = input("Input your Phone Number: ")
        input_pass = input("Input your Password: ")

        if input_phone == self.phone and input_pass == str(self.password):
            amount = float(input("Amount: "))
            if amount > 0:
                bonus = amount * 0.02  # 2% bonus
                total = amount + bonus
                self.balance += total
                print(f"Deposit Successful! Amount: ${amount} + Bonus: ${bonus} = Total Added: ${total}")
                print(f"New Balance: ${self.balance}")
            else:
                print("Amount must be greater than 0")
        else:
            print("Error: Wrong phone or password!")

    def withdraw(self):
        print("Withdraw not allowed for Premium Saving accounts!")

    def transfer(self, receiver):
        print("Transfer not allowed for Premium Saving accounts!")


# BusinessAccount inherits Khmerbank
class BusinessAccount(Khmerbank):
    def __init__(self, name, phone, password, secret, balance):
        super().__init__(name, phone, password, secret, balance)
        self.loan_taken = 0
        print(f"--- Business Account Ready: {self.name} ---")

    def take_loan(self):
        print("\n--- Take Loan ---")
        input_secret = input("Input Secret Number: ")
        if input_secret == str(self.secret):
            amount = float(input("Loan Amount: "))
            if amount > 0:
                self.balance += amount
                self.loan_taken += amount
                print(f"Loan Approved: ${amount}")
                print(f"New Balance: ${self.balance} | Total Loans Taken: ${self.loan_taken}")
            else:
                print("Loan amount must be greater than 0")
        else:
            print("Wrong secret number!")


# Create example accounts
khmer_acc = Khmerbank("Raty", "012345678", 123456, 1122, 1000)
saving_acc = SavingAccount("Vanra", "011223344", 654321, 2233, 500)
student_acc = StudentBankAccount("Sophea", "099887766", 111222, 3344, 800)
premium_acc = PremiumSaving("Sareth", "088776655", 987654, 5566, 2000)
business_acc = BusinessAccount("MegaCorp", "077665544", 555666, 7788, 10000)


# Simple ATM Menu (example for Khmerbank and child accounts)
accounts = {
    "1": khmer_acc,
    "2": saving_acc,
    "3": student_acc,
    "4": premium_acc,
    "5": business_acc
}

while True:
    print("\n========= Welcome to KhmerBank =========")
    print("Choose Account:")
    print("1 - KhmerBank (Normal)")
    print("2 - Saving Account")
    print("3 - Student Account")
    print("4 - Premium Saving Account")
    print("5 - Business Account")
    print("6 - Exit")

    acc_choice = input("Select account (1-6): ")
    if acc_choice == "6":
        print("Thank you for using KhmerBank!")
        break
    elif acc_choice not in accounts:
        print("Invalid choice!")
        continue

    acc = accounts[acc_choice]

    # Show menu for selected account
    while True:
        print(f"\n--- {acc.name} Menu ---")
        print("1 - Check Balance")
        print("2 - Withdraw")
        print("3 - Deposit")
        print("4 - Transfer Money")
        if isinstance(acc, SavingAccount):
            print("5 - Calculate Interest")
        if isinstance(acc, BusinessAccount):
            print("6 - Take Loan")
        print("7 - Back to Account Selection")

        choice = input("Choose option: ")

        if choice == "1":
            acc.check_balance()
        elif choice == "2":
            acc.withdraw()
        elif choice == "3":
            acc.deposit()
        elif choice == "4":
            # For transfer, select target account
            print("\nTransfer to which account?")
            for key, a in accounts.items():
                if a != acc:
                    print(f"{key} - {a.name}")
            target_key = input("Target account: ")
            if target_key in accounts and accounts[target_key] != acc:
                acc.transfer(accounts[target_key])
            else:
                print("Invalid target account!")
        elif choice == "5" and isinstance(acc, SavingAccount):
            acc.calculate_interest()
        elif choice == "6" and isinstance(acc, BusinessAccount):
            acc.take_loan()
        elif choice == "7":
            break
        else:
            print("Invalid option!")