# 97. Interleaving String

- **Link:** https://leetcode.com/problems/interleaving-string/
- **Difficulty:** Medium
- **Topics:** Dynamic Programming, String
- **Date solved:** 2026-08-05
- **Status:** ✅ Solved

## Problem
Given s1, s2, s3 — check if s3 is formed by interleaving s1 and s2 (preserving relative order of each).

## Approach
2D DP where `dp[i][j]` = can we form `s3[:i+j]` using `s1[:i]` and `s2[:j]`.
Base case: `dp[0][0] = True`. For each cell, we can arrive from the left (used a char from s2)
or from above (used a char from s1) — take the OR of both valid paths.

## Complexity
- **Time:** O(m * n)
- **Space:** O(m * n) — reducible to O(n) with a 1D rolling array

## Notes / Gotchas
- Early exit if `len(s1) + len(s2) != len(s3)`.
- Index into s3 with `i + j - 1` (0-indexed), which equals the current combined length minus 1.
