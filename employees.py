#1/user/bin/##
#date : 2/5/2022
#name : Sam Gitau
#write a programme to print name , age , id number and salary
class employee:
    def __init__(self,_name , _age ,_idnumber,_salary):
        self.name = _name
        self.age = _age 
        self.idnumber = _idnumber
        self.salary = _salary
    def sayHi(self):
        print("my name is" + self.name
         + "my age is " + self.age +"my id number is"
         + self.idnumber + "my salary is ", + self.salary)
employee1 = employee ('Sam',str(25) , str(9449) , str(180000))
employee1.sayHi()
