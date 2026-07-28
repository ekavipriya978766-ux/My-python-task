class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print("name",self.name)
        print("age",self.age)
class doctor(person):
    def __init__(self,name,age,dept):
        person.__init__(self,name,age)
        self.dept=dept
    def doctor_info(self):
        print("dept",self.dept)
class patient(person):
    def __init__(self,name,age,disease):
        person.__init__(self,name,age)
        self.disease=disease
    def patient_info(self):
        print("disease",self.disease)
class medical_intern(doctor,patient):
    def __init__(self,name,age,dept,disease,intern_id):
        doctor.__init__(self,name,age,dept)
        patient.__init__(self,name,age,disease)
        self.intern_id=intern_id
    def intern_info(self):
        print("intern_id",self.intern_id)
s1=medical_intern("kavi","20","xray","fever","23")
print("name:",s1.name)
print("age:",s1.age)
print("dept:",s1.dept)
print("disease:",s1.disease)
print("intern_id:",s1.intern_id)