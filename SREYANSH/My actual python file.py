# ===== DATA STRUCTURES =====
# word_bank: Dictionary organizing words by difficulty level
# Difficulty 1 (Easy): 4-5 letter words, Difficulty 2 (Medium): 6-7 letter words, Difficulty 3 (Hard): 8+ letter words

import random
import time
import sys
import msvcrt

# ===== DATA STRUCTURES =====
# word_bank: Dictionary organizing words by difficulty level
# Difficulty 1 (Easy): 4-5 letter words, Difficulty 2 (Medium): 6-7 letter words, Difficulty 3 (Hard): 8+ letter words

word_bank = {
    "1": ["apple", "pear", "kiwi", "grape", "melon", "plum", "lime", "berry", "jazz", "fizz", "yoga", "paco", "wolf", "frog", "desk"],
    "2": ["banana", "orange", "cherry", "python", "galaxy", "planet", "bridge", "castle", "forest", "guitar", "laptop", "pigeon", "socket", "hammer", "window"],
    "3": ["javascript", "mountain", "rainforest", "tundra", "keyboard", "algorithm", "adventure", "dinosaur", "butterfly", "architect", "astronomy", "metropolis", "orchestra", "volcano", "pyramid"]
}

# categories: Maps each word to its theme category for display purposes
# Ensures every word in word_bank has a corresponding category for context
categories = {
    "apple": "Fruit", "pear": "Fruit", "kiwi": "Fruit", "grape": "Fruit", "melon": "Fruit",
    "plum": "Fruit", "lime": "Fruit", "berry": "Fruit", "jazz": "Music", "fizz": "Sound",
    "yoga": "Exercise", "paco": "Name", "wolf": "Animal", "frog": "Animal", "desk": "Furniture",
    "banana": "Fruit", "orange": "Fruit", "cherry": "Fruit", "python": "Coding", "galaxy": "Space",
    "planet": "Space", "bridge": "Structure", "castle": "Building", "forest": "Nature", "guitar": "Instrument",
    "laptop": "Tech", "pigeon": "Bird", "socket": "Tech", "hammer": "Tool", "window": "Home",
    "javascript": "Coding", "mountain": "Nature", "rainforest": "Nature", "tundra": "Nature", 
    "keyboard": "Tech", "algorithm": "Math", "adventure": "Action", "dinosaur": "History", 
    "butterfly": "Insect", "architect": "Job", "astronomy": "Science", "metropolis": "City",
    "orchestra": "Music", "volcano": "Nature", "pyramid": "History"
}

# ===== GAME INITIALIZATION =====
print("------ HANGMAN ------")
print("Type 'hint' during the game to reveal a letter (-20 pts)")

# choice: Player's difficulty selection (1, 2, or 3)
# score: Player's current score; starts differently based on difficulty (100 Easy, 70 Medium, 50 Hard)
choice = input("Select Difficulty (1(Easy), 2(Medium), or 3(Hard)): ")

if choice == "3": score = 50
elif choice == "2": score = 70
else: score = 100; choice = "1"

secret_word = random.choice(word_bank.get(choice, word_bank["1"]))
theme = categories.get(secret_word, "General")
display_word = ["_"] * len(secret_word)
guessed_letters = []
time_bank = 20.0 
current_input = ""

print(f"\nSTARTING GAME... THEME: {theme}")
time.sleep(1)

while "_" in display_word and score > 0 and time_bank > 0:
    start_loop = time.time()
    
    
    sys.stdout.write(f"\rSCORE: {score} | TIME: {round(time_bank, 1)}s | Word: {' '.join(display_word)} | Typing: {current_input}    ")
    sys.stdout.flush()

    if msvcrt.kbhit():
        char = msvcrt.getch() 
        
        try:
            char_decoded = char.decode('utf-8').lower()
        except:
            char_decoded = ""

        if char_decoded == '\r': 
            user_input = current_input.strip()
            current_input = ""
            print("\n")
            
           
            if user_input == "hint":
                if score >= 20:
                    score -= 20
                    hidden_indices = [i for i, c in enumerate(display_word) if c == "_"]
                    if hidden_indices:
                        idx = random.choice(hidden_indices)
                        letter = secret_word[idx]
                        for i, l in enumerate(secret_word):
                            if l == letter: display_word[i] = letter
                        print(f"HINT USED! Revealed '{letter.upper()}' | -20 Points")
                else:
                    print("NOT ENOUGH POINTS FOR A HINT!")
            
          
            elif user_input in secret_word and user_input != "" and user_input not in guessed_letters:
                for i, l in enumerate(secret_word):
                    if l == user_input: display_word[i] = user_input
                score += 10
                time_bank += 2.0
                print(f"CORRECT! '{user_input}' found. +2s")
                guessed_letters.append(user_input)
            else:
                score -= 10
                print(f"WRONG or ALREADY GUESSED! -10 Points")
                
        elif char_decoded == '\x08': 
            current_input = current_input[:-1]
        else:
            current_input += char_decoded

    time.sleep(0.05)
    end_loop = time.time()
    time_bank -= (end_loop - start_loop)


print("\n" + "="*30)
if "_" not in display_word:
    print("CONGRATULATIONS! YOU WON!")
else:
    print("GAME OVER! Better luck next time.")

print(f"THE WORD WAS: {secret_word.upper()}")
print(f"YOUR FINAL SCORE: {max(0, score)}")
print("="*30)