def new_game():
    guesses=[]
    correct_guesses=0
    question_number=1
    for key in questions:
        print("--------------------------------")
        print(key)
        for i in Options[question_number-1]:
            print(i)
        guess=input("Enter(A,B,C,D):").upper()
        guesses.append(guess)

        check_answer(questions.get(key),guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_number+=1

    display_score(correct_guesses,guesses)
#--------------------------
def check_answer(answer,guess):

    if answer==guess:
        print("CORRECT!")
        return 1
    else:
        print("INCORRECT!")
        return 0
#--------------------------
def display_score(correct_guesses,guesses):
    print("------------------------------------")
    print("RESULTS")
    print("------------------------------------")
    print("ANSWERS: ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("Guesses: ",end="")
    for i in guesses:
        print(i,end=" ")
    print()
        
    score = int((correct_guesses/len(questions))*100)
    print(f"Your Score is: {score}%")
#-------------------------- 
def play_again():
    response = input("Do you want to play again? (yes no): ").upper()
    print(f"Response: {response}")
    if response=="YES":
        return True
    else:
        return False
#--------------------------
questions={
"Who created Python?: ": "A",
"What year was Python created?: ":"B",
"Python is attributed to which comedy group?":"C",
"Is the Earth round?: ":"A"
}

Options=[[ #list of lists
"A. Guido van Rossum","B. Elon Musk", "C. Bill Gates","D: Mark Zuckerberg"],
["A. 1989", "B. 1991", "C. 2000","D. 2016"],
["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
["A. True", "B. False","C. sometimes","D. What's Earth?" ]]

new_game()

while play_again():
    new_game()

print("Goodbye!")