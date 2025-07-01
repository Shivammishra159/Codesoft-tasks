import random

user_score = 0
computer_score = 0

print("Welcome to Rock-Paper-Scissors Game!")

while True:
    user = input("Enter rock, paper, or scissors: ").lower()
    if user not in ["rock", "paper", "scissors"]:
        print("Invalid input. Try again.")
        continue

    computer = random.choice(["rock", "paper", "scissors"])

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print("Score -> You:", user_score, "| Computer:", computer_score)

    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break
