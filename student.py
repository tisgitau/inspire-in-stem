
class Student():
    def __init__(self,name,hobby,year_of_birth):
        self.name =  name
        self.hobby = hobby
        self.year_of_birth = year_of_birth
    def greet_student(self):
        print("Hello from"+ self.name)