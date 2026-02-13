class BankAccount:
    def __init__(self,balance,name,secret):
        self.__balance = balance
        self.name = name 
        self.__secret = secret
        
    def withdraw(self):
        print(f"{self.name} is withdraw money" )
        
    def check_balance(self,secret):
        if secret == self.__secret:
            print(f'{self.name} remaining balance is {self.__balance}')
        else:
            print("Who are you???")
       
sok = BankAccount(balance=100000,name="sok",secret="123")
sby  = BankAccount(balance=200,name="sby",secret="456")


sok.check_balance(secret="123")
sby.check_balance(secret="4567")

