class Employee():
    def __init__(self,id,name,dept,salary):
        self.id=id
        self.name=name
        self.dept=dept
        self.salary=salary
    def display(self):
        print("id",self.id)
        print("name",self.name)
        print("dept",self.dept)
        print("salary",self.salary)
n=int(input("how many employee they want to enter"))
employees=[]
for i in range(1,n+1):
    print(i,"employee")
    id=int(input("enter the id:"))
    name=input("enter the name:")
    dept=input("enter the dept:")
    salary=float(input("enter the salary:"))
    employee=Employee(id,name,dept,salary)
    file=open("employeedatabase.txt","a")
    print(file.write(f"name:{name}\nid:{id}\ndept:{dept}\nsalary:{salary}\n"))
    file.close()
for employee in employees:
    employee.display()

