import math
import time
print("Name is humna")
first_name = 'humna'
last_name = 'code'
full_name = first_name + last_name
print("hello " + full_name)

age = 21
age += 1
print(age)
print(type(age))

print("my age is" + str(age))

height = 250.5
print("your height is " + str(height)) #know as typecasting

humna = True
print("are you a human: " + str(humna))

name, age , attractive = "bro" , 21 , True #known as multiple assignemnt
spongebob = patrick = Sandy = squidward = 30 #when all variables have same value

name = "bro code"
print(len(name)) #return how long length of our string is, 3 for 3 characters
print(name.find("B")) #use to find the first index of where the character B is
print(name.capitalize()) #will make a string capitalize
print(name.upper())#will make things upper case
print(name.lower())#will make thigns lower case
print(name.isdigit())  #if string is a digit, this will reply either true or false
print(name.isalpha()) #will tell if it is alphabetical or not. If you add a space that will be counted as not alphabetica;l
print(name.count("o")) #count how many characters are in our string
print(name.replace("o" , "a")) #will replace characters in a string
print(name*3) #display string multipl times

#*********************** LEARNING ABOUT TYPE CASTING********************
x = 1 #int
y = 2.0 #floar
z = "3" #string

y = int(y) #this is also typecasting, but this is a permenanet change now
x = str(x) #converting int to a string
print(x)
print(y) #typecastin, converting flot to int
print(int(z) * 3) #also type casting.
#you can not dispaly a string along with an int or flot, hence typecasting is important
#*************** Accepting user input in python****************************
name = input("What is your name: ")
age = int(input("what is your age")) #casting with int becuase down below i am performing math and since user input is a string, it will not perform math operatin on a string so you need to convert to an int
height = float(input("how tall are you"))
age = age + 1 #adding 1 to someone's age

#whenver we accept data input frm user, it is always a string
print("hello" + name)
print("you are" + str(age) + "years old")
print("you are " + str(height) + "cm tall")
#************************* useful function relating numbers in python******************
#make sure to import math on top to allow these functions to work
pi = 3.14
x = 1
y = 2
z = 3

print(round(pi)) #will round the number for up
print(math.ceil(pi)) #round a number up  to the nearest whole integer
print(math.floor(pi)) #round a number down
print(abs(pi)) #absoulte value of a number. How far a number is away from 0.if the number is negative, it will turn it into positive
print(pow(pi , 2)) #raise a base number to a power. pass 2 argument, base and exponent
print(math.sqrt(420)) #will find a squre rott. based within math moduke
print(max(x,y,z)) #finds the largest value between all 3
print(min(x,y,z)) #finds minimum values between all 3
#***************************String slicing in python********************
#slicing = creating a substring by extracting elements from another string
#indexing[] or slice ()
#[start:stop:step]

name = "Bro Code"
first_name = name[0:3] #basically starting and stopping index
last_name = name[4:8]
funky_name = name[0:8:2] #in this example, step will only display every second character including the first
print(last_name)
#reversing a string in python
reversed_name = name[::-1]
print(reversed_name)
#explaining and using the slice function
website ="http://google.com"
website2 = "http://chvrhjkvcuhrb.com"
slice = slice(7,-4) #slice object is ready and now we can resue this
print(website[slice])
print(website2[slice])
#*******************if,elseif, and else statements********************
#if statement = a block of code that will only execute if it's conditions is true

age = int(input("how old are you"))
if age >= 18:
    print("you are an adult")
elif age == 100:
    print("you are too old") #order of your else if statements matters a lot
elif age < 0:
    print("you have not been born yet")
else:
    print("you are a child")
#*****************************  logical operators in python*********************
#operators (and, or, not) = used to check if two or more conditional statement is true.
temp = int(input("What is the temperature outside: "))
if temp >=0 and temp <= 30: #in order for this to be true, both conditions must be true in the and.
    print("Temperature is " + str(temp))
    print("go outside")
elif temp < 0 or temp > 30: #one of them is true then the entire statement is true
    print("the temperature is bad today: " + str(temp))
    print("stay inside")
#what the not logical oerator do is that if the condiiton is true, it will flip and turn it into false.
if not(temp >= 0 and temp <= 30): #if the condition is true, it will flip and if it is false, it will be true.
    print("bye whtaever")

#***********************WHILE LOOPS IN PYTHON*****************
#while loop= a statement that will execute its block of code, as long as it's conditions remains true.
name = ""
while len(name) == 0:
    name = input("Enter your name")

print("hello" + name)
#****************FOR LOOP***************
#for loop= a statement that will execute it's block of code a limited amount of times.
#while loop = unlimited
#for loop = limited

for i in range(10):
    print(i+1)
for i in range(50,100+1,2):#3 argumnets in total, the range that is from 50 and 100 and then last argument tells how much you want to add by.
    print(i)
for i in "Humna Saqin":
    print(i)
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("happy new year!")
#**************Nested Loops****************
#nested loops: the inner loop will finish all of it's iterations before finishing one iteration of the "outer" loop

rows = int(input("how many rows"))
columns = int(input("How many columns"))
symbol = input("entier a symbol to use")

for i in range (rows):
    for j in range (columns):
        print(symbol,end="") #after using the print statement, the edn will prevent our cursor from moving down to the next line.
    print()
rows1 = int(input("how many rows"))
columns1 = int(input("How many columns"))
symbol1 = input("entier a symbol to use")

for i in range (rows1):
    for j in range (columns1 + 1):
        print(symbol1,end="") #after using the print statement, the edn will prevent our cursor from moving down to the next line.
    print()




#************************* EXAMPLE FOR FOR LOOP ********************************












