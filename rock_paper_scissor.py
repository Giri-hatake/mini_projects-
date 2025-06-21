import random

choices = ['r', 'p', 's']

user_score = 0
computer_score = 0
rounds = 10 

for i in range(rounds):
    user = input(f"Round {i+1} - Choose r, p, or s: ").lower()
    print("you choose : " , user)
    while user not in choices:
        user = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
    
    computer = random.choice(choices)
    print("Computer chose : ", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or \
        (user == 'scissors' and computer == 'paper'):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score card\n You: {user_score}| Computer: {computer_score}\n")

print("Game Over!")
if user_score > computer_score:
    print("You won the game!")
elif computer_score > user_score:
    print("Computer won the game!")
else:
    print("The game is a tie!")
