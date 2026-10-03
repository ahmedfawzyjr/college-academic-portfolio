"""
Dynamic Programming Reference Implementations
0/1 Knapsack and Longest Common Subsequence (LCS).
"""

from typing import List, Tuple

def knapsack_01(weights: List[int], values: List[int], capacity: int) -> Tuple[int, List[int]]:
    """Solves 0/1 Knapsack, returns (max_value, chosen_indices)."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w = weights[i - 1]
        v = values[i - 1]
        for c in range(capacity + 1):
            if w <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - w] + v)
            else:
                dp[i][c] = dp[i - 1][c]

    # Reconstruct chosen items
    chosen = []
    curr_c = capacity
    for i in range(n, 0, -1):
        if dp[i][curr_c] != dp[i - 1][curr_c]:
            chosen.append(i - 1)
            curr_c -= weights[i - 1]

    chosen.reverse()
    return dp[n][capacity], chosen

def longest_common_subsequence(s1: str, s2: str) -> str:
    """Computes the Longest Common Subsequence string."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct LCS
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    result.reverse()
    return "".join(result)
