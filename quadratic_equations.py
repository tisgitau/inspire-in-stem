#1/user/bin/##
#date : 31/5/2022
#name : Sam Gitau
#quadratic equation
#import math
#a = int(input("Enter the coefficient of first term"))
#b = int(input("Enter the coefficient of first term"))
#c = int(input("Enter the constant")) 
#def find_roots(a,b,c):
    #y1 =( -b +  math.sqrt((b**2)- 4 * a * c) )/ (2*a)
    #y2 =( +b - math.sqrt((b**2)- 4 * a * c) )/ (2*a)
    #print("roots of quadratic equation:",y1,y2)
#find_roots(a,b,c)
import math
a = int(input("Enter the coefficient of first term"))
b = int(input("Enter the coefficient of first term"))
c = int(input("Enter the constant"))
w = math.sqrt((b**2)-4*a*c)
def find_roots(a,b,c,w):
    y1=(-b-w)/(2*a)
    y2=(+b-w)/(2*a)
    print("roots of quadratic equation:",y1,y2)
find_roots(a,b,c,w)