MAX_GUESSES = 10
CURRENT_PUZZLE = ''


def game_board(game_word):  # Returns amount of blank lines in the player word
    official_word = "_" * len(game_word)
    return official_word


def letter_check(letter, word, the_game):  # Checks to see whether the letter is in the secret word
    mapped_word = list(map(str, word.lower()))

    while True:
        if letter.lower() in word.lower():
            # Find out where the letter is in the string and replace "_" with the letter
            index_of_letter = mapped_word.index(letter)
            toast = list(map(str, the_game))
            toast.pop(index_of_letter)
            toast.insert(index_of_letter, letter)
            return toast
        else:
            return -1


print(f"Welcome to Hangman! You have {MAX_GUESSES} guesses before the game ends.")
secret_word = input("Please type the secret word to use: ")
print(f"The word is: {game_board(secret_word)}")


while True:
    playerTurn = 0
    guessed_letter = input("Please guess a letter: ")
    outcome = letter_check(guessed_letter.lower(), secret_word, game_board(secret_word))
    if MAX_GUESSES == 1:
        print('Game over man, game over!')
        break
    else:
        if outcome == -1:
            MAX_GUESSES -= 1
            print('Sorry, that letter is not in the word. Try again.')
            print(f'You have {MAX_GUESSES} left.')
        else:
            print(f"Nice! '{guessed_letter}' is in the word!")
            currentPuzzle = ''.join(map(str, outcome))
