# Key Findings: PEP8 Violations by Student
## Year 11 Software Engineering - Task 1 Submissions

---

## 📊 Overview

**Total Students:** 8  
**Students with File Naming Violations:** 7 (87.5%)  
**Students with Folder Naming Violations:** 1 (12.5%)  
**Students with Perfect Submissions:** 0 (0%)  
**Students with Perfect File Naming Only:** 1 (Blake) ✅

**Note:** Blake had perfect file naming but violated folder naming conventions by using `hang asees` (with spaces) for GitHub submission.

---

## 🚨 File Naming Violations

### **AZMEER**
**File:** `Hangman_game_project - Azmeer.py`

**Violations:**
- ❌ **Spaces in filename** (contains " - ")
- ❌ **Capital letters** (H in Hangman, A in Azmeer)
- ❌ **Hyphens** (should use underscores)
- ❌ **Personal name in filename** (Azmeer)
- ❌ **Non-standard format** (project name + author name)

**Should be:** `hangman_game.py`

---

### **BLAKE**
**File:** `hangman.py` ✅  
**Folder:** `hang asees` ❌

**File Violations:** NONE - Perfect! ✅

**Folder Violations:**
- ❌ **Spaces in folder name** (critical issue for GitHub/version control)
- ❌ **Non-descriptive/unclear name** ("asees" unclear meaning)
- ⚠️ **GitHub Impact:** This folder was pushed to GitHub with spaces, causing potential issues for:
  - Command-line operations (requires quotes)
  - Automated scripts and CI/CD pipelines
  - Cross-platform compatibility
  - Other developers cloning the repository

**Folder should be:** `hangman_web` or `hangman_flask_app`

**Note:** While file naming was perfect, the folder naming violation is actually **more serious** because it was committed to version control (GitHub), affecting anyone who clones or works with the repository.

---

### **HARSHAAN**
**File:** `Hangman.py`

**Violations:**
- ❌ **Capital letter** (H in Hangman)

**Should be:** `hangman.py`

**Additional Code Issues:**
- ⚠️ **Line length violations** (Lines 9-15: extremely long lists)
- ⚠️ **Excessive comments** (every line commented, reduces readability)

---

### **JOHAN**
**File:** `legacy_hangman-3.py`

**Violations:**
- ❌ **Hyphen instead of underscore** (between "hangman" and "3")
- ❌ **Version number in filename** (-3)
- ❌ **"Legacy" prefix** (suggests poor version control practices)

**Should be:** `hangman.py`

**Note:** Use Git for version control instead of filename versioning

---

### **MOKSH**
**File:** `test.py`

**Violations:**
- ❌ **Non-descriptive filename** (doesn't indicate it's a Hangman game)
- ❌ **Generic name** (could be any test file)

**Should be:** `hangman_game.py` or `hangman.py`

**Additional Code Issues:**
- ⚠️ **Extremely long lines** (Lines 9-13: 300+ characters)
- ⚠️ **Typo in comment** (Line 39: "captal" should be "capital")

---

### **SHAHIL**
**File:** `legacy_hangman-3.py`

**Violations:**
- ❌ **Hyphen instead of underscore** (between "hangman" and "3")
- ❌ **Version number in filename** (-3)
- ❌ **"Legacy" prefix** (suggests poor version control practices)

**Should be:** `hangman.py`

**Note:** Same issues as Johan - possibly shared/copied template

---

### **SREYANSH**
**File:** `My actual python file.py`

**Violations:**
- ❌ **Spaces in filename** (multiple spaces)
- ❌ **Capital letters** (M in My)
- ❌ **Non-descriptive name** ("actual python file" is vague)
- ❌ **Unprofessional naming** (sounds like a placeholder)

**Should be:** `hangman_realtime.py` (since it uses real-time input)

**Additional Code Issues:**
- ⚠️ **Duplicate comments** (Lines 1-3 identical to lines 10-12)
- ⚠️ **Multiple statements on one line** (Line 43-45)

---

### **TAREQ**
**File:** `Tareqs Hangman Code-1.py`

**Violations:**
- ❌ **Spaces in filename** (multiple spaces)
- ❌ **Capital letters** (T, H, C)
- ❌ **Possessive/personal name** (Tareqs)
- ❌ **Hyphen instead of underscore** (Code-1)
- ❌ **Version number in filename** (-1)

**Should be:** `hangman.py`

**Additional Files:**
- `word_bank.py` ✅ (correctly named)
- `custom_words.csv` ✅ (correctly named)

---

## 📁 Folder Naming Violations

### **BLAKE**
**Folder:** `hang asees`

**Violations:**
- ❌ **Space in folder name**
- ❌ **Unclear/non-descriptive name**

**Should be:** `hangman_web` or `hangman_flask_app`

---

## ✅ Code Quality Highlights

### **Students with Good Variable Naming:**
- ✅ **All students** used proper `lowercase_with_underscores` for variables

### **Students with Good Function Naming:**
- ✅ **All students** used proper `lowercase_with_underscores` for functions

### **Students with Good Constant Naming:**
- ✅ **Blake** - `WORD_BANK`, `DIFFICULTY`
- ✅ **Harshaan** - `CUSTOM_FILE`
- ✅ **Tareq** - `CSV_FILE`

### **Students with Good Import Organization:**
- ✅ **Most students** used separate lines for imports
- ✅ **Tareq** - properly imported local module (`word_bank`)

---

## 📋 Violation Summary Table

| Student | Spaces | Capitals | Hyphens | Version # | Non-descriptive | Personal Name | Folder Issues |
|---------|--------|----------|---------|-----------|-----------------|---------------|---------------|
| **AZMEER** | ✗ | ✗ | ✗ | - | - | ✗ | - |
| **BLAKE** | - | - | - | - | - | - | ✗ |
| **HARSHAAN** | - | ✗ | - | - | - | - | - |
| **JOHAN** | - | - | ✗ | ✗ | - | - | - |
| **MOKSH** | - | - | - | - | ✗ | - | - |
| **SHAHIL** | - | - | ✗ | ✗ | - | - | - |
| **SREYANSH** | ✗ | ✗ | - | - | ✗ | - | - |
| **TAREQ** | ✗ | ✗ | ✗ | ✗ | - | ✗ | - |

**Legend:** ✗ = Violation present, - = No violation

---

## 🎯 Most Common Violations

### **1. Capital Letters (4 students)**
- Azmeer, Harshaan, Sreyansh, Tareq

### **2. Spaces in Filenames (3 students)**
- Azmeer, Sreyansh, Tareq

### **3. Hyphens Instead of Underscores (3 students)**
- Azmeer, Johan, Shahil, Tareq

### **4. Version Numbers in Filenames (3 students)**
- Johan, Shahil, Tareq

### **5. Non-descriptive Names (2 students)**
- Moksh, Sreyansh

### **6. Personal Names in Filenames (2 students)**
- Azmeer, Tareq

---

## 🏆 Best Practices Observed

### **BLAKE - File Naming Champion (Partial)**
- Only student with perfect **file** naming: `hangman.py` ✅
- Demonstrates understanding of file naming conventions
- **However:** Folder naming violated standards (`hang asees` with spaces)
- **Critical issue:** Folder was committed to GitHub, amplifying the problem
- **Model to follow for files:** `hangman.py`
- **Needs improvement for folders:** Should be `hangman_web`

### **All Students - Internal Code Quality**
- Good variable naming conventions
- Good function naming conventions
- Functional, working code
- Creative implementations

---

## 📝 Required Actions by Student

### **Immediate Fixes Needed:**

1. **AZMEER:** Rename `Hangman_game_project - Azmeer.py` → `hangman_game.py`
2. **BLAKE:** Rename folder `hang asees` → `hangman_web`
3. **HARSHAAN:** Rename `Hangman.py` → `hangman.py`
4. **JOHAN:** Rename `legacy_hangman-3.py` → `hangman.py`
5. **MOKSH:** Rename `test.py` → `hangman_game.py`
6. **SHAHIL:** Rename `legacy_hangman-3.py` → `hangman.py`
7. **SREYANSH:** Rename `My actual python file.py` → `hangman_realtime.py`
8. **TAREQ:** Rename `Tareqs Hangman Code-1.py` → `hangman.py`

---

## 💡 Key Takeaways

### **What Went Well:**
- ✅ All students wrote functional code
- ✅ All students used proper variable naming
- ✅ All students used proper function naming
- ✅ Creative and diverse implementations
- ✅ Blake demonstrated understanding of file naming conventions

### **What Needs Improvement:**
- ❌ 87.5% of students violated file naming conventions
- ❌ 100% of students had at least one naming violation (file or folder)
- ❌ Common issues: spaces, capitals, hyphens, version numbers
- ❌ Lack of awareness about cross-platform compatibility
- ❌ No use of version control best practices (Git) - hence version numbers in filenames
- ⚠️ **Critical:** Blake's GitHub submission with folder spaces demonstrates how violations propagate in version control

### **Learning Opportunity:**
This is a **teaching moment**, not a failure. These violations are common among beginners and easily correctable. The important thing is to learn the standards now and apply them going forward. Blake's case shows that even when you get file naming right, folder naming matters too - especially when using GitHub.

---

## 🎓 Recommendations for Future Assignments

### **For Students:**
1. Always use `lowercase_with_underscores.py` for file names
2. Never use spaces, capitals, or hyphens in file/folder names
3. Use descriptive names that indicate purpose
4. Install a linter (Pylint) to catch issues early
5. Check the Quick Reference Guide before submitting

### **For Assessment:**
Consider adding a **Code Quality/Style** section to rubrics:
- File/folder naming: 10%
- PEP8 compliance: 10%
- Code readability: 10%
- **Total:** 30% of grade for professional standards

This incentivizes good practices from the start.

---

## 📚 Related Documents

- **GitHub repo:** https://github.com/Mr-Zamora/11se_task_1_submissions
- **Marking.md** - Breakdown of marks based on rubric and assessment notification requirements
- **PEP8_Analysis_Report.md** - Detailed analysis with examples
- **Student_Quick_Reference_Guide.md** - Quick lookup for correct conventions
- **Real_World_Consequences.md** - Why these standards matter

---

## 📘 PEP8 Documentation for Students

### What is PEP8?

PEP8 is Python's official style guide - it provides conventions for writing readable, consistent Python code. Following PEP8 makes your code easier to read, maintain, and collaborate on with others.

### Key PEP8 Rules for File Naming

#### ✅ DO Use:
- **Lowercase letters only:** `hangman.py`, `game_logic.py`, `word_bank.py`
- **Underscores for spaces:** `hangman_game.py`, `user_interface.py`
- **Descriptive names:** Names that clearly indicate what the file does
- **Short, meaningful names:** Avoid overly long filenames

#### ❌ DON'T Use:
- **Capital letters:** `Hangman.py`, `Game.py`, `MyFile.py`
- **Spaces:** `hangman game.py`, `my file.py`
- **Hyphens:** `hangman-game.py`, `my-file.py`
- **Version numbers:** `hangman-v1.py`, `game-2.py`
- **Personal names:** `johns_game.py`, `mary_hangman.py`
- **Non-descriptive names:** `test.py`, `file.py`, `code.py`

### PEP8 Rules for Folder Naming

#### ✅ DO Use:
- **Lowercase letters only:** `hangman`, `game_project`, `assets`
- **Underscores for spaces:** `hangman_game`, `user_interface`
- **Descriptive names:** Names that indicate folder contents
- **No spaces:** Critical for GitHub and cross-platform compatibility

#### ❌ DON'T Use:
- **Spaces:** `hangman game`, `my project` (breaks many tools)
- **Capital letters:** `Hangman`, `GameProject`
- **Hyphens:** `hangman-game`, `my-project`
- **Special characters:** `hangman@game`, `project#1`

### PEP8 Rules for Code

#### Variable Names:
- Use `lowercase_with_underscores`: `user_score`, `word_list`, `game_active`
- ✅ Good: `max_attempts`, `current_word`, `guessed_letters`
- ❌ Bad: `maxAttempts`, `currentWord`, `GuessedLetters`

#### Function Names:
- Use `lowercase_with_underscores`: `get_word()`, `check_guess()`, `display_progress()`
- ✅ Good: `load_word_bank()`, `validate_input()`, `update_display()`
- ❌ Bad: `getWord()`, `checkGuess()`, `UpdateDisplay()`

#### Constant Names:
- Use `UPPERCASE_WITH_UNDERSCORES`: `MAX_ATTEMPTS`, `WORD_BANK`, `DIFFICULTY_LEVELS`
- ✅ Good: `MAX_GUESSES`, `CSV_FILE_PATH`, `HINT_LIMIT`
- ❌ Bad: `maxGuesses`, `csvFilePath`, `hint_limit`

#### Import Organization:
- Import standard library first: `import random`, `import time`
- Import third-party libraries second: `import pandas`, `import flask`
- Import local modules third: `from word_bank import load_words`
- Each import on its own line

#### Line Length:
- Maximum 79 characters per line
- Break long lines using parentheses or backslashes
- ✅ Good:
  ```python
  word_list = load_words_from_csv(
      'custom_words.csv',
      min_length=4
  )
  ```
- ❌ Bad:
  ```python
  word_list = load_words_from_csv('custom_words.csv', min_length=4, max_length=10, difficulty='medium')
  ```

#### Whitespace:
- One space around operators: `x = 5`, `a + b`, `if x > 0:`
- No spaces inside function calls: `func(arg)`, not `func( arg )`
- Two blank lines between functions
- One blank line between logical sections

### Why PEP8 Matters

1. **Readability:** Consistent code is easier to read and understand
2. **Collaboration:** Teams can work together more effectively
3. **Professionalism:** Industry standard for Python development
4. **Tool Compatibility:** Many tools expect PEP8 compliance
5. **Career Skills:** Employers expect PEP8 knowledge

### Tools to Check PEP8 Compliance

#### Pylint:
```bash
pip install pylint
pylint your_file.py
```

#### Flake8:
```bash
pip install flake8
flake8 your_file.py
```

#### Black (Auto-formatter):
```bash
pip install black
black your_file.py
```

### Quick Checklist Before Submitting

- [ ] All filenames use lowercase letters only
- [ ] All filenames use underscores, not spaces or hyphens
- [ ] All folder names use lowercase letters only
- [ ] All folder names use underscores, not spaces
- [ ] Filenames are descriptive and indicate purpose
- [ ] No version numbers in filenames
- [ ] No personal names in filenames
- [ ] Variable names use lowercase_with_underscores
- [ ] Function names use lowercase_with_underscores
- [ ] Constants use UPPERCASE_WITH_UNDERSCORES
- [ ] Each import is on its own line
- [ ] Lines are under 79 characters
- [ ] Proper spacing around operators

### Common Mistakes to Avoid

1. **Using CamelCase in Python:** Python uses snake_case, not CamelCase
2. **Forgetting to run a linter:** Always check your code before submitting
3. **Using version numbers:** Use Git for version control, not filenames
4. **Adding personal names:** Code should be independent of the author
5. **Ignoring line length:** Long lines are hard to read on small screens

---

*Analysis Date: April 22, 2026*  
*Class: Year 11 Software Engineering 2026*  
*Assignment: Hangman Game - Task 1*
