# PEP8 Quick Reference Guide for Students
## Year 11 Software Engineering - Python Naming Conventions

---

## 📁 File Naming Rules

### ✅ DO THIS:
```
hangman.py
hangman_game.py
word_manager.py
game_logic.py
```

### ❌ DON'T DO THIS:
```
Hangman.py                    ❌ Capital letters
hangman-game.py               ❌ Hyphens
My File.py                    ❌ Spaces
My actual python file.py      ❌ Spaces and capitals
Hangman_game_project - Azmeer.py  ❌ Everything wrong
test.py                       ❌ Not descriptive
legacy_hangman-3.py           ❌ Version numbers and hyphens
```

### 🎯 Golden Rules:
1. **All lowercase** - no capital letters
2. **Use underscores** (`_`) to separate words
3. **No spaces** - they break imports and scripts
4. **No hyphens** (`-`) - Python thinks it's subtraction
5. **Be descriptive** - name should explain what the file does
6. **No version numbers** - use Git instead
7. **No personal names** - code is shared

---

## 📂 Folder Naming Rules

### ✅ DO THIS:
```
hangman_project/
game_assets/
word_lists/
templates/
```

### ❌ DON'T DO THIS:
```
hang asees/          ❌ Spaces
My Folder/           ❌ Spaces and capitals
Project-1/           ❌ Hyphens
```

---

## 🔤 Variable Naming Rules

### ✅ DO THIS:
```python
# Regular variables - lowercase with underscores
player_name = "Alice"
secret_word = "python"
guessed_letters = []
total_score = 100
is_game_over = False

# Constants - UPPERCASE with underscores
MAX_LIVES = 10
WORD_BANK_FILE = "words.csv"
DEFAULT_DIFFICULTY = "easy"
```

### ❌ DON'T DO THIS:
```python
PlayerName = "Alice"      ❌ Capital letters (looks like a class)
secretWord = "python"     ❌ camelCase (this is JavaScript style)
guessed-letters = []      ❌ Hyphens (syntax error!)
TOTAL_SCORE = 100         ❌ Not a constant, shouldn't be uppercase
```

---

## 🔧 Function Naming Rules

### ✅ DO THIS:
```python
def start_game():
    pass

def check_game_over():
    pass

def load_custom_words():
    pass

def add_word_to_csv():
    pass
```

### ❌ DON'T DO THIS:
```python
def StartGame():          ❌ Capital letters
def checkGameOver():      ❌ camelCase
def load-words():         ❌ Hyphens
def f():                  ❌ Not descriptive
```

---

## 📏 Line Length Rules

### ✅ DO THIS:
```python
# Break long lines into multiple lines
easy_words = [
    "apple", "pear", "kiwi", 
    "grape", "melon", "plum"
]

# Or use parentheses for natural line continuation
message = (
    "This is a very long message that "
    "spans multiple lines for better readability"
)
```

### ❌ DON'T DO THIS:
```python
# Line is way too long (should be max 79 characters)
easy_words = ["apple", "pear", "kiwi", "grape", "melon", "plum", "lime", "berry", "jazz", "fizz", "yoga", "wolf", "frog"]
```

---

## 💬 Comment Rules

### ✅ DO THIS:
```python
# This is a good comment with space after hash
x = 5  # Inline comment with 2 spaces before

# Multi-line comment explaining
# a complex section of code
# goes here
```

### ❌ DON'T DO THIS:
```python
#No space after hash
x = 5 #Only 1 space before inline comment

# Don't over-comment obvious things
x = 5  # This sets x to 5  ❌ (too obvious)
```

---

## 📦 Import Rules

### ✅ DO THIS:
```python
# Standard library imports first
import csv
import random
import time

# Blank line between groups
import flask

# Local imports last
import word_bank
import game_logic
```

### ❌ DON'T DO THIS:
```python
import random, time, csv  ❌ Multiple imports on one line
import word_bank
import random             ❌ Wrong order
```

---

## 🎨 String Formatting Rules

### ✅ DO THIS (Modern - f-strings):
```python
name = "Alice"
score = 100

# Use f-strings (Python 3.6+)
print(f"Welcome {name}!")
print(f"Your score is {score}")
```

### ⚠️ ACCEPTABLE (Older style):
```python
# .format() method
print("Welcome {}!".format(name))
```

### ❌ DON'T DO THIS (Outdated):
```python
# String concatenation - hard to read
print("Welcome " + name + "!")
print("Your score is " + str(score))
```

---

## 📐 Spacing Rules

### ✅ DO THIS:
```python
# 2 blank lines before top-level functions
def function_one():
    pass


def function_two():
    pass


# Spaces around operators
x = 5 + 3
y = x * 2

# No space inside brackets
my_list = [1, 2, 3]
my_dict = {"key": "value"}

# Space after comma
function(arg1, arg2, arg3)
```

### ❌ DON'T DO THIS:
```python
def function_one():
    pass
def function_two():    ❌ Only 1 blank line
    pass

x=5+3                  ❌ No spaces around operators
my_list = [ 1,2,3 ]    ❌ Spaces inside brackets, no space after comma
```

---

## 🚨 Why This Matters - Real Examples

### **Problem 1: Spaces in Filenames**
```bash
# Your file: "My actual python file.py"

# On Windows (might work):
python "My actual python file.py"

# On Linux/Mac (BREAKS):
python My actual python file.py
# Error: Can't find file "My" 

# In Git:
git add My actual python file.py
# Error: Unknown files "My", "actual", "python", "file.py"
```

### **Problem 2: Hyphens in Filenames**
```python
# Your file: hangman-game.py

# Try to import it:
import hangman-game
# SyntaxError: invalid syntax
# Python thinks: hangman minus game
```

### **Problem 3: Non-Descriptive Names**
```
Your project folder:
├── test.py          ❌ What does this test?
├── file.py          ❌ What's in this file?
├── new.py           ❌ New what?
└── final.py         ❌ Final version of what?

# 6 months later, you have no idea what anything does!
```

### **Problem 4: Automated Tools Fail**
```bash
$ pylint "Hangman_game_project - Azmeer.py"
************* Module Hangman_game_project - Azmeer
Hangman_game_project - Azmeer.py:1:0: C0103: Invalid module name
"Hangman_game_project - Azmeer" (invalid-name)

BUILD FAILED - Code does not meet standards
```

---

## ✅ Before You Submit - Checklist

### File Names:
- [ ] All lowercase?
- [ ] Uses underscores (not spaces or hyphens)?
- [ ] Descriptive name?
- [ ] No version numbers?
- [ ] No personal names?

### Folder Names:
- [ ] All lowercase?
- [ ] Uses underscores?
- [ ] No spaces?

### Code:
- [ ] Lines under 80 characters?
- [ ] 2 blank lines before functions?
- [ ] Proper spacing around operators?
- [ ] Comments have space after `#`?
- [ ] Using f-strings for formatting?

### Naming:
- [ ] Variables are lowercase_with_underscores?
- [ ] Constants are UPPERCASE_WITH_UNDERSCORES?
- [ ] Functions are lowercase_with_underscores?

---

## 🛠️ Tools to Help You

### In VS Code:
1. Install **Pylint** extension
2. Install **autopep8** extension
3. Enable format on save

### Check Your Code:
```bash
# Install checker
pip install pylint

# Check your file
pylint hangman.py

# Auto-fix formatting
pip install autopep8
autopep8 --in-place hangman.py
```

---

## 📚 Common Mistakes from Your Class

### Mistake #1: Spaces in File Names
**Students affected:** Azmeer, Sreyansh, Tareq

**Fix:**
```
Before: "My actual python file.py"
After:  "hangman_game.py"
```

### Mistake #2: Capital Letters in File Names
**Students affected:** Harshaan, Azmeer, Sreyansh, Tareq

**Fix:**
```
Before: "Hangman.py"
After:  "hangman.py"
```

### Mistake #3: Hyphens Instead of Underscores
**Students affected:** Johan, Shahil, Tareq

**Fix:**
```
Before: "legacy_hangman-3.py"
After:  "hangman.py"
```

### Mistake #4: Non-Descriptive Names
**Students affected:** Moksh, Sreyansh

**Fix:**
```
Before: "test.py"
After:  "hangman_game.py"
```

---

## 🎯 Quick Rename Guide

### Your Current File → Correct Name

| Current Name | Correct Name |
|--------------|--------------|
| `Hangman_game_project - Azmeer.py` | `hangman_game.py` |
| `Hangman.py` | `hangman.py` |
| `legacy_hangman-3.py` | `hangman.py` |
| `test.py` | `hangman_game.py` |
| `My actual python file.py` | `hangman_realtime.py` |
| `Tareqs Hangman Code-1.py` | `hangman.py` |

### Your Current Folder → Correct Name

| Current Name | Correct Name |
|--------------|--------------|
| `hang asees` | `hangman_web` |

---

## 💡 Pro Tips

1. **Use your IDE's rename function** - it updates all references automatically
2. **Set up a linter** - catch mistakes as you type
3. **Read error messages** - they often tell you what's wrong
4. **Ask "Would this work on Linux?"** - if not, fix it
5. **Think about your future self** - will you understand this in 6 months?

---

## 🌟 Remember

> "Code is read much more often than it is written."
> 
> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand."

Following PEP8 isn't about being picky - it's about being **professional**.

---

## 📖 Learn More

- **Official PEP8:** https://peps.python.org/pep-0008/
- **PEP8 Online Checker:** http://pep8online.com/
- **Real Python Tutorial:** https://realpython.com/python-pep8/

---

*Keep this guide handy for all your Python projects!*
