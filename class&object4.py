class student():
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print("name",self.name)
        print("roll_no",self.roll_no)
        print("marks",self.marks)
    def result(self):
        if self.marks >=50:
            print("pass")
        else:
            print("fail")
s1=student("kavipriya",410624244011,43)
s2=student("pradeesha",410624244015,50)
s1.display()
s1.result()
s2.display()
s2.result()







class student():
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print("name",self.name)
        print("roll_no",self.roll_no)
        print("marks",self.marks)
    def result(self):
        if self.marks >=50:
            print("pass")
        else:
            print("fail")
s1=student(name=input("enter the name"),roll_no=input("enter the roll_no"),marks=input("enter the marks"))          
s2=student(name=input("enter the name"),roll_no=input("enter the roll_no"),marks=input("enter the marks"))                 
s1.display()
s2.display()
