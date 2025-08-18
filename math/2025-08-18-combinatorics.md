# 2025-08-18 — Combinatorics & Probability Problems

**Problem 1: Seating Arrangement**

Eight students (4 boys and 4 girls) sit around a circular table. In how many distinct seating arrangements can boys and girls alternate? Two arrangements are the same if everyone's neighbors match after rotation.

*Solution:* Fix one boy's seat to remove rotational symmetry. There are \(3!\) ways to arrange the remaining boys relative to him and \(4!\) ways to place the girls in the alternating seats. The total number of distinct arrangements is
\(3! \times 4! = 6 \times 24 = \mathbf{144}\).

*Why this works:* Fixing one seat removes equivalent rotations, and alternation forces the girls into the gaps between the boys, leaving only permutations of the remaining students.

**Problem 2: Grid Paths**

Consider a \(5\times5\) grid. You walk from the bottom-left corner to the top-right corner, moving only up or right. The cell in row three, column three (counting from the bottom-left) is blocked. How many distinct paths exist?

*Solution:* Without the block there are \(\binom{8}{4}=70\) paths from \((0,0)\) to \((4,4)\). Paths that pass through the blocked cell \((2,2)\) are counted as \(\binom{4}{2}\times\binom{4}{2}=36\). Subtracting gives \(70-36=\mathbf{34}\) valid paths.

*Why this works:* \(\binom{m+n}{m}\) counts lattice paths with \(m\) moves of one type and \(n\) of another. Subtracting those forced through the forbidden cell applies the inclusion–exclusion principle.

**Problem 3: Probability of Matching Birthdays**

In a class of 30 students, what is the probability that at least two share a birthday? Assume 365 equally likely days and independence.

*Solution:* Compute the complement where all birthdays are distinct:
\[
P(\text{no match}) = \frac{365}{365}\times\frac{364}{365}\times\cdots\times\frac{365-29}{365} \approx 0.2937.
\]
Therefore the probability of a match is
\[
P(\text{at least one match}) = 1 - 0.2937 = \mathbf{0.7063}.
\]

*Why this works:* It's easier to count distinct birthdays than matching ones. Multiplying decreasing possibilities treats selections without replacement, and subtracting from one yields the complement event.

**What I learned:** These problems illustrate circular permutations, lattice path counting with forbidden cells, and the complement rule in probability—core tools for efficient combinatorial reasoning.
