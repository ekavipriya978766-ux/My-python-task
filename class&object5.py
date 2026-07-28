class employee():
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def bonus(self):
        print("id",self.id)
        print("name",self.name)
        print("salary",self.salary)
        if self.salary>=50000:
            print("bonus=",self.salary*0.10)
        else:
            print("bonus=",self.salary*0.05)
e1=employee(11,"kavi",10000)
e2=employee(12,"pradeesha",20000)
e3=employee(13,"kalai",30000)
e4=employee(14,"sathya",40000)
e5=employee(15,"kaviya",50000)
e1.bonus()
e2.bonus()
e3.bonus()
e4.bonus()
e5.bonus() 