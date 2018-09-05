# Create hangman game with python

# importing the time module
import time


def main():

    # global variables
    words = "math"
    guessed = '____'
    lives = 10

    # game introduction
    # welcome the user
    name = input("What is your name? ")

    print("Hello, " + name + "! It's time to play hangman!")

    # wait for 2 second to add suspense
    time.sleep(2)

    print("I am thinking of a word...")

    time.sleep(2)

    print("You have 10 lives... lets begin.")

    time.sleep(2)

    # begin game
    while True:

        guess = input("What is your guess? ")
        # method to verify input
        if not validate_input(guess):
            continue
        pass

        # if the user guesses correctly
        if guess in words:
            # method to update guessed letters
            guessed = update_guessed(guess, words, guessed)
            # show the user their progress
            print("You got a letter! Lets keep going.")
            print(guessed)
            # if the user won
            if guessed == words:
                time.sleep(2)
                print("Thats it! You've won!!")
                break
        # if they don't guess correctly
        else:
            lives -= 1
            # if they have no lives left
            if lives == 0:
                print("Sorry... You lose!!!")
                exit()
            # when they still have lives remaining
            else:
                print("Nope! You have " + str(lives) + " lives remaining.")
                time.sleep(1)
                print("Try again.")
        # the game will let the user read the final messages instead of closing
        # input("Press enter key to continue.")


def validate_input(guess):
    # if too many characters are entered
    if len(guess) > 1:
        print("You may only enter one letter at a time.")
        return False
    # if a number is pressed
    try:
        # this returns false if guess is an integer
        # convert back to string to return in output
        guess = str(int(guess))
        print(guess + " is not a letter. Only enter letters.")
        return False
    # input has been validated
    except ValueError:
        return True


def update_guessed(guess, words, guessed):
    characters = list(guessed)
    # search the secret word for the guessed character
    for index in range(len(words)):
        letter = words[index]
        # when you find the index of the guessed character
        if letter == guess:
            # store the correctly guessed characters so the user can view their progress
            characters[index] = letter
    return ''.join(characters)


if __name__ == '__main__':
    main()
