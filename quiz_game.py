print("\n===============================")
print("\n========== QUIZ GAME ==========")
print("\n===============================\n")

questions = ("How many elements are in the periodic table?: ",
             "Which animals lays the largest egg?: ",
             "Which is the most abundant gas in earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which is the hottest planet in the solar sysrem?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Hydrogen", "C. Carbon Dioxide", "D. Oxygen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1  

print("----------------")
print("     REsult     ")              
print("----------------")

print("     answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Your guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

