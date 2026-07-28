class user_login:
    def __init__(self, username,password):
        self.username = username
        self.password = password
    def login(self):
        username=input("Enter username: ")
        password=input("Enter password: ")
        if username==self.username and password==self.password:
            print("Login successful")
            return True
        else:
            print("Login failed")
            return False
class food:
    def __init__(self,food_name,quantity):
        self.food_name=food_name
        self.quantity=quantity
    def place_order(self):
        print("1.Place Order")
        print("2.Exit")
        choice=int(input("Enter choice: "))
        if choice==1:
            print("Food:",self.food_name)
            print("Quantity:",self.quantity)
        elif choice==2:
            print("Order cancelled")
class food_delivery(food, user_login):
    def __init__(self,username,password,food_name,quantity,amt):
        user_login.__init__(self,username,password)  
        food.__init__(self,food_name,quantity)       
        self.amt = amt
    def generate_bill(self):
        print("User:", self.username)
        print("Food:", self.food_name)
        print("Quantity:", self.quantity)
        print("Total Bill:", self.quantity * self.amt)
username = input("Set username: ")
password = input("Set password: ")
food_name = input("Enter food name: ")
quantity = int(input("Enter quantity: "))
amt = float(input("Enter price per item: "))
s1 = food_delivery(username, password, food_name, quantity, amt)
if s1.login():
    s1.place_order()
    s1.generate_bill()