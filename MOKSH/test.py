import random
import csv  # Needed for CSV handling

# ask player for their name
name = input("Enter your name: ")
print("Welcome to the hangman game " + name )

# different word banks according to difficulty
easy_words = ("bear", "boar", "bull", "calf", "clam", "crow", "deer", "dove", "duck", "frog","goat", "hawk", "ibis", "kiwi", "lion", "lynx", "mole", "mule", "newt", "owl","oxen", "pike", "pony", "seal", "slug", "snail", "snake", "swan", "toad", "wolf","worm", "wren", "yak", "zebu", "bat", "bird", "crab", "eel", "fish", "gull","hare", "lamb", "lark", "mink", "orca", "puma", "tuna", "vole", "wasp", "beet")

medium_words = ("badger", "beaver", "bison", "bobcat", "buffalo", "canary", "cougar", "coyote", "donkey", "falcon","ferret", "gibbon", "gopher", "hermit", "heron", "jackal", "jaguar", "kitten", "lemur", "magpie","mantis", "meerkat", "monkey", "mullet", "ocelot", "oriole", "otter", "parrot", "pigeon", "python","rabbit", "salmon", "shrimp", "skunk", "spider", "squid", "turtle", "turkey", "walrus", "weasel","whale", "wombat", "woodpeck", "yakut", "zander")

hard_words = ("alligator", "anteater", "antelope", "armadillo", "baboonery", "butterfly", "caterpillar", "chimpanzee", "chinchilla", "cockroach","crocodile", "dragonfly", "elephant", "flamingo", "grasshopper", "hedgehoggy", "hippopotamus", "hummingbird", "jellyfish", "kangaroo","kingfisher", "kookaburra", "leopardess", "lobsterine", "mandrill", "mosquitoes", "nightingale", "orangutan", "porcupine", "raccoonish","rattlesnake", "reindeerish", "rhinoceros", "salamander", "scorpion", "seahorses", "sparrowhawk", "starling", "stingray", "swordfish","tarantula", "termiteking", "woodpecker", "wolverine", "yellowtail")

# Central game state
current_game_state = {
    "secret_word": "",     # word the player guess
    "guessed_letters": [], # shows the letters you guessed
    "score": 0,            # shows your score
    "wrong_guesses": 0     # shows number of wrong guesses
}

# CSV Function
# loads the CSV words into the pyton file game
def load_custom_words(file_name="custom_words.csv"):
    words = []
    try:
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)  # reads the CSV file
            for row in reader:
                if row:
                    words.append(row[0].strip().lower())
    except FileNotFoundError:
        print("Custom word file not found. Starting with an empty list.")
    return tuple(words) # Convert list to tuple before returning (prevents accidental changes)

# adds the words into the CSV while playing
def add_word_to_csv(new_word, file_name="custom_words.csv"):
    new_word = new_word.strip().lower() # removes any spaces and captal letters when the input is made
    with open(file_name, "a", newline="") as csvfile: # adds the new word within the csv file
        writer = csv.writer(csvfile)
        writer.writerow([new_word])
    print(f" '{new_word}' has been added to the custom word list!") # checks if the word has been added

# 1: Set up the game
def start_game():
    # selects difficulty based on players input
    difficulty = input("Choose difficulty (easy, medium, hard, custom): ").lower()
    if difficulty == "easy":
        word_bank = easy_words
    elif difficulty == "medium":
        word_bank = medium_words
    elif difficulty == "hard": 
        word_bank = hard_words
    elif difficulty == "custom":
        add_more = input("Do you want to add a word to the custom list? (y/n): ").lower()
        if add_more == "y":
            new_word = input("Enter the word you want to add: ")
            add_word_to_csv(new_word)

        custom_words = load_custom_words()
        if not custom_words:
            print("Custom list is empty. Defaulting to easy words.")
            word_bank = easy_words
        else:
            word_bank = custom_words
    else:
        print("Invalid Input. Difficulty is easy.")
        word_bank = easy_words

    print("Hangman Game Starting")
    # randomly chooses a word from the word list
    chosen_word = random.choice(word_bank)

    current_game_state["secret_word"] = chosen_word
    current_game_state["guessed_letters"] = []
    current_game_state["score"] = 100
    current_game_state["wrong_guesses"] = 0

    print(f"System: Game Started. Secret word has {len(chosen_word)} letters.")
    print(f"Starting Score: {current_game_state['score']}")

# 2: Process one guess
def play_turn(letter):
    print(f"\n--- Player guesses: '{letter}' ---")

    secret = current_game_state["secret_word"]

    # player guesses full word
    if len(letter) > 1:
        if letter == secret:
            print(">> Correct! You guessed the whole word!")
            current_game_state["score"] += 50
            current_game_state["guessed_letters"] = list(secret)
        else:
            print(">> Wrong word guess! -30 points")
            current_game_state["score"] -= 40
            current_game_state["wrong_guesses"] += 1
        return
    # shows if you guessed the same letter
    if letter in current_game_state["guessed_letters"]:
        print(">> You already guessed that letter <<")
        return

    current_game_state["guessed_letters"].append(letter)
    # checks if players guessed correct
    if letter in secret:
        print(">> Correct Guess!")
        current_game_state["score"] += 10
    else:
        print(">> Incorrect!")
        current_game_state["score"] -= 10
        current_game_state["wrong_guesses"] += 1
        # when you guess the wrong letter more than three times it provides you with a hint
        if current_game_state["wrong_guesses"] % 3 == 0:
            give_hint()

# 3: Print display and check win/loss
def check_game_over():
    score = current_game_state["score"]
    secret = current_game_state["secret_word"]
    guesses = current_game_state["guessed_letters"]

    display_string = ""
    for char in secret:
        if char in guesses:
            display_string += char + " "
        else:
            display_string += "_ "

    print(f"Display: {display_string}")
    print("Guessed letters:", " ".join(current_game_state["guessed_letters"]))
    print(f"Score: {score}")
    # when player losses when it hits 0 points
    if score <= 0:
        print(">> GAME OVER: Your score reached 0.")
        print(f"The word was: {secret}")
        return True
    # when player wins when guessed the word
    if "_" not in display_string:
        print(">> YOU WIN: You guessed the word!")
        print(f"Final Score: {current_game_state['score']}")
        print("Game Over!")
        return True

    return False

# HINT FUNCTION
# gives a random letter in secret word as a hint
def give_hint():
    secret = current_game_state["secret_word"]
    guesses = current_game_state["guessed_letters"]

    # finds letter not guessed so it does not give the same letter as an hint
    remaining_letters = [char for char in secret if char not in guesses]

    if remaining_letters:
        hint_letter = random.choice(remaining_letters)
        print(f" HINT: The word contains the letter '{hint_letter}'")
    else:
        print(" No hints available, you already guessed all letters!")

# Main program loop
if __name__ == "__main__":
    play_again = True
    # loop for playing again
    while play_again:
        start_game()

        game_is_running = True

        while game_is_running:
            user_input = input("Enter a letter or word: ").lower()

            if not user_input.isalpha():
                print("Error: Invalid Input")
                continue

            play_turn(user_input)

            game_is_running = not check_game_over()
        # ask to play again
        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing! Goodbye!")
            play_again = False
            