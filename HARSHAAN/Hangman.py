import random
# random allows the program to randomly select items from a list.

# These lists store the possible secret words the player will guess.
easy_words = ["tree", "book", "game", "milk", "star"]
# Easy mode words are short and simple.
medium_words = ["computer", "elephant", "difficult", "hangman", "programming"]
# Medium words are longer and harder to guess.
hard_words = [
    "electromagnetism",
    "photosynthesis",
    "pseudopseudohypoparathyroidism",
    "hypothetically",
    "friendlessness"
]
# Hard words are very long or complex.
# Name of the file that stores custom words added by the player.
CUSTOM_FILE = "custom_words.csv"

# This dictionary stores the current game state.
current_game_state = {
    "secret_word": "",
    # The hidden word the player must guess.
    "guessed_letters": [],
    # A list storing every letter the player has guessed so far.
    "score": 100,
    # The player begins with 100 points.
    "hints_left": 2
    # The player can only use two hints per game.
}

# Function to load custom words from the CSV file.
# This allows players to add their own words and play with them later.
def load_custom_words():
    words = []
    # Create an empty list where custom words will be stored.

    with open(CUSTOM_FILE, "r") as file:
        # Open the custom word file in READ mode ("r").
        # The 'with' statement automatically closes the file afterwards.

        for line in file:
            # Loop through each line in the file.

            word = line.strip().lower()
            # strip() removes spaces and newline characters.
            # lower() converts the word to lowercase so comparisons are easier.

            if word:
                # If the line is not empty
                words.append(word)
                # Add the word to the list.

    return words
    # Return the full list of custom words.

# Function that allows the player to add their own word to the file.
def add_custom_word():
    new_word = input("Enter a new custom word: ").lower()
    # Ask the player for a new word and convert it to lowercase.

    if not new_word.isalpha():
        # isalpha() checks that the word contains only letters.
        # If numbers or symbols exist, the word is invalid.

        print("Invalid word. Letters only.")
        return
        # Stop the function and return to the menu.

    with open(CUSTOM_FILE, "a") as file:
        # Open the file in APPEND mode ("a").
        # Append means add new data without deleting existing data.

        file.write(new_word + "\n")
        # Write the new word to the file followed by a newline.

    print("Word added successfully!")
    # Inform the user the word was saved.

# Function that displays the difficulty menu and returns a chosen word.
def choose_difficulty():

    while True:
        # Loop forever until a valid choice is made.
        print("Choose Mode:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        print("4 - Add Custom Word")
        print("5 - Play From Custom List")

        choice = input("Enter option number: ")
        # Ask the user to select a menu option.

        if choice == "1":
            return random.choice(easy_words)
            # random.choice selects a random word from the easy word list.
        elif choice == "2":
            return random.choice(medium_words)
        elif choice == "3":
            return random.choice(hard_words)
        elif choice == "4":
            add_custom_word()
            # Call the function that adds a new custom word.
            # After adding, the menu will display again.

        elif choice == "5":
            return random.choice(load_custom_words())
            # Load the custom words and randomly select one.

        else:
            print("Invalid choice. Try again.")
            # If the user enters something incorrect.

# Function that displays the current progress of the game.
def display_progress():
    secret = current_game_state["secret_word"]
    # Get the secret word from the game state.

    guesses = current_game_state["guessed_letters"]
    # Get the list of guessed letters.

    display_word = ""
    # This string will visually show the progress of the guessed word.

    for letter in secret:
        # Loop through every letter in the secret word.
        if letter in guesses:
            # If the player has guessed this letter
            display_word += letter + " "
            # Show the actual letter.
        else:
            display_word += "_ "
            # Otherwise show an underscore.

    print("Word:", display_word)
    # Display the partially revealed word.
    print("Guessed Letters:", ", ".join(guesses))
    # Reveal and joins guessed letters

    print("Score:", current_game_state["score"])

    print("Hints Left:", current_game_state["hints_left"])

# Function that processes the player's input each turn.
def play_turn(user_input):

    secret = current_game_state["secret_word"]

    # ---- HINT SYSTEM ----
    if user_input == "hint":

        if current_game_state["hints_left"] <= 0:
            # If no hints remain

            print("No hints remaining!")
            return

        # Find the first letter not yet guessed
        for letter in secret:

            if letter not in current_game_state["guessed_letters"]:

                current_game_state["guessed_letters"].append(letter)
                # Automatically reveal that letter.

                current_game_state["score"] -= 10
                # Deduct 10 points for using a hint.

                current_game_state["hints_left"] -= 1
                # Reduce remaining hints.

                print("Hint used! Letter revealed:", letter)
                return

        return


    # ---- WORD GUESS ----

    if len(user_input) > 1:
        # If the player entered more than one letter,

        if user_input == secret:
            # If the guess is correct
            current_game_state["guessed_letters"] = list(secret)
            # Reveal all letters.

            current_game_state["score"] += 10

        else:
            print("Incorrect Guess! -10 points")

            current_game_state["score"] -= 10

        return


    # ---- SINGLE LETTER GUESS ----

    letter = user_input

    if letter in current_game_state["guessed_letters"]:
        # If the player already guessed this letter

        print("You already guessed that letter.")
        return

    current_game_state["guessed_letters"].append(letter)
    # Add the new guess to the list.
    if letter in secret:
        print("Correct Guess! +10 points")
        current_game_state["score"] += 10
    else:
        print("Incorrect Guess! -10 points")
        current_game_state["score"] -= 10

# Function that determines if the game has ended.
def check_game_over():

    secret = current_game_state["secret_word"]
    guesses = current_game_state["guessed_letters"]

    if current_game_state["score"] <= 0:
        # Player lost all points

        print("GAME OVER")
        print("You ran out of points!")
        print("The word was:", secret)

        return True

    if all(letter in guesses for letter in secret):
        # Check if every letter in the secret word has been guessed.
        print("YOU WIN!")
        print("Final Score:", current_game_state["score"])
        return True

    return False
    # Otherwise the game continues.

# Function asking the player if they want to play again.
def play_again():

    choice = input("Do you want to play again? (yes/no): ").lower()

    return choice == "yes"
    # This returns True if the player typed "yes".
    # Otherwise it returns False.

# The main program starts here.
if __name__ == "__main__":

    playing = True
    # This variable controls whether the entire game repeats.

    while playing:
        chosen_word = choose_difficulty()
        # Ask the player to choose difficulty and get a word.

        # Reset game state for a new game
        current_game_state["secret_word"] = chosen_word
        current_game_state["guessed_letters"] = []
        current_game_state["score"] = 100
        current_game_state["hints_left"] = 2

        print(f"\nThe word has {len(chosen_word)} letters.")
        # Tell the player how many letters are in the word
        print("You have 2 hints available (-10 points each).")

        game_running = True
        # Controls the gameplay loop.

        while game_running:
            display_progress()
            # Show the current game state.
            user_input = input("Enter a letter, word, or 'hint': ").lower()

            if not user_input.isalpha():
                # Ensure only letters are entered.
                print("Invalid input. Letters only.")
                continue
                # Skip the rest of this loop and restart.

            play_turn(user_input)
            # Process the player's guess.
            game_running = not check_game_over()
            # If the game is over, game_running becomes False.
        playing = play_again()
        # Ask if the user wants another game.
    print("Thanks for playing!")