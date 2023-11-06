#****************************************INHERITENCE IN PYTHON*****************************************
#inheritance
#classes can inherit  attributes and methods form another class.
#these classes can form parent-child relationships where a child will receive everything that the parents class has.
class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal): #rabbit is child class and animal is parents class.
#let us have different methods of these of our classes
    def run(self):
        print("This rabbit is running")

class Fish(Animal):

    def swim(self):
        print("This animal can swim")

class Hawk(Animal):
   def kill(self):
       print("This animal can kill")





rabbit = Rabbit() #now we will be creating three object from the class above.
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

hawk.kill()
rabbit.run()
fish.swim()

#***********************************MULTI-LEVEL INHERITANCE********************************
#multi-level inheritance = when a derived (child) inherits another derived (child) class
