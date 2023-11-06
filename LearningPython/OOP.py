#*************************** OBJECT ORIENTED PROGRAMMING**********************
#Object orinted programming in python
#an object is an instance of a class.
# in order to create an object, you need to create a  class.
# a class can function as a blue print that will describe that what methods and attributes that  our distince type of object will have,
 #class names should be capital
    #now we can receive arguments when we create car objects but we need to pass them in.
class Car:
    #class variable is declared inside the class but outside of the constructor. and what we can do here is set some default values.
    wheels = 4 #class variable
    def __init__(self, make, model, year, color): #init method is also known as a constructor
        self.make = make
        self.model = model
        self.year = year #variables inside the constructor are called or known as instance variable
        self.color = color

    def drive(self):
        print("This car is driving")
#what you can also do is fixitiate sentence with attributes mentioed in init method, example below
        print("This "+ self.model + "is driving")
    #the self keyword, think of it as you're replacing self with the name of the obejct that we are working on.

    def stop(self):
        print("This car is stopped")
        print("This " + self.model + "is stopped")





#we need one more method that is a special method that we will absolutely need.
#this will construct objects for us.



#how to import a class to a different module? SYNTAX BELOW
#from car import Car
#object can have attributes and methods.
#attribute describe what an object is or has

#********************************** BASICS OF CLASS VARIABLE IN PYTHON***************************
#differecnes between class and instance variables

car_1 = Car("Chevy", "Corvet", 2021, "Blue")
car_2 = Car ("Ford", "Mustang", 2022 , "red")



car_1.wheels = 2
car_2.wheels
print(car_1.wheels)
print(car_2.wheels) #will be using that default amount of wheels




#****************************************INHERITENCE IN PYTHON*****************************************
#inheritance
#classes can inherit  attributes and methods form another class.
#these classes can form parent-child relationships where a child will receive everything that the parents class has.  
