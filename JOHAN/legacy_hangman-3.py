import random
import csv # For handling csv file

#Enter your name then outputs welcome to hangman (name)
name = input("Enter your name: ")
print(f"Welcome to hangman, {name}!")

# Function to save a word into my csv file
def add_to_csv():
    while True: # A loop until player makes a valid choice
        # Asks the player for a word to save into the csv
        new_word = input("Enter a custom word: ").lower()
    
        # Checks if the word is valid (letters only)
        if new_word.isalpha():
            # 'with open' opens the file, 'a' means append (add word to the end of the list)
            # 'newline=' makes the file not have empty gaps in-between words 
            with open('custom_words.csv', 'a', newline='') as file:
                writer = csv.writer(file) # This writes the new word into its own row in the Csv file. 
                writer.writerow([new_word])
            print(f">> '{new_word}' added to csv file")
            break # Word is valid and saved. exit loop
        else:
            print("Invalid word. Use letters only.")

# Function to get all words from csv file and randomly pick one word
def get_from_csv():
    words = [] # Create an empty list to store the words it finds
    try: # Try to open a file but doesn't crash if its missing
        # 'r' means to read the words in csv file 
        with open("custom_words.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader: # if the row isn't empty, add the word to list
                if row: 
                    words.append(row[0]) # looks at the row and takes out the word
        return words # Sends list of words back to difficulty function
    # 'except' prevents a crash if the file hasn't been created yet
    except FileNotFoundError:
        return[] # return an empty list if file is not found.

# Word bank of difficulty: easy, medium, hard
easy_words = ("happy", "angry", "book", "cool", "peel")
medium_words = ("master", "eating", "bowling", "father", "doodle")
hard_words = ("understandable", "psychologist", "grandmaster", "initialising", "hooligans")

# Its now its own function and the loop inside will repeat until a valid choice is chosen
# Returning a random word from the difficulty chosen back to the main control loop
def get_difficulty():
    while True:
        #.lower() automatically converts the players typing to lowercase, so that "Hard, HARD" still work. 
        difficulty = input("Choose Difficulty (easy / medium / hard / custom): ").lower()
         
        # If player chooses custom mode, they have an option to add a word to the csv file or just carry on with the game
        if difficulty == "custom": 
            add_choice = input("Would you like to add a custom word? (y/n): ").lower()

            # Only allows the player to type yes or no
            while add_choice not in ('y', 'n'):
                print("Invalid input. Type y or n.")
                add_choice = input("Would you like to add a custom word? (y/n): ").lower()

            # If they say yes, the code runs the add_to_csv function. 
            if add_choice == 'y':
                add_to_csv()
            
            options = get_from_csv() # Goes to the csv file and get all the words inside it. 

            if options: # If it finds a word in the csv, it selects a random word to start the game.
                return random.choice(options)
            else: # Prevents the game from crashing, if the csv file has no words in it.  
                print(">> Your custom list is empty! Add a word first.") 
                continue # To go back to the option of y/n

        elif difficulty == "easy":
            return random.choice(easy_words)
        elif difficulty == "medium":
            return random.choice(medium_words) 
        elif difficulty == "hard":
            return random.choice(hard_words) 
        else: 
            print("Invalid choice. Try again.")
  # Repeats the loop until a valid choice is made

# D2: Central game state so functions can read/update it.
current_game_state = {
    "secret_word": "",
    "score": 100, 
    "guessed_letters": [],
    "wrong_guesses": 0
}

# 1.0 Set up the game by choosing a secret word and initialising score and guesses.
def start_game():
    # Initialise the game state.
    print("--- PROCESS 1.0: Setting up D2 ---")
    
    # Shows your chosen secret word
    chosen_word = current_game_state["secret_word"]
    
    # Reset game state with the chosen word. Shows starting score and guessed letters list
    current_game_state["secret_word"] = chosen_word
    current_game_state["score"] = 100 
    current_game_state["guessed_letters"] = [] 
    current_game_state["wrong_guesses"] = 0
    # Shows the user how long the secret word is 
    print(f"System: Game Started. Secret word has {len(chosen_word)} letters.")

# 2.0 Process one guess.
def play_turn(letter):
    print(f"\n--- Player guesses: '{letter}' ---")
    
    # Grabs the secret word, so we can compare the guess made from the player. 
    secret_word = current_game_state["secret_word"]

    # Whole word guess 
    if len(letter) > 1: #If the player guess is more than one letter, it treats the guess as the whole word
        # Checks if the guessed word matches the secret_word. 
        if letter == secret_word: 
            print(">> Correct! You guessed the entire word!")
            current_game_state["score"] += 50 # Adds a 50 point bonus if you get the whole word correct.
            current_game_state["guessed_letters"] = list(secret_word)# Breaks the secret word into a list of letters to reveal them all at once
        else: 
            #If the whole word guess is wrong, the player loses the game and his points
            print(">> Incorrect! You lost all your points!")
            current_game_state["score"] = 0 
    
    # Single letter guess
    else:
       #Allows player to guess again if letter has already been said
       if letter in current_game_state["guessed_letters"]:
            print("You already guessed that letter")
            return
    
    # Record the guess so it shows up in future displays.
       current_game_state["guessed_letters"].append(letter)
    
       if letter in secret_word:
            print(">> Correct Guess! +10 points")
            current_game_state["score"] += 10 #score goes up by 10 points per correct guess
       else:
            print(">> Incorrect! -10 points")
        # Wrong guess costs loss of 10 points.
            current_game_state["score"] -= 10 #score goes down by 10 points per incorrect guess
            
            # Update the mistake counter
            current_game_state["wrong_guesses"] += 1
            wrong_count = current_game_state["wrong_guesses"]
            # Creates a list of letters that haven't been revealed yet. To send back a hint
            missing = [l for l in secret_word if l not in current_game_state["guessed_letters"]] 
        
            # Only provide a hint if there are letters left to find. 
            if missing: 
                # Automatically reveals a hint after 5 wrong guesses
                if wrong_count == 5: 
                    hint = random.choice(missing)
                    current_game_state["guessed_letters"].append(hint) # Add the hint letter to the list of guessed letters
                    print(f">> Hint: It looks like you were struggling! We've revealed letter {hint} for you.")

                # After 5 wrong guesses, it gives the player a choice if they want a hint or not
                elif wrong_count >5:
                    choice = input(">> Wrong guess again! Would you like another hint? (y/n): ").lower()
                    if choice == 'y':
                        hint = random.choice(missing)
                        current_game_state["guessed_letters"].append(hint)
                        print(f">> Hint: Here you go. The letter is '{hint}'.")
                    else: 
                        print(">> You don't want hint? okay then. Good Luck!")
                 
            

# 3.0 Print the current display and decide if the game should end.
def check_game_over():
    current_score = current_game_state["score"]
    secret = current_game_state["secret_word"]
    guesses = current_game_state["guessed_letters"]
    
    # Build what the player sees (e.g., "_ a _ _").
    display_string = ""
    for char in secret:
        if char in guesses:
            display_string += char + " "
        else:
            display_string += "_ "
            
    print(f"Display: {display_string}")
    print(f"Guessed letters: {', '.join(guesses)}")
    print(f"Current score: {current_score}") 

    # Win/loss conditions.
    if current_score == 0: # If score is 0 then you lose and it shows what the secret word was
        print(f">> GAME OVER: You reached 0 points. The word was '{secret}'.")
        return True 
    elif "_" not in display_string: # If there are no letters in underscore display left, You Win.
        print(f">> YOU WIN: You guessed the word! Final score: {current_score}!") 
        return True # Tells the main loop the game is over
        
    return False # Tells the main loop the game is not over yet

# Main control loop.
if __name__ == "__main__":
    word = get_difficulty()
    current_game_state["secret_word"] = word
    start_game()
    
    check_game_over()# displays the (_ _ _ _ _) at start of game
    
    game_is_running = True

    while game_is_running:
        #Gets the length of the secret word
        secret_len = len(current_game_state["secret_word"])
       
        # Gets a guess from the player.
        user_input = input(f"Enter a letter or the {secret_len}-letter word: ").lower()

        # Checks if a player guessed a letter and not symbols or numbers
        if not user_input.isalpha():
            print("Error: Letters only")
            continue
        
        # Only allows the guess to be 1 letter or secret word length
        if len(user_input) != 1 and len(user_input) != secret_len:
            print(f"Error: Guess 1 letter or {secret_len} letter word.")
            continue # Goes back to the while loop to ask again

        # Apply guess and then check whether the game has ended.
        play_turn(user_input)
        is_over = check_game_over()
        
        if is_over:
            game_is_running = False
