class bank_account:
    def __init__(self,account_no,name):
        self.account_no=account_no
        self.name=name
    def display_account(self):
        print("account_no",self.account_no)
        print("name",self.name)
class saving_account(bank_account):
    def __init__(self,balance):
        self.balance=balance
    def display_saving(self):
        print("balance",self.balance)
class online_account(saving_account):
    def __init__(self, account_no, name, balance,avl_balance):
        super().__init__(balance)
        self.account_no=account_no
        self.name=name
        self.avl_balance=avl_balance
    def withdraw(self,amount):
            if amount>self.balance:
                print("Insufficient balance")
            else:
             self.balance-=amount
             self.avl_balance-=amount
             print("Withdrawal successful")
s1=online_account("78779888989","Priya",10000,10000)
print("acc no:",s1.account_no)
print("name:",s1.name)
print("balance:",s1.balance)
print("avl balance:",s1.avl_balance)
amount=float(input("Enter amount:"))
s1.withdraw(amount)
s1.display_saving()