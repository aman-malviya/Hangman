import string
from words import choose_word
from images import IMAGES

def is_word_guessed(secret_word, letters_guessed):
    if secret_word==letters_guessed:
        return True
    return False



def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    letters_left = string.ascii_lowercase
    for letter in letters_guessed:
        if letter in letters_left:
            letters_left=letters_left.replace(letter, "")
    return letters_left

def print_image(image):
    print(IMAGES[image])

def isValid(character):
    if len(character)==1 and 'a'<=character<='z':
        return True
    return False


def hangman(secret_word):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    letters_guessed = []
    remaining_lives=8
    no_of_wrong_inputs=0

    while remaining_lives>0:
        print("You have "+str(remaining_lives)+" lives remaining.")
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))

        guess = input("Please guess a letter: ")
        letter = guess.lower()

        if not isValid(letter):
            print("INVALID INPUT, FUCK OFF!!")
            continue

        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
        else:
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            remaining_lives-=1
            no_of_wrong_inputs+=1
            print_image(no_of_wrong_inputs)
            letters_guessed.append(letter)
            print("")


secret_word = choose_word()
hangman(secret_word)