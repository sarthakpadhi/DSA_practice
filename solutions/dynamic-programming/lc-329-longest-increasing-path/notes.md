# 329. Longest Increasing Path in a Matrix

- **Link:** https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
- **Difficulty:** Hard
- **Topics:** Dynamic Programming, DFS, Memoization, Graph
- **Date solved:** 2026-08-05
- **Status:** ✅ Solved

## Problem
Given an m×n integer matrix, return the length of the longest strictly increasing path.
You can move in 4 directions; no diagonal, no wrapping.

## Approach
DFS with memoization (top-down DP). From each cell, recurse into all 4 neighbors that
are strictly greater. Cache the result per cell — each cell is computed once, making
it O(m*n) despite looking like exponential DFS.

The key insight: because paths are strictly increasing, the graph is a DAG (no cycles),
so memoization is safe — you can never revisit a cell on the same path.

## Complexity
- **Time:** O(m * n) — each cell computed once
- **Space:** O(m * n) — memo + recursion stack

## Notes / Gotchas
- No cycles possible (strictly increasing), so no visited set needed.
- Could also do topological sort (Kahn's BFS) bottom-up, but memo DFS is cleaner.
