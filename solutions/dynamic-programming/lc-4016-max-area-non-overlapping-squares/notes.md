# 4016. Maximum Area of Non-Overlapping Squares

- **Link:** https://leetcode.com/problems/maximum-area-of-two-non-overlapping-squares/
- **Difficulty:** Medium
- **Topics:** Dynamic Programming, Matrix, Prefix Sum
- **Date solved:** 2026-08-09
- **Status:** ✅ Solved

## Problem
Given a binary matrix, find the maximum k² such that two non-overlapping k×k all-1 submatrices exist.

---

## Solution 1 — Brute Force (`solution.py`)

**Time:** O(sqrt(S) · m · n · k² · m · n) &nbsp;&nbsp; **Space:** O(1)

For each k from maxK down, scan every cell as the top-left of the first square (O(mn)), validate it in O(k²), then scan every cell again for a non-overlapping second square (O(mn · k²)). Stop at the first k that works.

`maxK` is bounded by sqrt(total_sum) — you can't have a k×k all-1 square if the matrix doesn't have k² ones.

---

## Solution 2 — Brute Force + Memoization (`solution2.py`)

**Time:** O(sqrt(S/2) · m · n · k²) &nbsp;&nbsp; **Space:** O(m · n · k)

Two improvements over solution 1:
1. **Tighter maxK:** Since we need *two* non-overlapping squares, each can use at most half the total 1s, so `maxK = sqrt(total_sum / 2)`.
2. **Propagate cache on hit:** When a k×k all-1 square is confirmed, every smaller sub-square starting within it is also all-1 — mark all of them `True` in the cache so future calls skip the O(k²) scan.

Still the same nested-loop structure, but with far fewer full O(k²) checks in practice.

---

## Solution 3 — Prefix Sums (`solution3.py`)

**Time:** O(k_max · m · n) &nbsp;&nbsp; **Space:** O(m · n)

Key insight: precompute a 2D prefix sum so any rectangle sum is O(1):
```
prefix[i][j] = matrix[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
square_sum   = prefix[r2][c2] - prefix[r1-1][c2] - prefix[r2][c1-1] + prefix[r1-1][c1-1]
```
This reduces each `checkIfSquare` from O(k²) to O(1), cutting the overall complexity to O(k_max · mn).

To check non-overlap without a second O(mn) scan: maintain a running bounding box (min/max row and col) of all valid corners found so far. Two squares are guaranteed non-overlapping if their top-left corners differ by ≥ k in at least one axis.

---

## Solution 4 — DP Maximal Square + Buckets (Optimal) (`solution4.py`)

**Time:** O(m · n) &nbsp;&nbsp; **Space:** O(m · n)

Two ideas chained together:

**Step 1 — Maximal Square DP:**
`endDp[i][j]` = side length of the largest all-1 square with its bottom-right corner at (i, j).
```
endDp[i][j] = 1 + min(endDp[i-1][j], endDp[i][j-1], endDp[i-1][j-1])  if matrix[i][j] == 1
```
This is O(mn) and gives, for every cell, the largest square that *ends* there.

**Step 2 — Bucket by side length, sweep from largest:**
Group cells by their `endDp` value. Iterate k from `maxSide` down to 1. For each k, add cells from `buckets[k]` to a running bounding box. As soon as 2+ cells are accumulated and their bounding box spans ≥ k in any direction, those two cells are centers of non-overlapping k×k squares → return k².

Every cell is visited exactly once across all k values, so this pass is O(mn).

## Notes / Gotchas
- The bounding-box non-overlap check works because `endDp[i][j] = k` means the k×k square occupying rows `[i-k+1, i]` and cols `[j-k+1, j]`. Two such squares overlap only if both their row ranges AND col ranges overlap — so if the bounding box of two bottom-right corners already spans ≥ k in either dimension, they can't overlap.
- Early exit on `total_sum ≤ 1` avoids edge cases (can't have two 1×1 non-overlapping squares if there's only one 1).
