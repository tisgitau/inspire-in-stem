
#1/user/bin/python

############
#  Name : Sam Gitau
#  Date:24/5/2022
#################
#loops : for loops with 
#write aprogram to withdraw 2500 if acc bal is between 100000 to 200000
acc_bal = input ("enter you acc bal")
if (int)(acc_bal) > 100000 and (int(acc_bal) < 200000) :
    acc_bal = acc_bal = 25000 
    print("we have deducted ksh 25000")
elif(int(acc_bal) > 500000 and (int(acc_bal) < 1000000)):
     acc_bal= int(acc_bal)-(int(acc_bal)*0.3)
     print("we have deducted 30%")
elif(int(acc_bal)>1000000):
    acc_bal= int(acc_bal)-15000
    print("we have deducted 15000")
else:
    print("no deductions")
    