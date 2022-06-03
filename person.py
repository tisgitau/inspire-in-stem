#1/user/bin/##
#date : 2/5/2022
#name : Sam Gitau

class Person :
    def __init__ (self,_name ,_age):
         self.name = _name
         self.age = _age
    def sayHi(self):
        print("hello my name is" +str(self.name )+ "and i am age" + str(self.age))
person1 = Person ("Bob", 16)
person1.sayHi()
person2 = Person ("James",24)
person2.sayHi()

