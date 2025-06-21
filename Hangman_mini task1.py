import random

# List of challenging words
words = ['abarana','abayambakai','agalya','aishwarya','anushree','anandhi','dharshini','giridhar',\
         'guru sabarieshwaran','hariharan','jeevitha','manoshree','nandhini sri','priya','shreya','sruthisagar','vipraja']
    

# Track used words
used_words = set()

# lifeline allotment
stages = ["lives 4","lives 3","lives 2","lives 1"]

def choose_word():
    available_words = [word for word in words if word not in used_words]
    if not available_words:
        return None 
    word = random.choice(available_words)
    used_words.add(word)
    return word.lower()

def play_hangman():
    word = choose_word()
    if not word:
        print("All words have been used! Game over.")
        return False

    guessed = ["_"] * len(word)
    attempts = len(stages) - 1
    used_letters = set()

    print("\nWelcome to Hangman!")
    print("Guess the name ")
    
    while attempts > 0 and "_" in guessed:
        print(stages[len(stages) - 1 - attempts])
        print("Word: " + " ".join(guessed))
        print("Used letters:", " ".join(sorted(used_letters)))

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in used_letters:
            print("You already guessed that letter.")
            continue

        used_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("Correct!")
        else:
            attempts -= 1
            print("Wrong!")

    if "_" not in guessed:
        print("Congratulations! You guessed the word:", word)
    else:
        print(stages[len(stages) - 1 - attempts])
        print("Game over! The word was:", word)
    
    return True

# Main  loop
if __name__ == "__main__":
    while True:
        keep_playing = play_hangman()
        if not keep_playing:
            break
        again = input("Play another round? (y/n): ").lower()#changing into lower case form user input 
        if again != 'y':
            break
