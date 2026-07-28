class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print("name",self.name)
        print("age",self.age)
class student(person):
    def __init__(self,name,age,roll_no,course):
        super().__init__(name,age)
        self.roll_no=roll_no
        self.course=course
s1=student("kavi",20,420,"CSBS")
print(s1.name)
print(s1.age)
print(s1.roll_no)
print(s1.course)
