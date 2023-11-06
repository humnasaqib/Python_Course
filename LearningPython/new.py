n = 5
for i in range(n):
    for j in range(i+1):
        print("@", end='')
    print()  # Add this line to move to the next row
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("@", end='')
    print()
for i in range(0,10):
    print("heloo world")

for i in "Humna Saqin":
    print(i,end="")
print()
#*********LOOP CONTROL STATEMENTS IN PYTHON**********
#loop control statements = change a loops execution from it's normal sequence
#break = used to terminate the loop entirely
#continue = skips to the next iteration of the loop
#pass = does nothingm acts as a place holder
#break example
while True:
    name = input("what is your name")
    if name != "": #!= basically means does not. This line basically means if the user dooes not type anything
        break
#a break is used to terminate a loop entirely when it is encountered.
#example of continue
phone_number = "123-456-7869"
for i in phone_number:
    if i =="-":
        continue
    print(i,end="")
print()
#what is happening in above code is that the loop is running, and skiiping the - that we have asked it to skip
#example of pass below
for i in range(1,21+1):

    if i == 13:
        pass
    else:
        print(i)
#what the above code is doing is basically skipping or not skipping, keep 13 as a placeholder.
#*********************LISTS IN PYTHON****************
#list = used to store multiple items in a single variable

food = ["pizza","burger", "pastas", "biryani"] #each item in a list is referred to as an element

print(food)
#if you want to list a certain element of this list, then exmaple below
print(food[1]) #basically specifiying the index
#one good things about list is that you can change elements in a list later on as well.example below

food[0] = "sushi"
print(food[0]) #we updated element 0 to be sushi
#if you want to display all of the elements found within a list you can easily do that with a standard for loop, example below

for i in food:

    print(i) #this will display all the elemtsn within the food list
#now we will talk about few useful functions of list
food.append("ice cream") #this will add ice cream to the end of you lsit
food.remove("biryani") #remove an elements from a list
food.pop() #will remove last element in a list
food.insert(0,"cake") #inserting a value at a given index
food.sort() #sort a list alphabetically
food.clear() #will remove all elements of a list
#***************** 2D LISTS IN PYTHON************
#2D lists = a list of lists, also refered to multidimensional list
drink = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger","hotdog"]
dessert = ["cake", "ice cream"]

food = [drink, dinner , dessert]
print(food)
#to access only one of the list, and not all of the lsits within thr 2D list, you can use indexing
print(food[0][1]) #in this example, the first parameter is basically the index of the lsits from the 2D lists adn second one is the index of within the list
#*********************** tuples in python**************************
#tuple = collection which is ordered and unchangeable. Use to group together related data

student = ("Humna", 21, "female")
print(student.count("Humna"))# how many time a vlaue appears. function of a tupple
print(student.index("female")) #gives you the index of  a value in a tuple
# few tricks we ccan do with tuples
for x in student:
    print(x)
if "Humna" in student: #another trick you can do with tuples is to use it with for loop and see if a certain vlaue is available in your tuple

    print("Humna is here")
#****************WHAT A SET IS IN PYTHON***********************
#set = collection which is unordered, unindexed,. No duplicate values

utensils = {"fork", "spoon", "knife"}
for x in utensils:
     print(x) # will not be in the same order as they are placed abvoe becuase they are unordered
#set is faste than a list if you want to check to see if something  is withint a set compared to a list
#set also does not allow any duplicate values.
# few useful method of sets
# add an item to our set
utensils.add("napki") # adding an element to a set
utensils.remove("fork") #removing an element from a set
utensils.clear() #all elements iwthin set should be gone

dishes = {"bowl", "plate", "cup", "knife"}
#now we will be adding one set to another by using the update method

utensils.update(dishes) #will add all of the elemts found within dishes to our element set
# we can also join two sets together and create a new set entirely
dinner_table = utensils.union(dishes) # this is basically creating a new set and conjoining the 2 previous sets together
# compare similarities and elements found within a set
print(utensils.difference(dishes)) #this will print what utensils has that dishes does not
print(utensils.intersection(dishes))# this will return whatever element they have in commomn


#*********************** DICTIONARY IN PYTHON**************************
#dictionary = a changeable, unordered colelction of unique key: value pairs.
#Fast because theu use hashing, allow us to access a value quickly

capitals = {"USA":'Washington DC',
            "India": "New Delhi",
            "China" :"Beijing",
            "Russia": "Moscow"
}
print(capitals['Russia']) #since dictionaries are unordered, you can not use an index to print out a certain vlaue, rather you use a key for that balue. This is an example of that
# A much safer way to access the key to check if it is there, hou can use the get method of the dictionaries
print(capitals.get('Germany')) # this will return none because we do not have any germany value in our dictionary
# FEW OTHER USEFUL METHODS
print(capitals.keys()) #will print only the keys and not the values
print(capitals.values()) #will only print values
print(capitals.items()) #will print your entire dictionary

for key, value in capitals.items():
    print(key,value) #printing an entire dictionary using for loops.
#dictionaries are mutable, ,meaning we can chage them even if it still running.
capitals.update({'Germany': 'Berline'}) # this will add a new key value pair to your dictionary
capitals.update({'USA': 'NYC'}) # you can also change the value of an exisiting key
capitals.pop('China') # this will removethe key vlaue pair from your dicitonary
capitals.clear() #this will clear your dictionary
#************************** INDEX OPERATOR IN PYTHON*************************
#index operator [] = gives access to a sequence's element (str, lists, tuples)
name = 'humna saqib!' #we cna use the index operator to access an element of the sequence
# lets check if the first letter in our name is lowercase
if (name[0].islower()):
    name = name.capitalize()

print(name)

#creating substrings using index operator

first_name = name[0:4].upper() #with index operator, we speicifed a range, we would like to access index 0-4 and turn it into uppercase
last_name = name[6:].lower()
last_character = name[-1]

print(first_name,last_name)
print(last_character)
















