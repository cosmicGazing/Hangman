MAX_LIVES = 3


def letter_index_finder(mapped_game_word: list, letter: str):  # Locates index of correct letter
    index_bucket = []
    for each_letter in range(len(mapped_game_word)):
        if letter == mapped_game_word[each_letter]:
            index_bucket.append(each_letter)
    return index_bucket


def replace_underscore_with_letter(letter_index_list: list, letter: str):  # Replaces the '_' with a correct letter
    for each_correct_letter in letter_index_list:
        blank_board_list.pop(each_correct_letter)
        blank_board_list.insert(each_correct_letter, letter)
    return blank_board_list
    

player_word = input('Please type a word: ').upper()
spaces_index_storage = list()
guessed_letters = set()  # Bucket for player guessed letters
blank_board_string = '_' * len(player_word)
blank_board_list = list(map(str, blank_board_string))
mapped_player_word = list(map(str, player_word))

i = 0
for each in mapped_player_word:  # Will determine where the spaces are so that they can be put back into the puzzle
    if each == ' ':
        spaces_index_storage.append(i)
        i += 1
    else:
        i += 1
        continue

for each in spaces_index_storage:  # This replaces '_' with ' ' in the list so players can see the individual words.
    blank_board_list[each] = ' '


refilled_phrase_string = ''.join(map(str, blank_board_list))
print(f'The word, or phrase, is: {refilled_phrase_string}')
print(f'You have {MAX_LIVES} chances before you run out of guesses.')

while MAX_LIVES > 0:
    if '_' not in blank_board_list:
        print('YOU WIN!!! YOU\'VE SOLVED THE PUZZLE! HURRAY!')
        break
    else:
        player_letter_guess = input('Please guess a letter: ').upper()
        if player_letter_guess not in guessed_letters:  # Checks if the player has already guessed this letter
            guessed_letters.add(player_letter_guess)
            if player_letter_guess in player_word:
                print('Awesome! That letter is in the puzzle!')
                values = letter_index_finder(mapped_player_word, player_letter_guess)
                joined_str = replace_underscore_with_letter(values, player_letter_guess)
                print(''.join(joined_str))
            else:
                if MAX_LIVES > 1:
                    print('Sorry, that letter is not in the puzzle.')
                    MAX_LIVES -= 1
                    print(f'You have {MAX_LIVES} remaining!')
                elif MAX_LIVES == 1:  # Reason for 1 is due to this was their last attempt.
                    print('Sorry, you have run out of turns. Game over, man! Game over!')
                    break
        else:
            print(f"Sorry, you've already guessed {player_letter_guess}, try another letter.")
