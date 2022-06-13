
#1/user/bin/python

############
#  Name : Sam Gitau
#  Date:24/5/2022
#################

#using classes
#def dog (name , age):
    #print(f"the name of the dogis{name}age is{age}")
#dog( "bosco",8)

#class for vehicle
class Vehicle :
    def __innit__(speed,_max_speed ,_mileage):
        speed.max_speed = _max_speed
        speed.mileage = _mileage
vehicle1 =Vehicle(233 , 9998)
print (vehicle1._max_speed,vehicle1._mileage)        
