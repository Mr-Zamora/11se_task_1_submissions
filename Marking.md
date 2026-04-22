# DETAILED CODE RUBRIC REVIEW BY STUDENT

## Assignment Brief Requirements (for reference)
- Difficulty Levels: Easy (4–5), Medium (6–7), Hard (8+) — 5 marks
- Game Progress Display: Show guessed letters & word state — 5 marks
- Guessing Options: Single letters OR entire word — 5 marks
- Score System: Start 100pts, -10 incorrect, +10 correct, 0 if fail — 5 marks
- Additional Features: 2 required from list (Timer, Hints, CSV, AI API, Save Game, GUI) — 20 marks total

---

## 1. BLAKE FIEDLER

| Category | Status |
|----------|--------|
| Code Comments | ✅ Excellent |
| Difficulty Levels | ✅ Fully Implemented |
| Game Progress Display | ✅ Flawless |
| Single Letter Guessing | ⚠️ Minor Issue |
| Whole Word Guessing | ✅ Fully Functional |
| Scoring System | ⚠️ Bug |
| Additional Feature 1 (Timer) | ✅ Excellent |
| Additional Feature 2 (Flask GUI) | ⚠️ Minor Bug |

**Strengths:**
- Exceptional code comments—accurate and comprehensive
- All difficulty levels fully implemented
- Flawless game progress display
- Whole word guessing works perfectly
- Timer feature works well and follows brief
- Flask GUI implementation is very good

**Weaknesses:**
- Single letter guessing: Input only displays "Guess a letter" (inconsistent feedback)
- Scoring system: Score not displayed as 0 if word not guessed
- Flask GUI: Pop-up activates even if word correctly guessed when timer reaches 0

**Recommendation:** Fix the score display bug and refine Flask GUI timer logic to prevent false loss conditions.

---

## 2. JOHAN CLARENCE TULIAO

| Category | Status |
|----------|--------|
| Code Comments | ⚠️ Redundant |
| Difficulty Levels | ⚠️ Custom Added |
| Game Progress Display | ✅ Fully Functional |
| Single Letter Guessing | ✅ Works Correctly |
| Whole Word Guessing | ❌ Major Deviation |
| Scoring System | ❌ Major Deviation |
| Additional Feature 1 (CSV) | ⚠️ Validation Issues |
| Additional Feature 2 (Hint) | ⚠️ Input Validation |

**Strengths:**
- Game progress display fully functional
- Single letter guessing works correctly
- Excellent flowchart organization
- Mature development tracking

**Weaknesses:**
- **Whole Word Guessing: MAJOR DEVIATION** — Awards +50pts instead of +10, sets score to 0 on wrong guess (not per brief)
- **Scoring System: MAJOR DEVIATION** — Doesn't follow -10/+10 specification
- Code Comments: Redundant, grammar errors, indentation issues
- CSV Feature: No word length validation; allows infinite letters, single-letter words, gibberish
- Hint Feature: Doesn't validate hint choice; accepts any letter besides y/n
- Difficulty Levels: Added custom difficulty (not in brief)

**Recommendation:** **Revise scoring system to match brief exactly.** Remove custom difficulty level. Add validation to CSV and hint features.

---

## 3. SHAHIL SAMI

| Category | Status |
|----------|--------|
| Code Comments | ⚠️ Missing Sections |
| Difficulty Levels | ✅ Fully Implemented |
| Game Progress Display | ✅ Flawless |
| Single Letter Guessing | ✅ Works Correctly |
| Whole Word Guessing | ✅ Fully Functional |
| Scoring System | ✅ Correct |
| Additional Feature 1 (CSV/Word Bank) | ⚠️ Partial |
| Additional Feature 2 (Hint/Timer) | ✅ Excellent |

**Strengths:**
- Flawless core mechanics
- Dynamic progress displays with varied difficulty levels
- Robust scoring system—correct implementation
- Excellent reflection and logbook
- Both additional features work well
- Outstanding quiz mastery

**Weaknesses:**
- Code Comments: Missing critical comments for Timer, Whole word guess, Hint system details, and game over conditions
- CSV Feature: Partially implemented; no ability for players to add words

**Recommendation:** Add comprehensive code comments for all feature sections. Complete CSV implementation to allow player word additions.

---

## 4. HARSHAAN GREWAL

| Category | Status |
|----------|--------|
| Code Comments | ❌ Poor Quality |
| Difficulty Levels | ⚠️ Specification Error |
| Game Progress Display | ⚠️ Display Issues |
| Single Letter Guessing | ✅ Works Correctly |
| Whole Word Guessing | ✅ Works Correctly |
| Scoring System | ⚠️ Display Bug |
| Additional Feature 1 (CSV) | ⚠️ Design Issues |
| Additional Feature 2 (Hint) | ✅ Correct |

**Strengths:**
- Hint feature functions correctly
- CSV file works and append function works
- Single and whole word guessing work correctly
- Excellent programming fundamentals
- Outstanding quiz performance
- Brilliant additional feature integration

**Weaknesses:**
- **Code Comments: POOR QUALITY** — Focuses on "what" not "why"; inconsistent placement (before and after lines); missed important functional logic
- **Difficulty Levels:** Medium words are 8 letters (should be 6-7)
- **Game Progress Display:** Lacks linebreaks; terminal not refreshed (design flaw)
- **Scoring System:** Score of 0 not displayed
- **CSV Design Flaw:** Why aren't easy/medium/hard in CSV instead of hardcoded? Inconsistent capitalization

**Recommendation:** **Rewrite code comments to explain WHY, not just WHAT.** Fix difficulty level word lengths. Add terminal refresh and linebreaks to display. Fix score display bug. Consider refactoring CSV to include difficulty categories.

---

## 5. TAREQ RAHMAN

| Category | Status |
|----------|--------|
| Code Comments | ✅ Excellent |
| Difficulty Levels | ✅ Fully Implemented |
| Game Progress Display | ✅ Fully Functional |
| Single Letter Guessing | ✅ Works Correctly |
| Whole Word Guessing | ✅ Fully Functional |
| Scoring System | ⚠️ Display Bug |
| Additional Feature 1 (CSV) | ✅ Very Good |
| Additional Feature 2 (Timer) | ⚠️ Specification Issue |

**Strengths:**
- Comprehensive and well-documented code comments
- All difficulty levels fully implemented
- Flawless game progress display
- Both guessing options work perfectly
- Scoring mathematics correct (scales by 10)
- CSV and Hints work very well
- Highly advanced software engineering principles
- Two complex features seamlessly integrated

**Weaknesses:**
- **Scoring System:** Fails to display final score of 0 when player loses
- **Timer Feature:** Does NOT follow assessment brief—needed countdown for each turn (10 seconds per guess), not whole game (60 seconds total)

**Recommendation:** Fix score display bug. **Revise timer to be per-turn countdown (10 seconds per guess) instead of whole-game timer.**

---

## 6. MOKSH PATEL

| Category | Status |
|----------|--------|
| Code Comments | ⚠️ Incomplete |
| Difficulty Levels | ⚠️ Invalid Words |
| Game Progress Display | ✅ Fully Functional |
| Single Letter Guessing | ✅ Works Correctly |
| Whole Word Guessing | ✅ Works Correctly |
| Scoring System | ⚠️ Deviation |
| Additional Feature 1 (Hint) | ⚠️ Incomplete |
| Additional Feature 2 (Word Guessing) | ❌ Major Issues |

**Strengths:**
- Game progress display fully functional
- Single and whole word guessing work correctly
- Excellent quiz performance
- Highly detailed and logical flowchart

**Weaknesses:**
- **Code Comments: INCOMPLETE** — Good intent with numbered sections, but check_game_over() mostly unmarked; main loop sparse; spelling errors
- **Difficulty Levels:** Made-up words in hard and medium categories (not real words)
- **Scoring System:** Deductions/additions don't follow brief (-10/+10 specification)
- **Hint Feature:** Displays letter but doesn't add to guessed_letters, reveal in display, or indicate hint was given
- **Second Feature:** Accepts ANY input as valid word (empty strings, single letters, spaces); no duplicate checking

**Recommendation:** **Add comprehensive code comments explaining game logic.** Replace made-up words with real words matching length specs. Fix scoring to match -10/+10 brief. Complete hint implementation (add to guessed_letters, reveal in display). Add input validation to second feature.

---

## 7. AZMEER MUHAMMAD

| Category | Status |
|----------|--------|
| Code Comments | ⚠️ Surface Level |
| Difficulty Levels | ❌ Major Issues |
| Game Progress Display | ⚠️ Incomplete |
| Single Letter Guessing | ❌ Missing |
| Whole Word Guessing | ❌ Missing |
| Scoring System | ❌ Broken |
| Additional Feature 1 (Timer) | ❌ Wrong Implementation |
| Additional Feature 2 (Hint) | ⚠️ No Limits |

**Strengths:**
- Good code comments (explains what code does)
- Solid quiz performance
- Shows promise with two additional features

**Weaknesses (CRITICAL):**
- **Whole Word Guessing: MISSING ENTIRELY** — Not implemented
- **Difficulty Levels: MAJOR ISSUES** — Word lengths don't match spec; most "Medium" are 4-5 letters; most "Hard" are 6 letters
- **Game Progress Display:** ASCII art but NO display of previously guessed letters
- **Scoring System: BROKEN** — Players don't start with 100 points; score goes negative; doesn't score 0 on failure
- **Code Comments:** Explains "what" but never "why"; lacks meaningful purpose
- **Timer Feature:** NOT a countdown per-turn; made a hidden stopwatch with end-of-game bonus instead
- **Hint Feature:** No hint limit or message

**Recommendation:** **This submission requires significant revision.** Implement whole word guessing. Fix difficulty levels to match specifications. Fix scoring system to start at 100, deduct 10 for wrong, add 10 for correct, score 0 on failure. Add display of guessed letters. Rewrite timer as per-turn countdown. Add hint limits and messages. 

---

## 8. SREYANSH VELDANDI

| Category | Status |
|----------|--------|
| Code Comments | ⚠️ Incomplete |
| Difficulty Levels | ⚠️ Specification Issue |
| Game Progress Display | ✅ Flawless |
| Single Letter Guessing | ❌ Missing |
| Whole Word Guessing | ❌ Missing |
| Scoring System | ⚠️ Display Issues |
| Additional Feature 1 (Timer) | ✅ Perfect |
| Additional Feature 2 (Hint) | ✅ Perfect |

**Strengths:**
- Dynamic game progress display operates flawlessly
- Both additional features fully integrated and work perfectly
- Exceptional reflection and logbook
- Strong procedural programming
- Solid quiz performance

**Weaknesses:**
- **Whole Word Guessing: MISSING** — Not implemented
- **Code Comments:** Missing critical game loop comments; no comments on complex operations (lines 64+); no timer logic comments
- **Difficulty Levels:** Different starting scores for each level (specification issue)
- **Scoring System:** Score not always displayed as 0 if word not guessed; scores need to start at 100

**Recommendation:** **Implement whole word guessing feature.** Add comprehensive code comments for game loop and complex operations. Fix difficulty level scoring to be consistent. Fix score display to show 0 on loss.

---

## COMPARATIVE SUMMARY TABLE

| Student | Comments | Difficulty | Progress | Guessing | Scoring | Feature 1 | Feature 2 |
|---------|----------|------------|----------|----------|---------|-----------|-----------|
| Blake | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ⚠️ |
| Johan | ⚠️ | ⚠️ | ✅ | ❌ | ❌ | ⚠️ | ⚠️ |
| Shahil | ⚠️ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| Harshaan | ❌ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| Tareq | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ⚠️ |
| Moksh | ❌ | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ❌ |
| Azmeer | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ |
| Sreyansh | ❌ | ⚠️ | ✅ | ❌ | ❌ | ✅ | ✅ |

---

## KEY FINDINGS BY CATEGORY

### Code Comments Quality
- **Excellent:** Blake, Tareq
- **Good:** Johan, Shahil
- **Poor:** Harshaan, Sreyansh, Moksh
- **Issue:** Most students explain "what" not "why"; inconsistent placement
- **Recommendation:** Teach distinction between descriptive and explanatory comments

### Difficulty Levels Implementation
- **Perfect:** Shahil, Tareq
- **Issues:** Johan (custom added), Harshaan (wrong word lengths), Azmeer (major issues), Sreyansh (different starting scores)
- **Common Problem:** Word lengths don't match brief specs

### Game Progress Display
- **Perfect:** Blake, Shahil, Tareq, Moksh, Sreyansh
- **Issues:** Harshaan (no linebreaks), Azmeer (no guessed letters shown)
- **Strength:** Most students handle this well

### Guessing Options (Single Letter & Whole Word)
- **Perfect:** Shahil, Tareq
- **Major Issue:** 3 students missing whole word guessing entirely (Azmeer, Sreyansh, + partial issues in others)
- **Problem:** Johan has major deviation for whole word guesses

### Scoring System
- **Perfect:** Shahil
- **Issues:** 
  - Johan: Major deviation 
  - Blake, Harshaan, Tareq, Moksh: Display bug (not showing 0 on loss)
  - Azmeer: Completely broken 
  - Sreyansh: Display issues

### Additional Features
- **Excellent:** Blake (Timer), Shahil (Hint/Timer), Harshaan (Hint), Tareq (CSV), Sreyansh (Timer & Hint)
- **Issues:** Johan (CSV validation), Moksh (Hint incomplete, second feature broken), Azmeer (wrong timer implementation)

---

## PRIORITY ACTIONS FOR STUDENTS

| Student | Priority 1 | Priority 2 | Priority 3 |
|---------|-----------|-----------|-----------|
| Blake | Fix guessing feedback | Fix score display | Fix Flask timer logic |
| Johan | **Fix scoring system** | Add CSV validation | Fix hint validation |
| Shahil | Add code comments | Complete CSV | Minor refinements |
| Harshaan | **Rewrite code comments** | Fix difficulty levels | Fix display formatting |
| Tareq | Fix score display | **Fix timer to per-turn** | Minor refinements |
| Moksh | **Add code comments** | Replace fake words | Fix hint implementation |
| **Azmeer** | **Implement whole word guessing** | **Fix scoring system** | **Fix difficulty levels** |
| Sreyansh | **Implement whole word guessing** | Add code comments | Fix scoring display |