#****************************** VARIABLE SCOPES IN PYTHON****************
#scope = a variable is only available from inside the region it is created.
#a global and locally scoped versions of a variable can be created.

def display_name():
    name = "Code" #local scope variable (available only inside this function)
    print(name)


 #print(name) #you can see here that this wil give an error because name is only isnide of a function.

name = "Bro" #global variable scope (available inside and outside of function)
display_name()
print(name)
#you will use any local variable first, then you will use global if local's aren't there
#*********** ARGS PARAMETER IN PYTHON**************
#*args = parameter that will pack all arguments into a tuple.
#useful so that a function can accept a variny amount of arguments.
#example below
def add(num1,num2):
    sum = num1 + num2
    return sum

print(add(1,2))
#so what happens is that, if you were to pass 3 paramters in the statement above it qould give you an error,t o solve that you use *args


def add2(*args): #you can name the args whatever you want, important thing is astrick
    sum = 0
    for i in args:
        sum += i
    return sum

print(add2(3,0,9,8))

def add3(*args): #tuples are ordered and unchangebale, but if you wanted to change a value, you can use this method and turn tuple into a list.
    sum = 0
    args = list(args)
    args[0] = 100
    for i in args:
        sum += i
    return sum

print(add3(3,0,9,8))

#**************************** **KWARGS IN PYTHON******************************
# **kwargs = parameter that will pack all arguments into a dictionary.
#it is useful so that a function can accept a varying amount of keyword arguments.


def hello(**kwargs):
    print("Hello" + kwargs['first'] + "" + kwargs['last'])

hello(first="Bro",middle='none',last="Code")

#you do not need to name is kwargs, just make sure to have 2 **
#let's say we would like to display someone's full name based on the amount of keyword arguments that they pass into this function.
#we could write our program using for loop

def hello2(**kwargs): #kwarg is short for keyword arguments
    print("Hello", end=" ")
    for key,value in kwargs.items(): #.items IS A METHOD, IT ITERATES THROUGH THE KEY-VALUE PAIRS IN THE KWARGS.
        print(value,end=" ")

print(hello2(first="humna",middle=";lalalalalla",last="saqib" ))



