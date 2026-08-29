# 4036. Maximum Valid Splits

- **Link:** https://leetcode.com/problems/maximum-valid-splits/
- **Difficulty:** Medium
- **Topics:** Math, Dynamic Programming, GCD
- **Date solved:** 2026-08-09
- **Status:** ✅ Solved

## Problem
Find the maximum number of valid split points in an array, where a split at index `idx` is valid if the GCD of the left subarray equals the GCD of the right subarray.

## Approach
Precompute `dp[i][j]` = GCD of `nums[i..j]` for all subranges in O(n²). Then for each possible "skip" index `s` (treat as if one element is excluded), count how many split points satisfy left GCD == right GCD, using `safe(i, j)` to handle empty ranges gracefully. Take the max count over all skip choices.

## Complexity
- **Time:** O(n³) — O(n²) to build dp, O(n²) for the main loop (n choices of s, n split points each)
- **Space:** O(n²) — dp table

## Notes / Gotchas
- `safe(i, j)` returns 0 when `i > j` (empty range) to avoid index errors.
- GCD with 0 is the number itself (`gcd(x, 0) = x`) so `math.gcd(safe(...), safe(...))` collapses correctly when one side is empty.
- The first pass (no skip) is handled separately before the skip loop.
