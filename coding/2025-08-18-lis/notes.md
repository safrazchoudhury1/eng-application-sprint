# Notes for Longest Increasing Subsequence (LIS) Problem

**Problem:** Given a list of integers, compute the length of the longest strictly increasing subsequence.

**Approach:**
- Use the patience sorting technique. Maintain a `tails` list where `tails[i]` holds the smallest possible tail of an increasing subsequence of length `i+1`.
- Iterate through each number in the input; for each number, use binary search to find its position in `tails` and update the list accordingly.

**Complexity:** `O(n \log n)` time for `n` numbers and `O(n)` space for the `tails` list.

**Tests (expected output):**
- Input: `10 9 2 5 3 7 101 18` → LIS length = `4` (subsequence `2, 3, 7, 101`).
- Input: `0 1 0 3 2 3` → LIS length = `4` (subsequence `0, 1, 2, 3`).

**What I learned:** The binary search and `tails` approach keeps the smallest possible tail for each subsequence length, ensuring efficient updates and an `O(n \log n)` runtime.
