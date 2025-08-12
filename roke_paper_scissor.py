import random
print("=== Welcome To Rock Paper Scissors Game ! ===\n")
print("You can choose from the following options:")
print("r → Rock")
print("p → Paper")
print("s → Scissors")

user_score = 0
computer_score = 0

while True:
    computer = random.choice([1, -1, 0])
    your_turn = input("Enter your choice: ")
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    youdict = {'r': 1, 'p': -1, 's': 0}
    reverse_dict = {1: "Rock", -1: "Paper", 0: "Scissors"}
    you = youdict[your_turn]
    print(f" 🧍 You Choose {reverse_dict[you]}\n 💻 Computer Choose {reverse_dict[computer]}")

    if(computer == you):
        print(" 🤝 Its a Draw!")
    elif(computer == -1 and you == 0):
        print("You Won!")
        user_score +=1
    elif(computer == -1 and you == 1):
        print(" ❌ You Lose!")
        computer_score +=1
    elif(computer == 1 and you == -1):
        print("You Won!")
        user_score +=1
    elif(computer == 1 and you == 0):
        print(" ❌ you Lose!")
        computer_score +=1
    elif(computer == 0 and you == 1):
        print("You Won!")
        user_score +=1
    elif(computer == 0 and you -1):
        print(" ❌ You Lose!")
        computer_score +=1   
    else:
        print(" ⚠️ Something Went Wrong!")

    print(f" 📊 Score → You: {user_score} | Computer: {computer_score}\n")

    again = input("Do you Want To Play? (y/n): ").lower() 
    if(again != 'y'):
        print("Exiting The Game....")
        print(f"\n🏁 Final Score → You: {user_score} | Computer: {computer_score}")
        break                        