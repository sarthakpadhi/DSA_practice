# 115. Distinct Subsequences

- **Link:** https://leetcode.com/problems/distinct-subsequences/
- **Difficulty:** Hard
- **Topics:** Dynamic Programming, String
- **Date solved:** 2026-08-05
- **Status:** ✅ Solved

## Solutions

**solution.py** — top-down DFS with memoization. Correct but uses recursion stack (risk of stack overflow on large inputs).

**solution2.py** — bottom-up iterative DP. Same O(m*n) time/space but avoids the recursion stack entirely by filling the table from the end, making it more robust in practice.
