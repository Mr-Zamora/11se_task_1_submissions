import random
import time

# Word lists for each difficulty
easy_words = [
    "lion", "grade", "school",
    "quiz", "fizz", "buzz", "jinx", "fuzz", "jink",
    "haze", "hajj", "vex", "fox", "apex", "affix",
    "annex", "axel", "lax", "junk", "jazz", "razz",
    "zit", "zine", "zap", "zinc", "dizzy", "jiff",
    "quest", "quaff", "qualm", "query", "quip", "fly"
]

medium_words = [
    "laptop", "hangman", "computer",
    "buzzing", "zigzag", "lynx", "myth",
    "sync", "crypt", "glyph", "nymph",
    "slyly", "wryly", "tryst"
]

hard_words = [
    "assessment", "programming", "developer",
    "quietude", "coccyx", "sphynx", "rhythm",
    "flysch", "ghylls", "sylphs", "syzygy",
    "myrrh"
]

# Hangman drawing stages
hangman = [
"""
  -----
  |   |
      |
      |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
      |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
  |   |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
 /|   |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
 /|\\  |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
 /|\\  |
 /    |
      |
---------
""",
"""
  -----
  |   |
  O   |
 /|\\  |
 / \\  |
      |
---------
"""
]

# Ask user for username
username = input("Enter your username: ")
print("Welcome", username, "to Hangman!")

# Variable to track total score across games
total_score = 0

# Main game loop (allows replay)
while True:

    # Difficulty selection
    print("\nChoose Difficulty:")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard")

    choice = input("Enter 1, 2, or 3: ")

    # Assign word list and score multiplier
    if choice == "1":
        words = easy_words
        difficulty_multiplier = 1
    elif choice == "2":
        words = medium_words
        difficulty_multiplier = 2
    else:
        words = hard_words
        difficulty_multiplier = 3

    # Randomly choose a word
    word = random.choice(words)

    # Create blank spaces for guessed letters
    guessed = ["_"] * len(word)

    # Set number of incorrect tries allowed
    tries = 6

    # Score for this round
    round_score = 0

    # Start timer
    start_time = time.time()

    print("\nType 'hint' to reveal a letter (costs 1 try)")

    # Game loop for guessing letters
    while tries > 0 and "_" in guessed:
        print(hangman[6 - tries])
        print("\nWord:", " ".join(guessed))
        print("Tries left:", tries)
        print("Score:", total_score + round_score)

        # Get user guess
        guess = input("Guess a letter or type hint: ").lower()

        # Hint system reveals one hidden letter
        if guess == "hint":
            for i in range(len(word)):
                if guessed[i] == "_":
                    guessed[i] = word[i]
                    tries -= 1
                    round_score -= 2
                    break
            continue

        # If guess is correct
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
                    round_score += 5 * difficulty_multiplier
            print("Correct!")
        else:
            # If guess is incorrect
            print("Wrong!")
            tries -= 1
            round_score -= 1

    # Stop timer
    end_time = time.time()
    time_taken = int(end_time - start_time)

    # Show final hangman stage
    print(hangman[6 - tries])

    # Check win or loss
    if "_" in guessed:
        print("\nYou lost,", username + "!")
        print("The word was:", word)        
    else:
        # Time bonus for faster completion
        time_bonus = max(0, 30 - time_taken)
        round_score += time_bonus
        print("\nCongratulations", username + "!")
        print("You won! The word was:", word)
        print("Time taken:", time_taken, "seconds")
        print("Time bonus:", time_bonus)

    # Add round score to total score
    total_score += round_score
    print("Total Score:", total_score)

    # Ask player if they want to play again
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Final Score:", total_score)
        print("Thanks for playing!")
        break