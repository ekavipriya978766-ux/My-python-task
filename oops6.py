class customer:
    def __init__(self,name,mobile_no):
        self.name=name
        self.mobile_no=mobile_no
    def display_customer(self):
        print("name",self.name)
        print("mobile_no",self.mobile_no)
class order(customer):
    def __init__(self,quantity,price):
        self.quantity=quantity
        self.price=price
    def calculate_total(self):
        print(quantity*self.price)
class payment(order):
    def __init__(self,name,mobile_no,product_name,quantity,price):
        super().__init__(quantity,price) 
        self.name=name
        self.mobile_no=mobile_no
        self.product_name=product_name
        self.quantity=quantity
        self.price=price
    def amount(self):
        total=self.calculate_total()
        if total>=0:
            print("payment successfully")
            print("total amount:",total)
        else:
            print("invalid order")
name=input("enter the name")
mobile_no=int(input("enter the mobile_no"))
product_name=input("enter the product_name")
quantity=int(input("enter the quantity"))
price=float(input("enter the price"))
s1=payment("name","mobile_no","product_name","quantity","price")
s1.amount()
    

        
