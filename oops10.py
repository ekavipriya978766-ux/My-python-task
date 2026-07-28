class BankAccount:
    def __init__(self,initial_balance=0):
        self.__balance=initial_balance 
    def deposit(self,amt):
        if amt>0:
            self.__balance+=amt
            print("Deposit successful")
        else:
            print("Invalid deposit amount")
    def withdraw(self,amt):
        if amt <= self.__balance:
            self.__balance -= amt
            print("Withdraw successful")
            self.get_balance()
        else:
            print("Insufficient balance")
    def get_balance(self):
        print("Current Balance:", self.__balance)
account=BankAccount()
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        amt=float(input("Enter amount to deposit: "))
        account.deposit(amt)
    elif choice==2:
        amt=float(input("Enter amount to withdraw: "))
        account.withdraw(amt)
    elif choice==3:
        account.get_balance()
    elif choice==4:
        print("Thank you!")
        break
    else:
        print("Invalid choice")