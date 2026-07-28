class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("name",self.name)
        print("age",self.age)
s1=student(name=input("enter the name"),age=(input("enter the age")))
s1.show()