import random

# List of possible words for the game
words = ["apple", "banana", "cherry", "orange", "pear", "strawberry"]

# Function to choose a random word from the list
def chooseWord():
    return random.choice(words)

# Function to initialize the game
def initialize(word):
    # Create a list of underscores with the same length as the chosen word
    return ["_"] * len(word)

# Function to display the current state of the game
def display(state):
    print(" ".join(state))

# Function to update the state of the game with the player's guess
def updateState(word, state, guess):
    # Loop through each letter in the word
    for i in range(len(word)):
        # If the letter matches the player's guess, update the state
        if word[i] == guess:
            state[i] = guess
    return state

# Function to check if the player has won
def checkWin(state):
    return "_" not in state

# Function to play the game
def play():
    word = chooseWord()
    state = initialize(word)
    guesses = set()
    remainingGuesses = 6

    # Loop until the player wins or runs out of guesses
    while remainingGuesses > 0 and not checkWin(state):
        display(state)
        print("Guesses remaining: ", remainingGuesses)
        guess = input("Guess a letter: ").lower()

        # If the player has already guessed this letter, skip it
        if guess in guesses:
            print("You already guessed that letter. Try again.")
            continue

        guesses.add(guess)

        # If the player's guess is not in the word, decrement the remaining guesses
        if guess not in word:
            print("Wrong guess!")
            remainingGuesses -= 1
        else:
            print("Correct guess!")

        # Update the state with the player's guess
        state = updateState(word, state, guess)

    # Display the final state of the game
    display(state)

    # Display the game result
    if checkWin(state):
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost. The word was:", word)

# Call the play function to start the game
play()
