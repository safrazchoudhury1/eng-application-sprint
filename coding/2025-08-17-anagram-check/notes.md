**Problem:** Check if two strings are anagrams (ignoring spaces, punctuation, case).

**Approach:** Clean input (retain only alphanumeric characters and convert to lowercase). Use a frequency dictionary to count letters in the first string and decrement counts for the second. If all counts return to zero, the strings are anagrams.

**Tests:**
- Input:
  Listen
  Silent
  Expected: YES
- Input:
  School master
  The classroom
  Expected: YES
- Input:
  hello
  world
  Expected: NO

**Learned:** Normalizing input is crucial. Counting letter frequencies avoids sorting and handles arbitrary punctuation or spacing.
