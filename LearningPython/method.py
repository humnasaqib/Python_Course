import random
#*************** FORMAT METHODS IN PYTHON****************************
# str.format() = optional method that gives users more control when displaying output.

animal = "cow"
item = "moon"

print("The " + animal + "jumped ovee the" + item ) #standard way to write a print statement
#now we can write same thing using placeholders and format methods

print("the {} jumped over the {}".format(animal,item)) #the curly brackets are placeholders
#curley braces are known as format fields. they function as place holder for value. and they work in order.
#another way of inserting values at a given place holder would be to use waht's referred to as positional argument.
#example below

print("the {1} jumped over the {0}".format(animal,item)) #positioal argument
print("the {animal} jumped over the {item}".format(animal = "cow",item = "moon")) #keyword argument. we will use keyword argument name in this.

print("the {animal} jumped over the {animal}".format(animal="panda", item="noone")) #you can use one keyword argument more than once.
#there is even more neater and elegant way to write this and you can do it by using the way below
text ="The {} jumped over the {}"
print(text.format(animal,item)) # so basically the more elegant way to write this is by storing the format field as a variable and thenusing the fromat method in the print statement along with the variable.

#next method we will dicsucc is how to add some padding to a string when we display it using the format method.
name = "humna saqib"
print("hello my name is {}".format(name)) # currently this will display as hello my name is humna saqib. now we can add some padding to the left or right side.
#let's add padding to the rigth side of the name that we have.
print("hello my name is {:20}. Nice to meet you".format(name)) #this is right align
print("hello my name is {:<20}. Nice to meet you".format(name)) #this is left align
print("hello my name is {:>20}. Nice to meet you".format(name)) #this is right aligned
print("hello my name is {:^20}. Nice to meet you".format(name)) #center align

#now we will talk about how to format numbers.
number = 3.141519
print("the number pi is {:.2f}".format(number)) #this will display only the 2 digits after the decimal. because we placed 2 within the format field.
number2 = 1000
print("the number pi is {:,}".format(number2)) #this will automatcially add , to all 100's places.
print("the number pi is {:b}".format(number2)) #tis will display binary representation of your number
print("the number pi is {:e}".format(number)) #will display your number in scientific notation.


#******************************* RANDOM MODULE USE CASES*************************
#HOW TO GENERATE RANDOM NUMBERS
#-pseudo random numbers
#random number between 1 and 6
x = random.randint(1,6)
print(x)
#you can also generate random floating point  number as well. example below
y = random.random()
print(y)
#you can also generate random choice from a collection
myList = ['rock','pAPER','scissors']
z = random.choice(myList)
print(z) #picking randomm values from a list.
#you can also shuffle a list or random collection using random module methods, example bekow
cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
random.shuffle(cards)
print(cards)


