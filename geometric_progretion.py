
#1/user/bin/python

############
#  Name : Sam Gitau
#  Date:27/5/2022
#################

#geometric progretion
a = int(input("enter first number"))
r = int(input("enter first number"))
n = int(input("enter first number"))

for i in range (1,n+1):
    n_term =a*r*(i-1)
    print(n_term)

#sum
s_m = float((a*(1-r**n) /1-r)) 