import random
import time

# Opens the csv file to choose words from.
with open("hangman_real_words_min4.csv", "r") as file:
    word_bank = [line.strip() for line in file if line.strip()]

# D1: Words from the csv file to be placed into different word banks.
easy_word_bank = [w for w in word_bank if 4 <= len(w) <= 5]
medium_word_bank = [w for w in word_bank if 6 <= len(w) <= 7]
hard_word_bank = [w for w in word_bank if len(w) >= 8]

# D2: Central game state so functions can read/update it.
current_game_state = {
    "secret_word": "",
    "lives": 0, 
    "guessed_letters": [],
    "score": 100,
    "hints": 0,
    "lives_lost": 0,
    "time_limit": 0,
}

# 1.0 Set up the game by choosing a secret word and initializing lives, guesses, and difficulty.
def start_game():
    while True:
        difficulty = input("Choose Difficulty: (e) easy, (m) medium, (h) hard): ").lower()
        if difficulty == "easy" or difficulty == "e":
            word_bank = easy_word_bank
            lives = 20
            time_limit = 25
            break
        elif difficulty == "medium" or difficulty == "m":
            word_bank = medium_word_bank
            lives = 15
            time_limit = 20
            break
        elif difficulty == "hard" or difficulty == "h":
            word_bank = hard_word_bank
            lives = 10
            time_limit = 15
            break
        else:
            print("Error: Invalid Difficulty. Please choose 'e', 'm', or 'h'.\n")
            

    # Initialize the game state.
    print("\n---BEGINNING HANGMAN GAME---\n") 

    # Pick a random word from the word bank.
    chosen_word = random.choice(word_bank)
    
    # Reset game state with the chosen word.
    current_game_state["secret_word"] = chosen_word
    current_game_state["lives"] = lives
    current_game_state["guessed_letters"] = []
    current_game_state["score"] = 100 
    current_game_state["hints"] = 0
    current_game_state["lives_lost"] = 0
    current_game_state["time_limit"] = time_limit

    print(f"System: Game Started. Secret word has {len(chosen_word)} letters.")
    print(f"System: You have {lives} lives.")
    print("System: If you want to guess the whole word, you only have 1 chance.\n")
    time.sleep(2) #Pause to letter the player read the instructions before continuing.
    print(f"Starting Score: {current_game_state['score']}")

# 2.0 Process one guess.
def play_turn(letter):
    print(f"\n--- Player guesses: '{letter}' ---\n")

    # Prevents player from guessing the same letter multiple times.
    if letter in current_game_state["guessed_letters"]:
        print("You already guessed that letter, try again.")
        return
    
    # Record the guess so it shows up in future displays.
    current_game_state["guessed_letters"].append(letter)

    # Compare the guess to the secret word.
    secret = current_game_state["secret_word"]
    
    if letter in secret:
        print("Correct Guess!\n")
        # Correct guess adds 10 points and sets lives_lost to 0.
        current_game_state["score"] += 10
        print(f"Current Score: {current_game_state['score']}")
        current_game_state["lives_lost"] = 0
    else:
        print("Incorrect guess.\n")
        # Wrong guess costs a life, minuses 10 points, and adds 1 to lives_lost.
        current_game_state["lives"] -= 1
        current_game_state["score"] -= 10
        print(f"Current Score: {current_game_state['score']}")
        current_game_state["lives_lost"] += 1

# 3.0 Print the current display and decide if the game should end.
def check_game_over():
    lives = current_game_state["lives"]
    secret = current_game_state["secret_word"]
    guesses = current_game_state["guessed_letters"]
    print(f"Guessed Letters: {', '.join(sorted(guesses))}")

    # Offer a hint after 3 wrong guesses.
    if current_game_state["lives_lost"] >= 3:
        print("Do you want a hint? (yes/no)")
        choice = input().lower()
        if choice == "yes":
            secret = current_game_state["secret_word"]
            guesses = current_game_state["guessed_letters"]
            remaining_letters = [char for char in secret if char not in guesses]
            if remaining_letters:
                hint_letter = random.choice(remaining_letters)
                print(f"Hint: The word contains the letter '{hint_letter}'")
                current_game_state["guessed_letters"].append(hint_letter)
                current_game_state["hints"] += 1
                current_game_state["lives_lost"] = 0
            else:
                print("No more hints available.")
        elif choice == "no":
            current_game_state["lives_lost"] = 0
        else:
            print("Invalid choice. No hint will be given.")
            current_game_state["lives_lost"] = 0

    # Build what the player sees (e.g., "_ a _ _").
    display_string = ""
    for char in secret:
        if char in guesses:
            display_string += char + " "
        else:
            display_string += "_ "
    
    print(f"\nDisplay: {display_string}\n")
    print(f"Lives Left: {current_game_state['lives']}")

    # This function acts as the referee checking for Win/Loss states.
    if current_game_state["lives"] == 0:
        print("GAME OVER: You ran out of lives.")
        print(f"The word was: {secret}")
        return True
    elif current_game_state["score"] <= 0:
        print("GAME OVER: You ran out of points.")
        print(f"The word was: {secret}")
        return True
    elif "_" not in display_string:
        print("YOU WIN: You guessed the word!")
        return True
    return False

# Main control loop.
if __name__ == "__main__":
    while True:
        start_game()

        check_game_over()
        
        game_is_running = True
        
        while game_is_running:
            time_limit = current_game_state["time_limit"]
            print(f"\nYou have {time_limit} seconds to make a guess.\n")

            start_time = time.time()
            # Get one guess from the player.
            user_input = input("\nEnter a letter or guess the word: ").lower()
            end_time = time.time()

            if end_time - start_time > time_limit:
                print("Time is up! You took too long to guess.")
                current_game_state["lives"] -= 1
                current_game_state["score"] -= 10
                break
            
            # Validate the input.
            if not user_input.isalpha():
                print("Error: Invalid Input")
                continue

            # Whole word guess
            if len(user_input) > 1:
                if user_input == current_game_state["secret_word"]:
                    print("YOU WIN! You guessed the whole word!")
                else:
                    print("Incorrect word guess.")
                    print(f"The word was: {current_game_state['secret_word']}")
                break

            # Apply guess and then check whether the game has ended.
            play_turn(user_input)
            is_over = check_game_over()
            
            if is_over:
                game_is_running = False

        # Ask if the player wants to play again
        game_is_running = True
        while game_is_running:
            play_again = input("Play again? (y/n): ").lower()
            if play_again == "n":
                print("\nThanks for playing!\n")
                quit()
            elif play_again == "y":
                print("\n Starting New Game \n")
                break
            else:
                print("Invalid Input, please type yes (y) or no (n)\n")