# Notes on Longest Common Subsequence (LCS)

**Problem:** Given two strings, find the length of their longest common subsequence (LCS). A subsequence is an ordered sequence of characters that appears (not necessarily contiguously) in both strings.

**Approach:**
- Let `n = len(a)`, `m = len(b)`.
- Use dynamic programming: create a `(n+1) \times (m+1)` table `dp` where `dp[i][j]` is the LCS length for the prefixes `a[:i]` and `b[:j]`.
- Recurrence: if `a[i-1] == b[j-1]` then `dp[i][j] = dp[i-1][j-1] + 1`; otherwise `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

**Complexity:** `O(n*m)` time and `O(n*m)` space. For just the length, we could reduce space to `O(min(n, m))` using two rows.

**Manual tests:**

| String 1 | String 2 | Expected LCS length | Reason |
|---------|---------|--------------------|-------|
| `abcde` | `ace`    | `3`                | LCS is `ace`. |
| `AGGTAB` | `GXTXAYB` | `4` | LCS is `GTAB`. |
| `hello` | `world` | `1` | LCS is `o`. |

**What I learned:** The LCS problem illustrates overlapping subproblems and optimal substructure. A naive recursive solution would be exponential, but dynamic programming turns it into a polynomial-time algorithm. Optimising space is a typical improvement once the basic DP is understood.
