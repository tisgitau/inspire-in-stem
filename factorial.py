
#1/user/bin/python

############
#  Name : Sam Gitau
#  Date:27/5/2022
#################

number = int(input("enter the number"))
factorial=1
if number<0:
    print("factorial of negative number does not exist")

else:
    for i in range (1,number+1):
     factorial= factorial*i
print("factorial of" "number" ,"is",factorial)
