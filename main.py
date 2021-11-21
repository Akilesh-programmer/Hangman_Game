# Importing the random module and the data from other files.
import random
import hangman_art as art
import hangman_words as words

# Choosing the random word from the data and calculating its length.
chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

# Creating a condition for end the while loop.
end_of_game = False

# Creating the lives for player.
lives = 6

# Printing an asci art logo
print(art.logo)

# Creating the blank list for storing the inputs and matching it with the actual word.
display = []

# Creating "_" equal to the number of letters present in the chosen word.
for _ in range(word_length):
    display += "_"

# Starting the game with while loop
while not end_of_game:

    # Getting the input from the user into lower case.
    guess = input("Guess a letter: ").lower()

    # Getting the user to know that they have entered the word which they already entered.
    if guess in display:
        print(f"You have already entered '{guess}', try another word.")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:

        if guess not in chosen_word:
            print(f"'{guess}' is not in the word, so you lose one point.")

        # Reducing the lives
        lives -= 1

        # Ending the game if the player lost all of his lives.
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Printing the asci art for each stage.
    print(art.stages[lives])
