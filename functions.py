



#functions 
#def say_hello():
    #print("Hello from JKUAT")
    #r = 4
    #y = 6
    #z = r + y
    #print(z)
#say_hello()

#animal sounds










#add numbers
#def add_number(x,y):
    #sum_nums = x + y
    #print("the sum of numbers:",sum_nums)
#add_number(100,200)
#add_number(200,400)

# multiply
#def multiply_numbers(z,w):# z and w are called parameters
    #multiply_nums = z * w
    #print("multiply numbers:",multiply_nums)
#multiply_numbers(9,5)

# Using default parameters
#def print__name(name ="Sam Gitau"):
    #print (name)
#print__name("Timothy")

#return from a function
#def get__sum(num1, num2):
    #sum__nums = num1 + num2
    #return sum__nums
#print(get__sum (7,12))

#getting squers of numbers
#def get__power(number,power):
    #pow__nums = number**power
    #return pow__nums
#print(get__power(6,4))

#getting full names
#def get__full__names( f.name, s.name):
    #full__name = f.name + s.name
    #return get__full__names
#print(get__full__names("Sam" , "Gitau"))

#Returning dictionaries
def create_full_name(first_name , second_name):
    person = {"first":first_name,"second":second_name}
    return person
print (create_full_name ("Sam","Gitau"))

#pasing a list in a function
def greet_friends(names):
    for name in names :
        msg = "hello" + name.title() + "!"
        print(msg) 
friends = ["Tim", "Erick","Sally"]
greet_friends(friends)