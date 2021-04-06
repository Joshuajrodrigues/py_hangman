import random
from words import words
import string


def valid_gen(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = valid_gen(words)
    # print(word)
    word_letters = set(word)
    # fprint(word_letters)
    alphabet = set(string.ascii_uppercase)
    # print(alphabet)
    used_letters = set()
    lives = 6
    while len(word_letters) > 0 and lives != 0:
        print('You have:', lives, 'lives. You have used', ' '.join(used_letters))
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print(word_list)
        user_input = input('Guess a Letter :\n').upper()
        if user_input in alphabet-used_letters:  # the word that i just guessed is in the alphabet and not used yet
            used_letters.add(user_input)  # then add to used letters
            if user_input in word_letters:
                # and removed from word letters
                word_letters.remove(user_input)
            else:
                lives = lives-1

        elif user_input in used_letters:
            print("This letter has already been used")
        else:
            print("invalid Character. Plase Try Again.")
    if lives == 0:
        print(f"You Loose :(, the word was {word}")
    else:
        print(f"Congratulations ! the word was {word}, you guessed it !!")


hangman()
