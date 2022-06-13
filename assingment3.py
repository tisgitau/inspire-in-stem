
#1/user/bin/python

############
#  Name : Sam Gitau
#  Date:30/5/2022
#################
#loops : for loops with list
age = input("what is you age")
gender = input("what is you gender:male/female")

acc_bal = 0

if (int(age)  > 25) and (int(age) < 30):
    acc_bal = acc_bal + 10000
    print("Confirmed you have received ")
else :
    print("no money available")
