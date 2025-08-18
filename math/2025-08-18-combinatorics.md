# 2025-08-18 — Combinatorics & Probability Problems

**Problem 1: Seating Arrangement**

Eight students (4 boys and 4 girls) must be seated around a circular table. In how many distinct seating arrangements can the boys and girls be seated alternately (boys and girls alternate seats)? Two arrangements are considered the same if everyone has the same neighbors up to rotation.

*Solution:* Fix one boy's seat to remove rotational symmetry. There are 3! ways to arrange the remaining three boys relative to him. Once the boys are placed, there are 4! ways to place the girls into the alternating seats. The total number of distinct arrangements is `(3! × 4!) = 6 × 24 = **144**`.

**Problem 2: Grid Paths**

Consider a 5×5 grid (5 rows and 5 columns). You need to walk from the bottom-left corner to the top-right corner. You can only move either one step up or one step right at a time. However, the cell in the third row and third column (counting from the bottom-left) is blocked and cannot be stepped on. How many distinct paths exist?

*Solution:* Without any block, the total number of paths from (0,0) to (4,4) with 4 upward moves and 4 rightward moves is `C(8,4) = 70`. The blocked cell is at (2,2) (two moves up and two moves right). Count the number of paths that pass through (2,2), then subtract them. The number of paths from start to (2,2) is `C(4,2) = 6` and from (2,2) to the end is `C(4,2) = 6`. The number of paths passing through (2,2) is `6 × 6 = 36`. Therefore, the number of valid paths is `70 – 36 = **34**`.

**Problem 3: Probability of Matching Birthdays**

In a class of 30 students, what is the probability that at least two students share the same birthday? Assume each of the 365 days of the year (ignoring leap years) is equally likely and independent for each student.

*Solution:* Compute the complement: the probability that all birthdays are distinct. For the first student there are 365 possible birthdays, for the second 364, then 363, and so on down to `365‑29` for the 30th student. The probability that all 30 birthdays are distinct is:

P(no match) = \(\frac{365}{365} \times \frac{364}{365} \times \cdots \times \frac{365-29}{365}\) 

\(\approx 0.2937\) (approx.). Therefore, the probability that at least two students share a birthday is:

P(at least one match) = `1 - 0.2937 = **0.7063**` (approximately 70.63%).

**What I learned:** These problems illustrate counting principles, permutations with restrictions (circular arrangements), inclusion–exclusion ideas (subtracting paths through a forbidden cell), and the complement rule in probability. Such techniques are foundational for solving combinatorial and probability problems efficiently.
