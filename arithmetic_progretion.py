
#1/user/bin/python

############
#  Name : Sam Gitau
#  Date:27/5/2022
#################
#arithmetric_progretion
#a =first term
#d = common diffrence
#n= number of terms

from this import d


a = int(input ("enter the first number"))
d = int(input ("enter the first number"))
n =int(input ("enter the first number"))
for i in range (1,n+1):
    n_term = a+ (i-1)*d
    print(n_term)
sum_n = (n_term/2)*(2*a+(n-1)*1)
print(sum_n)