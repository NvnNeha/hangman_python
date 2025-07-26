from name import word_list
from hangman_ascii_art import stages
from replit import clear
import random

print(word_list)
level = len(stages) - 1
selected_word = random.choice(word_list)
print(selected_word)
display = ["_" for _ in selected_word]
print(display)
game_is_finished = False
while not game_is_finished:
    user_char = input("Choose Your Character: ").lower()
    clear()
    if user_char in display:
        print(f"You have already chosen '{user_char}' character.")

    for n in range(len(selected_word)):
        letter = selected_word[n]
        if letter == user_char:
            display[n] = user_char
    print(display)

    if user_char not in selected_word:
        print(f"You guessed '{user_char}' that is not in the word, you lose a life.")
        level -= 1
        if level == 0:
            game_is_finished = True
            print("You lose")

    if "_" not in display:
        game_is_finished = True
        print("you Win!")

    print(stages[level])
