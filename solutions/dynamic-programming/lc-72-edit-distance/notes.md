# 72. Edit Distance

- **Link:** https://leetcode.com/problems/edit-distance/
- **Difficulty:** Medium
- **Topics:** Dynamic Programming, String
- **Date solved:** 2026-08-09
- **Status:** ✅ Solved

## Problem
Given two strings, return the minimum number of insert / delete / replace operations to convert word1 into word2.

## Approach
Bottom-up 2D DP. `dp[(i, j)]` = min edits to convert `word1[i:]` to `word2[j:]`.
If characters match, no operation needed — carry over `dp[i+1][j+1]`.
Otherwise take the min of insert, delete, replace and add 1.

## Complexity
- **Time:** O(m * n)
- **Space:** O(m * n)

## Notes / Gotchas
- **Base case — empty suffix:** when one string is exhausted, the only option is to insert/delete all remaining characters of the other. So `dp[(N_1, j)] = N_2 - j` (insert the rest of word2) and `dp[(i, N_2)] = N_1 - i` (delete the rest of word1). Without seeding these, the inner loop has nothing to build from.
- The three transitions map to: `dp[(i, j+1)]` = insert, `dp[(i+1, j)]` = delete, `dp[(i+1, j+1)]` = replace.
