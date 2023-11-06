def new_game():
    guesses = []
    answer_you_picked = 0
    question_num = 0

    for key in questions:
        print(key)
        print()
        for i in options[question_num]:
            print(i)


        guess = input("please pick either a, b, c").upper()
        guesses.append(guess)
        answer_you_picked += answer(guess,questions.get(key))







        question_num += 1
    display_score(answer_you_picked,guesses)






def answer(guess, answer):
    if guess == answer:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0




def display_score(answer_you_picked,guesses):
  #  print("Here are the results")
    #print("Answers You Picked/ Correct Answers")

   # for i in guesses:
      #  print(i, end=" ")
   # print()

    #for i in questions:
      #  print(questions.get(i), end= " ")
    #print()

    print("")
    print("results")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")  # confused about this line.
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print((i), end=" ")
    print()


    score = int((answer_you_picked/len(questions))*100)
    print("your score is " + str(score))













questions = { "What is my name: " :"B" ,
                "what is your age: " : "C"

}

options = [["A. Ayesha ", "B. Humna", "C.Taha "],["A. 40", "B. 60", "C. 21"]]

new_game()
