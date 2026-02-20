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
        

    def transfer(self, receiver):
        print("\n--- Transfer Money ---")
        input_secret = input("Input Secret Number: ")

        if input_secret == str(self.secret):
            amount = float(input("Amount to transfer: "))

            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                receiver.balance += amount
                print("Transfer Successful!")
                print(f"Your Balance: ${self.balance}")
            else:
                print("Not enough money!")
        else:
            print("Wrong Secret Number!")
            
            
raty = Khmerbank("Raty", "012345678", 123456, 1122, 1000)


             
         
   
   
        
class SavingAccount(Khmerbank):
    def __init__(self, name, phone, password, secret, balance):
        super().__init__(name, phone, password, secret, balance)
        print(f"--- Saving Account Ready: {self.name} ---")
    
     
    def calculate_interest(self):
         interest = 10
         self.balance += 10
         print("\n--interest applied--")
         print(f"Added: ${interest}   ----   New Balance: ${self.balance}")
    
    
    
raty = SavingAccount("Raty", "012345678", 123456, 1122, 1000)  


vanra = SavingAccount("Vanra", "011223344", 654321, 2233, 500)
     
        

while True:
    print("\n=========Wellcome KhmerbANK =========")
    print("1-Check Balance")
    print("2-Withdraw ")
    print("3-Deposit")
    print("4-Calulate Interest")
    print("5 - Transfer Money")
    print("6-Exit")
    

    choose = input("Choose Number (1-6): ")

    if choose == '1':
        raty.check_balance()
    elif choose == '2':
        raty.withdraw()
    elif choose == '3':
        raty.deposit()
    elif choose == '4':
        raty.calculate_interest()
    elif choose == '5':
        print("\nTransfer to:")
        print("1 - Vanra")
        print("2 - Raty")

        user = input("Choose account: ")

        if user == '1':
            raty.transfer(vanra)
        elif user == '2':
            raty.transfer(raty)
        else:
            print("Account not found!")
    elif choose == '6':
        print("Thank")
        break
    else:
        print("NO NO")