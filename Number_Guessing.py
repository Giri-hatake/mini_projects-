import random


# using a function 
def game(from_user):
    system_guess = random.randint(0,from_user)
    guess=0

# To loop until correct guess is come
    while guess != system_guess:
        guess=int(input(f"The number between 0 and {from_user} \nTry Your Guessing number: "))
        if guess < system_guess:
            print("your guess is too low")
        elif guess > system_guess:
            print("your guess is too high")
        
    print("Hurray!you find it!!!")


game(int(input("Enter the limit: ")))
