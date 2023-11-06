import os
import shutil
import messages
#************************************ EXCEPTION HANDLING IN PYTHON************************

#exception : events detected during execution that interrupt the flow of a program.

#basic form of exception handling is to surround any code that is considered dangerous qithin a try block

#we will create a progam that will throw exception intentionally
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = (int(input("Enter a number to divide by: ")))
    result = numerator/denominator
    print(result) #it is not good practice to have just on exception block.
#additional ways in which you could handle exceptions is that we could display exceptions that occurs and you can do that by using e , although it is optional

except ZeroDivisionError as e: #occurs when someone attempts to divide by 0
    print(e)
    print("you can not divide by 0 dummy ")

#except Exception:
   # print("something went wrong")

except ValueError as e:
    print(e)
    print("enter only number pls")

#so in the progrma abobe, if i were to divide 5 by 0, we obv mathemtically can not do that and this will reult in an error
#another thing that you can do is to add an else statement.if an exception happend it will handle it, if not it will go to else.
else:
    print(result)
#another caluse that you should be aware of is the finally clause.it is always at the end
finally:
    print("this will always execute") #whether or not we encounter exception, this will always run

#********************************** BASIC FILE DETECTION USING PYTHON*******************
#recomended to import OS
path = "/Users/humnasaqib/Desktop/test.txt"
if os.path.exists(path):
    print("that location exists!")
    if os.path.isfile(path):
        print("that is a file") #this will detect if it is a file or not.
    elif os.path.isdir(path):
        print("that is a directory") #this will tell you if it is a file or a directory.
else:
    print("that location does not exists")
#************************ READING A FILE IN PYTHON*************************
try:
    with open("test.txt") as file:
        print(file.read()) #what this will do is read the content of your file line by line and print it to you in your console.
#the method above will also close files automatically after opening them.
except FileNotFoundError:
    print("that file was not found")

print(file.closed) #this will show you if the file is open or closed.

#***************************** Writing files in PYTHON**********************
text = "yoooooooo\n this is some text\n have a food one\n" #\n is new line character
with open('test2.txt','w') as file: #w is to write a file
    file.write(text) #you can also change the mode to a for append. and that will allow you to add more files.

#*****************************COPYING FILES IN PYTHON***********************************
import shutil #import shutil module. in this module you have 3 basic functions to copy a file
# all three methods are listed below
#copyfile() = copies contetns of a file
#copy() = copyfile() + permission mode + destination can be a directory
#copy2() = copy() + copies metadata (file's creation and modification times)

shutil.copyfile('test.txt', 'copy.txt') # 2 aruguments, source and destination
#***************************************HOW TO MOVE FILES USING PYTHON*********************
import os #recommended

source = "folder"
destination = "/Users/humnasaqib/folder"


try:
    if os.path.exists(destination):
        print("there is already a file there ")
    else:
        os.replace(source,destination)
        print(source+ "was movded")
except FileNotFoundError:
    print(source+ "was not found")

#you can also move a directory as well. i just changed the above code to a directory instead of a file.
#************************* DELETING FILES USING PYTHON****************************
path2 = 'delete.txt'
try:
  os.remove(path2) #removed a filles
except FileNotFoundError:
    print("Files was not found")
#deleting a directory
path3 = 'empty_folder'
try:
  os.rmdir(path3) #rmdir short for remove directoory. this will delete empty directory
except FileNotFoundError:
    print("Files was not found")
except PermissionError:
    print("You do not have permission to delete that ")
except OSError:
    print("you can not delete a filled directory using rmdir method ")

else:
    print("path was deleted")


#to delete  a filled directory, use the methid below
#first make sure to import shutil

path4 = 'folder'
try:
    shutil.rmtree(path4) #deletes a directory containig files.

except NotADirectoryError:
    print("please add a directory/ folder and not a text file")

else:
    print("directory was deleted")

#**************************************** DISCUSSING MODULES IN PYTHON******************************
#module = a file containing python code. May contain functions, classes, etc.
#used with modular programming, which is to seperate a program into parts.

#to import a function written in some other module, you have to write import "name of module" in out case it will be messages.
#to use a function from that module, type the name of the module.name of the function
messages.hello()
messages.bye()
#it could be tedious to write entire names of modules, so at the top you could write
#import messages as msg
#you could import call modules using the method below
#from messages import hello, by
#another way to write this is
#from messages import * #this will import all the functions
#if you want all the prewritten modules python has, just type, help("modules")