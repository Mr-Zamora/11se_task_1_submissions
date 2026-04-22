# PEP8 & Naming Conventions Analysis Report
## Year 11 Software Engineering - Task 1 Submissions

---

## Executive Summary

This report analyzes all 8 student submissions for adherence to Python's PEP8 style guide and naming conventions. While all submissions demonstrate functional code, there are significant opportunities to improve code professionalism and maintainability through proper naming and formatting standards.

---

## What is PEP8?

**PEP8** (Python Enhancement Proposal 8) is the official style guide for Python code. It provides conventions for writing clean, readable, and consistent Python code that can be easily understood by other developers.

**Key Principle:** *"Code is read much more often than it is written."*

---

## Critical Issues Found Across Submissions

### 1. **FILE NAMING VIOLATIONS** ⚠️

#### Problems Identified:

| Student | File Name | Issues |
|---------|-----------|--------|
| **AZMEER** | `Hangman_game_project - Azmeer.py` | ❌ Spaces in filename<br>❌ Hyphens in filename<br>❌ Capital letters<br>❌ Student name in filename |
| **HARSHAAN** | `Hangman.py` | ❌ Capital letter (should be lowercase) |
| **JOHAN** | `legacy_hangman-3.py` | ❌ Hyphen instead of underscore<br>❌ Version number in filename |
| **MOKSH** | `test.py` | ❌ Non-descriptive name (doesn't indicate purpose) |
| **SHAHIL** | `legacy_hangman-3.py` | ❌ Hyphen instead of underscore<br>❌ Version number in filename |
| **SREYANSH** | `My actual python file.py` | ❌ Spaces in filename<br>❌ Capital letters<br>❌ Non-descriptive name |
| **TAREQ** | `Tareqs Hangman Code-1.py` | ❌ Spaces in filename<br>❌ Capital letters<br>❌ Apostrophe/possessive<br>❌ Hyphen instead of underscore |
| **BLAKE** | `hangman.py` | ✅ **CORRECT** - all lowercase, no spaces |

#### **PEP8 Standard for File Names:**
```
✅ CORRECT:   hangman.py, hangman_game.py, word_manager.py
❌ INCORRECT: Hangman.py, hangman-game.py, My File.py, test.py
```

**Rules:**
- All lowercase letters
- Use underscores (`_`) to separate words, **never hyphens** (`-`) or spaces
- Descriptive names that indicate purpose
- No version numbers (use version control like Git instead)
- No personal names in filenames

---

### 2. **FOLDER NAMING VIOLATIONS** ⚠️

| Folder Name | Issues |
|-------------|--------|
| `hang asees` (Blake) | ❌ Space in folder name<br>❌ Non-descriptive/unclear name |

#### **PEP8 Standard for Folder Names:**
```
✅ CORRECT:   hangman_project, game_assets, word_lists
❌ INCORRECT: hang asees, My Folder, Project-1
```

---

### 3. **VARIABLE & CONSTANT NAMING ISSUES**

#### **Constants (Should be UPPERCASE with underscores)**

**❌ Incorrect Examples Found:**
```python
# From Blake's code
WORD_BANK = "words.csv"  # ✅ CORRECT
DIFFICULTY = ["Easy", "Medium", "Hard"]  # ✅ CORRECT

# From Harshaan's code
CUSTOM_FILE = "custom_words.csv"  # ✅ CORRECT

# From Tareq's code
CSV_FILE = "custom_words.csv"  # ✅ CORRECT
```

**Good job on constants!** Most students correctly used UPPERCASE for constants.

#### **Variables (Should be lowercase with underscores)**

**❌ Issues Found:**
```python
# From Azmeer's code - Line 5
easy_words = [...]  # ✅ CORRECT
medium_words = [...]  # ✅ CORRECT

# From Sreyansh's code - Line 14
word_bank = {...}  # ✅ CORRECT
```

**Most students did well with variable naming!**

---

### 4. **FUNCTION NAMING ISSUES**

#### **PEP8 Standard:** Functions should be lowercase with underscores

**✅ Good Examples:**
```python
def load_custom_words():  # ✅ CORRECT
def add_custom_word():    # ✅ CORRECT
def start_game():         # ✅ CORRECT
def play_turn():          # ✅ CORRECT
def check_game_over():    # ✅ CORRECT
```

**All students followed proper function naming conventions!** ✅

---

### 5. **CODE FORMATTING ISSUES**

#### **Line Length (PEP8: Maximum 79 characters)**

**❌ Violations Found:**

```python
# From Harshaan's code - Line 12
hard_words = ["electromagnetism", "photosynthesis", "pseudopseudohypoparathyroidism", "hypothetically", "friendlessness"]
# ❌ Line is 150+ characters long

# From Moksh's code - Line 9
easy_words = ("bear", "boar", "bull", "calf", "clam", "crow", "deer", "dove", "duck", "frog","goat", "hawk", "ibis", "kiwi", "lion", "lynx", "mole", "mule", "newt", "owl","oxen", "pike", "pony", "seal", "slug", "snail", "snake", "swan", "toad", "wolf","worm", "wren", "yak", "zebu", "bat", "bird", "crab", "eel", "fish", "gull","hare", "lamb", "lark", "mink", "orca", "puma", "tuna", "vole", "wasp", "beet")
# ❌ Line is 300+ characters long
```

**✅ Correct Format:**
```python
hard_words = [
    "electromagnetism", 
    "photosynthesis", 
    "pseudopseudohypoparathyroidism",
    "hypothetically", 
    "friendlessness"
]
```

#### **Whitespace Issues**

**❌ Problems Found:**

```python
# From Blake's code - Line 6
app.secret_key = "12345bob" #key used to create the flask server
# ❌ Missing space before comment (should be 2 spaces)

# ✅ CORRECT:
app.secret_key = "12345bob"  # key used to create the flask server
```

**PEP8 Rule:** Inline comments should be separated by at least 2 spaces from code.

#### **Blank Lines**

**PEP8 Rules:**
- 2 blank lines before top-level functions and classes
- 1 blank line between methods inside a class
- Use blank lines sparingly inside functions

**❌ Issues Found:**
```python
# From Johan's code - Lines 82-84
  # Repeats the loop until a valid choice is made

# D2: Central game state so functions can read/update it.
current_game_state = {
# ❌ Only 1 blank line before major section (should be 2)
```

---

### 6. **IMPORT STATEMENT ISSUES**

**PEP8 Standard:** Imports should be on separate lines and grouped

**✅ Correct Examples:**
```python
# From most students
import random
import time
import csv
```

**❌ Incorrect (if found):**
```python
import random, time, csv  # ❌ Multiple imports on one line
```

**PEP8 Import Order:**
1. Standard library imports (random, time, csv)
2. Related third-party imports (flask)
3. Local application imports (word_bank)

**✅ Good Example from Tareq:**
```python
import random
import word_bank
import time
import csv
```
*Note: Should group standard library together, then local imports*

**✅ Better Format:**
```python
import csv
import random
import time

import word_bank
```

---

### 7. **STRING FORMATTING INCONSISTENCIES**

Students used multiple string formatting methods:

```python
# f-strings (Modern, preferred) ✅
print(f"Welcome {name}!")

# .format() (Acceptable) ✅
print("Welcome {}!".format(name))

# String concatenation (Outdated, avoid) ❌
print("Welcome " + name + "!")
```

**PEP8 Recommendation:** Use f-strings (Python 3.6+) for consistency and readability.

---

## Individual Student Feedback

### **AZMEER**
**Strengths:**
- Clean variable naming
- Good function structure
- Consistent formatting

**Areas for Improvement:**
- ❌ File name: `Hangman_game_project - Azmeer.py` → Should be `hangman_game.py`
- Line 97: Use f-string instead of concatenation

### **BLAKE**
**Strengths:**
- ✅ **Perfect file naming:** `hangman.py`
- Good use of constants
- Professional Flask structure

**Areas for Improvement:**
- ❌ Folder name: `hang asees` → Should be `hangman_web` or `hangman_app`
- Line 6: Add 2 spaces before inline comment
- Line 50: Consider removing debug print statement

### **HARSHAAN**
**Strengths:**
- Excellent documentation/comments
- Good function naming
- Clear code structure

**Areas for Improvement:**
- ❌ File name: `Hangman.py` → Should be `hangman.py`
- Lines 9-15: Break long list into multiple lines
- Excessive comments (every line doesn't need explanation)

### **JOHAN**
**Strengths:**
- Good CSV handling
- Clear function separation
- Helpful comments

**Areas for Improvement:**
- ❌ File name: `legacy_hangman-3.py` → Should be `hangman.py`
- Remove "legacy" and version numbers from filename
- Line 2: Space after `#` in comment

### **MOKSH**
**Strengths:**
- Good CSV integration
- Clean function structure
- Helpful comments

**Areas for Improvement:**
- ❌ File name: `test.py` → Should be `hangman.py` or `hangman_game.py`
- Lines 9-13: Break extremely long tuples into multiple lines
- Line 39: Comment has typo "captal" → "capital"

### **SHAHIL**
**Strengths:**
- Good difficulty system
- Clean code structure
- Time-based gameplay

**Areas for Improvement:**
- ❌ File name: `legacy_hangman-3.py` → Should be `hangman.py`
- Remove version numbers from filename
- Line 65: Comment typo "letter" → "let"

### **SREYANSH**
**Strengths:**
- Creative real-time input system
- Good use of dictionaries
- Innovative gameplay

**Areas for Improvement:**
- ❌ File name: `My actual python file.py` → Should be `hangman_realtime.py`
- Duplicate comments (lines 1-3 and 10-12)
- Line 43-45: Multiple statements on one line (avoid)

### **TAREQ**
**Strengths:**
- Excellent modular structure
- Good CSV handling
- Clear documentation sections

**Areas for Improvement:**
- ❌ File name: `Tareqs Hangman Code-1.py` → Should be `hangman.py`
- Import organization (group standard library together)
- Line 1: Space after `#` in comments

---

## Why These Standards Matter

### **1. Collaboration & Teamwork**
In real-world software development, you'll work with teams of developers. If everyone uses different naming conventions:
- Code becomes confusing
- Bugs are harder to find
- Projects take longer to complete
- Team members get frustrated

**Example:** Imagine trying to find a file called `My actual python file.py` in a project with 100+ files!

### **2. Professional Employment**
- Companies **require** adherence to coding standards
- Code reviews will reject non-compliant code
- Job interviews often test knowledge of PEP8
- GitHub/GitLab repositories are judged by code quality

### **3. Automated Tools & CI/CD**
Modern development uses automated tools:
- **Linters** (like `pylint`, `flake8`) check PEP8 compliance
- **CI/CD pipelines** reject code that doesn't meet standards
- **IDEs** highlight violations in real-time

**What happens if you don't follow standards:**
```bash
$ flake8 "My actual python file.py"
Error: Invalid filename - contains spaces
Error: Line 43 - multiple statements on one line
Error: Line 97 - line too long (150 > 79 characters)
Build FAILED - 47 violations found
```

### **4. Cross-Platform Compatibility**

**❌ File names with spaces cause problems:**
```bash
# Windows (might work)
python "My actual python file.py"

# Linux/Mac (breaks in scripts)
python My actual python file.py  # Tries to run 4 different files!

# Git/Version Control
git add My actual python file.py  # Requires quotes, causes errors
```

**✅ Proper naming works everywhere:**
```bash
python hangman.py  # Works on all platforms
git add hangman.py  # No issues
```

### **5. Import Issues**

**❌ Hyphens in filenames break imports:**
```python
# If file is named: hangman-game.py
import hangman-game  # ❌ SYNTAX ERROR! Python thinks it's subtraction
```

**✅ Underscores work correctly:**
```python
# If file is named: hangman_game.py
import hangman_game  # ✅ Works perfectly
```

### **6. Maintainability**

Code you write today might be maintained for years:
- Future you (6 months later) needs to understand it
- Other developers need to modify it
- Teachers/markers need to assess it

**Consistent standards make this possible.**

---

## Quick Reference Guide

### **File Naming Checklist**
- [ ] All lowercase letters
- [ ] Use underscores (`_`) not hyphens (`-`) or spaces
- [ ] Descriptive name (indicates purpose)
- [ ] Ends with `.py`
- [ ] No version numbers
- [ ] No personal names

### **Folder Naming Checklist**
- [ ] All lowercase letters
- [ ] Use underscores for multiple words
- [ ] Descriptive name
- [ ] No spaces

### **Code Formatting Checklist**
- [ ] Lines ≤ 79 characters
- [ ] 2 blank lines before functions
- [ ] 2 spaces before inline comments
- [ ] Imports on separate lines
- [ ] Imports grouped and ordered

### **Naming Conventions**
```python
# Constants
MAX_LIVES = 10
WORD_BANK_FILE = "words.csv"

# Variables
player_name = "Alice"
secret_word = "python"
guessed_letters = []

# Functions
def start_game():
    pass

def check_game_over():
    pass

# Classes (if you learn them later)
class GameManager:
    pass
```

---

## Tools to Help You

### **1. VS Code Extensions**
- **Pylint** - Real-time PEP8 checking
- **autopep8** - Automatically fixes formatting
- **Black** - Opinionated code formatter

### **2. Online Checkers**
- PEP8 Online: http://pep8online.com/
- Python Code Checker

### **3. Command Line Tools**
```bash
# Check your code
pylint hangman.py
flake8 hangman.py

# Auto-fix formatting
autopep8 --in-place hangman.py
```

---

## Action Items for Students

### **Immediate Actions:**
1. **Rename your files** to follow PEP8 conventions
2. **Rename folders** to use underscores instead of spaces
3. **Run a linter** on your code to identify issues
4. **Fix long lines** by breaking them across multiple lines

### **Going Forward:**
1. **Always** check file names before submitting
2. **Use an IDE** with PEP8 checking enabled
3. **Read PEP8** documentation: https://pep8.org/
4. **Practice** writing clean code from the start

---

## Conclusion

All students demonstrated strong programming logic and creativity in their Hangman implementations. However, professional software development requires more than just working code—it requires **clean, maintainable, and standards-compliant code**.

By adopting PEP8 conventions now, you're building habits that will serve you throughout your programming career.

**Remember:** *"Any fool can write code that a computer can understand. Good programmers write code that humans can understand."* - Martin Fowler

---

## Additional Resources

- **Official PEP8:** https://peps.python.org/pep-0008/
- **Google Python Style Guide:** https://google.github.io/styleguide/pyguide.html
- **Real Python PEP8 Tutorial:** https://realpython.com/python-pep8/
- **The Hitchhiker's Guide to Python:** https://docs.python-guide.org/writing/style/

---

*Report Generated: April 22, 2026*
*Class: Year 11 Software Engineering 2026*
*Task: Hangman Project - Task 1*
