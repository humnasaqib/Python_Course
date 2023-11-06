#*********************FUNCTIONS IN PYTHON*******************
#function =  a block of code which is executed only when it is called

def hello(name): #defining a function
#parameters here in your definiton of function
    print("hellow " + name)
    print("have a nice day")



hello("humna") #executing a function
#arguments are thigns you are sending to your functions

#you can aslo send a variable in functions
name ="humna saqib"
hello(name)
#******************Return Statment in PYTHON*************
#reutrn statement = Functions send Python values/object back to the caller.
# These values/objects are known as the function's return value.
def multiply (num1,num2):
    result = num1 * num2
    return result

print(multiply(6,9)) #this print will give you a return value
#you can also store the return value within a variable
x = multiply(6,8)
print(x) #this will assign the return value to x

#***********************KEY WORD ARGUMENTS IN PYTHON*******************
#arguments preceded by an identifier when we pass them to a function.
#The order of the argument doesn't matter, unlike positional arguments. Python knows the names of the arguments that our function recevoes.
#EXAMPLE BELOW

def hello(first,middle,last):
    print("Hello " + first + middle + last)

hello("bro", "Dude", "Code") #we are using positional arguments and order of the arguments does matter.
#now if we use keyword arguments, the order of the arguments does not matter

hello(last="saqib",middle="none", first="humna") #this is usingkeyword arguments, because we are preceding it with an identifier.


#****************NESTED FUNCTION CALLS IN PYTHON****************
#Nested Functions Calls = function calls inside other function calls
#innermost function calls are resolved first
#returned value is used as argument for the next outer function
#example

num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num) #so we can do this entire thigns that we did with this code in less number of lines using nested function
num = round(num)
print(num)


input(round(abs(float(input("Enter a whole positive number: ")))))
