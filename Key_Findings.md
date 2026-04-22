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

- **PEP8_Analysis_Report.md** - Detailed analysis with examples
- **Student_Quick_Reference_Guide.md** - Quick lookup for correct conventions
- **Real_World_Consequences.md** - Why these standards matter

---

*Analysis Date: April 22, 2026*  
*Class: Year 11 Software Engineering 2026*  
*Assignment: Hangman Game - Task 1*
