class Course:
    def create_course(self,course_name,instructor_name):
        self.course_name=course_name
        self.instructor_name=instructor_name
class OnlineCourse(Course):
    def display_details(self):
        print("Course Name:",self.course_name)
        print("Instructor Name:",self.instructor_name)
obj = OnlineCourse()
course = input("Enter Course Name: ")
instructor = input("Enter Instructor Name: ")
obj.create_course(course, instructor)
obj.display_details()