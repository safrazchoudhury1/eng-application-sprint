"""Longest Common Subsequence (LCS) length finder.

Reads two strings from standard input and prints the length of their longest common subsequence.
If either string is empty, the result is zero.

Usage:
    python solution.py
    # then type two lines (strings) as input.
"""


def lcs_length(a: str, b: str) -> int:
    """Compute the length of the longest common subsequence between two strings."""
    n, m = len(a), len(b)
    # Create a (n+1) x (m+1) DP table initialized to zero.
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = (
                    dp[i][j + 1] if dp[i][j + 1] >= dp[i + 1][j] else dp[i + 1][j]
                )
    return dp[n][m]


if __name__ == "__main__":
    try:
        s1 = input().rstrip("\n")
        s2 = input().rstrip("\n")
    except EOFError:
        print(0)
    else:
        print(lcs_length(s1, s2))
