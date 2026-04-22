import random
from flask import Flask, render_template, request, session, redirect, url_for
import time

app = Flask(__name__)
app.secret_key = "12345bob" #key used to create the flask server change this for different server

WORD_BANK = "words.csv" # word bank with the words
DIFFICULTY = ["Easy", "Medium", "Hard"]


@app.route("/", methods=["GET", "POST"]) #This is the app/server route
def index():
    message = "" #this is the variable that allows you to send messages to the player to help them.

    # Initialise points ONCE before the session starts.
    if "points" not in session:
        session["points"] = 100

    # Restart Game
    if request.method == "POST" and "restart" in request.form: #if the request method is called in the html it will restart the page and all the variables.
        session.clear()
        session["points"] = 100
        return render_template("index.html", options=DIFFICULTY)

    # Get session data, initializes what the app/server can see
    chosen_word = session.get("chosen_word")
    guessed_letters = session.get("guessed_letters", [])
    difficulty = session.get("difficulty")

    # Select difficulty from the dropdown box in the html code "post" means if a user inputed something.
    if request.method == "POST" and "dropdown" in request.form:
        difficulty = request.form["dropdown"]
        session["difficulty"] = difficulty

        with open(WORD_BANK) as f: #this opens the difficulty
            words = f.read().lower().split()

        # Choose word length based on difficulty
        if difficulty == "Easy":
            length_range = (4, 5)
        elif difficulty == "Medium":
            length_range = (6, 7)
        else:  # Hard
            length_range = (8, 13)

        word_length = random.randint(*length_range)
        filtered = [w for w in words if len(w) == word_length] #Filters out the letters from words and checks if it is equal to the word_length
        chosen_word = random.choice(filtered if filtered else words)
        print(chosen_word)

        session["chosen_word"] = chosen_word
        session["guessed_letters"] = []
        session["start_time"] = time.time()
        session["time_limit"] = 60
        guessed_letters = []

    start_time = session.get("start_time")
    time_limit = session.get("time_limit", 0)

    # Handle guess

    if request.method == "POST" and "guess" in request.form:
        guess = request.form["guess"].lower().strip()

        # Make sure a word has been chosen first
        if not chosen_word:
            message = "Select a difficulty first!"
        else:
            #whole word guess

            if len(guess) == len(chosen_word) and guess.isalpha():
                if guess == chosen_word:
                    # Set the message and reveal the word
                    message = f"Congratulations! You guessed the word: {chosen_word}"
                    display_word = chosen_word  # Show the full word

                    # Mark the game as over instead of clearing the session immediately
                    session["game_over"] = True
                else:
                    message = "Wrong word guess!"
                    session["points"] -= 20

            # single letter guess
            elif len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    message = "You already guessed that letter."
                else:
                    guessed_letters.append(guess)
                    session["guessed_letters"] = guessed_letters #saves the guessed letters to a flask session

                    if guess in chosen_word:
                        session["points"] += 10
                    else:
                        session["points"] -= 10

                    # Automatically restart if points drop to 0 or below
                    if session["points"] <= 0:
                        # Reset all game-related session variables
                        session.clear()
                        session["points"] = 100  # re-initialize points

                        # Redirect to restart the game
                        return redirect(url_for("index"))

            # invalid guess
            else:
                message = "Enter ONE letter or guess the FULL word."


    if chosen_word and all(letter in guessed_letters for letter in chosen_word): #if all your guessed letters have all the same letters in chosen_word you win the game :)
        message = f"Congratulations! You guessed the word: {chosen_word}"
        session.clear()

    # Create word display
    if chosen_word:
        display_word = " ".join(
            letter if letter in guessed_letters else "_"  #for every correct letter inside of chosen_word put a underscore
            for letter in chosen_word # based off guessed_letters than set it as the letter else put a _
        )
    else:
        display_word = "" #otherwise the display word is set to its normal state.

    if session.get("game_over"):
        display_word = chosen_word  # Reveal full word

    if start_time:
        elapsed = time.time() - start_time
        remaining = int(time_limit - elapsed)
        if remaining < 0:
            remaining = 0
            session["start_time"] = time.time()  # current timestamp
            session["time_limit"] = 60 # sets the time limit of the timer back to 60
    else:
        remaining = 0

    return render_template("index.html", #this renders all the variables from python to html like a pathway to index.html
        options=DIFFICULTY,
        selected=difficulty,
        word_display=display_word,
        guessed_letters=guessed_letters,
        message=message,
        chosen_length=len(chosen_word) if chosen_word else 0,
        time_left=remaining,
        points=session.get("points", 100),
    )

if __name__ == "__main__":
    app.run(debug=True) #runs the code setting debug to true to be able to see error messages.
