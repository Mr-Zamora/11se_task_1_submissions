import random #allows for randomised choices
import word_bank #Imports words to guess from
import time #Allows for time to be used (used for countdown)
import csv #Saves/Loads custom words



CSV_FILE = "custom_words.csv"  #File name (storing custom words)

#-------------- Initial Game Screen -----------------

print("Welcome to Hangman>>>>>>>>>") #Welcome
print("\n")
name = input("insert player name: ") #Gets player name
print("------------------------------")
print("\n")
print(f"Welcome {name}!, are you ready to play?") #Personalised welcome string asking if you want to play

ready = input("(Y/N): ").upper() #asks if player is ready to play

if ready == "Y":
    print("Great! Starting the game...") #If yes - starts game
else:
    print("Goodbye!") #If no - fully ends game
    exit() #Stops running code

# ---------------- CSV FUNCTIONS ----------------

def load_custom_words(): #Loads the words from CSV File
    try:
        with open(CSV_FILE, newline='') as f:
            reader = csv.reader(f)
            #Gets the first column from each row that isn't empty
            return [row[0] for row in reader if row]
    except FileNotFoundError:
        return []

#Append a new word to the CSV file and changes it to uppercase
def save_custom_word(word):
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([word.upper()])
    print(f"'{word.upper()}' added to your custom word list!")

#Promts the player to enter a custom word, only saves it if it contains letters ONLY
def add_custom_word():
    word = input("Enter a word to add to your custom list: ").strip()
    if word.isalpha():
        save_custom_word(word)
    else:
        print("Invalid word. Only letters allowed.")


# ---------------- DIFFICULTY ----------------

def choose_difficulty(): #Lets player choose their desired difficulty or custom mode
    while True:
        print("\nChoose a difficulty")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Custom (your word list)")
        print("5. Add a word to custom list")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            return word_bank.easy_words #Uses easy word list
        elif choice == "2":
            return word_bank.medium_words #Uses medium word list
        elif choice == "3":
            return word_bank.hard_words #Uses hard word list
        elif choice == "4":
            custom = load_custom_words()

            #Checks is the custom list is valid to play with
            if not custom:
                print("Your custom list is empty! Add some words first (option 5).")
            elif len(custom) < 3: #Makes sure words in custom list exceed 3 words before playing
                print("Add at least 3 words to your custom list before playing.")
            else:
                return custom
        elif choice == "5":
            add_custom_word() #Add word option
        else:
            print("Invalid input, try again.\n")


# ---------------- WORD SELECTION ----------------

#Randomly selects a word from the players chosen word list
def choose_word(word_list):
    word = random.choice(word_list)
    return word.upper() #converts word to uppercase


# ---------------- GAME LOGIC ----------------

def start_game(word):
    word_completion = "_" * len(word) #Word display showing if you have guessed correcly
    guessed = False                   #Game status if guessed or not
    guessed_letters = []              #Letters that have already been guessed by the player
    guessed_words = []                #Words that have already been guessed by the player
    points = 100                      #Starting points
    total_time = 60                   #Starting time given to guess the word fully
    start_time = time.time()          #Records start time
    hints_remaining = 3               #Amount of useable hints remaining

    print(f"\nYou have {points} points") #Displays to player how many points they have
    print(word_completion)               #Displays the word completion

    # Main loop
    while not guessed and points > 0:

        # Calculates remaining time
        time_remaining = total_time - int(time.time() - start_time)

        if time_remaining <= 0:
            print("\nSorry, TIME'S UP!")
            print("-- GAME OVER --")
            return

        #Players guess
        guess = input(
            f"\nTime Remaining: {time_remaining}s\n"
            f"Hints remaining: {hints_remaining}\n"
            f"Guess (or type 'hint'): "
        ).upper()

        # ---------------- HINT ----------------

        if guess == "HINT": #Checks if the player has asked for a hint
            if hints_remaining == 0:
                print("No hints remaining!")
            else:
                word_as_list = list(word_completion)

                #reveals first hidden letter and takes away 10 points and 1 hint
                for i in range(len(word)):
                    if word_as_list[i] == "_":
                        word_as_list[i] = word[i]
                        word_completion = "".join(word_as_list)
                        print("Hint used! Letter revealed:", word[i])
                        points -= 10
                        hints_remaining -= 1
                        break

        # ------------- SINGLE LETTER -------------
        elif len(guess) == 1 and guess.isalpha(): #checks if user has entered a single letter

            if guess in guessed_letters: #checks if the user has already guessed this letter
                print("You already guessed the letter", guess)

            # Takes away 10 points if the guess isn't in the word
            elif guess not in word:
                print(guess, "is not in the word")
                points -= 10
                guessed_letters.append(guess)

            #The only other outcome is a correct guess (adds 10 points)
            else:
                print("Good job,", guess, "is in the word!")
                points += 10
                guessed_letters.append(guess)

                #Updates the word display with the correct guessed letter or letters
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]

                for index in indices:
                    word_as_list[index] = guess

                word_completion = "".join(word_as_list)

                #Checks if the player has guessed the entire word (Win condition)
                if "_" not in word_completion:
                    guessed = True

        # ------------- FULL WORD GUESS -------------
        elif len(guess) == len(word) and guess.isalpha(): #Checks if the user has entered an entire word

            if guess in guessed_words: #Checks if the user has already guessed this word
                print("You already guessed", guess)

            elif guess != word: #Takes away 10 points if the guess isn't the word
                print(guess, "is not the word")
                points -= 10
                guessed_words.append(guess)

            #Else the word was guessed correctly and the game has been won
            else:
                guessed = True
                word_completion = word
        #Else the user typed somthing other than a word or letter so their input was invalid
        else:
            print("Invalid input")

        # ---------------- GAME STATE (OUTPUT) ----------------
        #The main display the user views whilst playing
        print("\n------------------------------------------------")

        #Shows the users guessed letters to the user
        print("Guessed Letters:", ", ".join(guessed_letters) if guessed_letters else "None")

        #Shows points left and word completion
        print(f"Points left: {points}")
        print(word_completion)

    # ---------------- GAME RESULT ----------------

    #If the player has fully guessed the word, print a win message with their score
    if guessed:
        print("\nYou guessed the word", word, "Congratulations!")
        print(f"You finished with {points} points!")

    #Otherwise, reveal the word and print game over
    elif points <= 0:
        print("\nSorry, you ran out of points. The word was", word)
        print("-- GAME OVER --")


# ---------------- MAIN ----------------

def main():
    #Welcomes player
    print("\nWelcome to Hangman! >>>>>")

    #Keeps running the game until player chooses to quit
    while True:
        word_list = choose_difficulty()
        word = choose_word(word_list)
        start_game(word)

        #Asks the player if they want to play again
        if input("\nPlay again? (Y/N): ").upper() != "Y":

            #Exits the loop if player says no
            print("Thanks for playing!")
            break

 #Runs the program
if __name__ == "__main__":
    main()