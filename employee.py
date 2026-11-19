class Employee:
    def get_details(self):
        self.name = input("Enter Employee Name: ")
        self.manager = input("Enter Manager Name: ")
        self.dept = input("Enter Department: ")
        self.exp = int(input("Enter Experience: "))
        self.score = int(input("Enter Score out of 100: "))

    def display(self):
        print("\nEmployee Name:", self.name)
        print("Manager Name:", self.manager)
        print("Department:", self.dept)
        print("Experience:", self.exp)
        print("Score:", self.score)

        if self.exp > 5 and self.score > 60:
            print("Eligible for Promotion")
        else:
            print("Not Eligible for Promotion")


e = Employee()
e.get_details()
e.display()  