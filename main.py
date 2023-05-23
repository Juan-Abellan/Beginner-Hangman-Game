from random import randint
from stages import stages_, medal, logo, fuck_you
from hangman_words import word_list

still_playing = True
lives = 6

word_list_main = word_list
used_letters_list = []

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list_main[randint(0, len(word_list_main) - 1)]
mistery_list = ["_" for letter in chosen_word]
mistery_list_len1 = len(mistery_list)

print(F"""
--- TESTING 1 ---
 {chosen_word = }
--- TESTING 1 --------------------------------------------------------------------------------------------------------
""")

print(logo)
print(mistery_list)

while still_playing:
    letter_guess = input("Let's guess a letter\n").lower()

    for index in range(len(chosen_word)):
        if letter_guess == chosen_word[index]:
            mistery_list[index] = letter_guess

    if letter_guess in used_letters_list:
        print(f"{letter_guess} is already there!")

    # print(mistery_list)

    elif letter_guess not in chosen_word:
        lives -= 1
        print(stages_[lives])

        if lives == 0:
            still_playing = False
            print(f"Game Over you big loser! the word you were trying to guess was {chosen_word}")
            print(fuck_you)

    elif "_" not in mistery_list:
        print(medal)

    used_letters_list.append(letter_guess)
    print(mistery_list)

    print(f"""
--- Testing 2 ----
    {chosen_word = }
    {letter_guess = }
    {mistery_list = }
    {used_letters_list = }
    {mistery_list_len1 = }
    {lives = }
--- Testing 2 --------------------------------------------------------------------------------------------------------
""")
