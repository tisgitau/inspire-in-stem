#1/user/bin/##
#date : 6/5/2022
#name : Sam Gitau

from student import Student
from teachers import Teachers
import operation
print(operation.add_nums(3,5))
print(operation.divide_nums(4,2))
print(operation.subtract_nums(40,10))
print(operation.mult_nums(30,10))

new_student = Student("John","skatting",1990)
new_student.greet_student()

new_teacher = Teachers("Juma",1234,"English",4654)
new_student.get_tsc_no()


