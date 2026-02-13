class Khmerbank:
    def __init__(self, name, phone, password, secret, balance):
        self.name = name
        self.phone = phone
        self.password = password
        self.secret = secret
        self.balance = balance

    def check_balance(self):
        print(f"\n--- Information---")
        print(f"Account Name៖ {self.name} | Balance៖ ${self.balance}")

    
    def withdraw(self):
        print("\n--- Withdraw---")
        input_secret = input("Input  (Secret Number)៖ ")

        if input_secret == str(self.secret):
            amount = float(input("Amount៖ "))
            if amount <= self.balance and amount > 0:
                self.balance -= amount
                print(f"Withdraw Successfully! Your Balance៖ ${self.balance}")
            else:
                print(" Not Enough Money!")
        else:
            print(" Wrong Number! Try Again")

    def deposit(self):
        print("\n--- Deposite---")
        input_phone = input("Input your Phone Number៖ ")
        input_pass = input("Input your Password៖ ")

        if input_phone == self.phone and input_pass == str(self.password):
            amount = float(input("Amount៖ "))
            if amount > 0:
                self.balance += amount
                print(f" Deposite Successfully៖ ${self.balance}")
            else:
                print("The amout must be greater than 0")
        else:
            print(" Erro!")

raty = Khmerbank("Raty", "012345678", 123456, 1122, 1000)

while True:
    print("\n=========Wellcome to KhmerbANK =========")
    print("1-Check Balance")
    print("2-Withdraw ")
    print("3-Deposit")
    print("4-Exit")

    choose = input("Choose Number (1-4): ")

    if choose == '1':
        raty.check_balance()
    elif choose == '2':
        raty.withdraw()
    elif choose == '3':
        raty.deposit()
    elif choose == '4':
        print("Thank")
        break
    else:
        print("NO NO")