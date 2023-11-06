#_______________________________________________
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in question:
        print()
        print(key) #what this for loop is doing is basically just displaying the KEYS ONLY, NOT VALUES ONLY KEYS FROM OUR DICTIONARY
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter a, b,c,d").upper()
        guesses.append(guess)

        correct_guesses +=check_answer(question.get(key), guess )





        question_num += 1

    display_score(correct_guesses, guesses)


#_______________________________________________
def check_answer(answer,guess):
    if answer == guess:
        print("correct")
        return 1
    else:
        print("wrong")
        return 0

#_______________________________________________
def display_score(correct_guesses, guesses):
    print("")
    print("results")
    print("Answers: ", end="")
    for i in question:
        print(question.get(i), end=" ") #confused about this line.
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print((i), end=" ")
    print()


    score = int((correct_guesses/len(question))*100) #confused here as well
    print("your score is " + str(score)+ "%")



#_______________________________________________
def play_again():

    response = input("Do you want to play again: (yes/no)")
    response = response.upper()

    if response == "YES":
        return True

    else:
        return False
# now we will create a collection that will hold all our questions. we will be using a dictionary here
#as we know a dictionary has key:value pairs. each key is a question that i would like to ask nd each question has an associated value.

question = {
    "what is my name?: ": "A",
    "what year was I born in?: ": "B",
    "Where was I born?: ": "C",
    "Is earth round?: ": "D"
}
#now we will be using a collection to store all the answer choices and specifically we will be using a 2D list
# as we know 2D list is basically a list of list

options = [["A. Humna ", "B. Taha ", "C. None", "D. Zainab"],
           ["A. 2005" , "B. 2002", "C. 1984" , "D. 2000"],
           ["A. USA ", "B. India " , "C. Pakistan" , "D. Saudia"],
           ["A. no ", "B. what is earth", "C.Sometimes", "D. yes "]
]
new_game()

while play_again():
    new_game()

print(
    "Bye"
)
