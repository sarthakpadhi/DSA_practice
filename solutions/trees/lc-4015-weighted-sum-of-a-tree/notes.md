# 4015. Weighted Sum of a Tree

- **Link:** https://leetcode.com/problems/weighted-sum-of-a-tree/
- **Difficulty:** Medium
- **Topics:** Tree, BFS, DFS
- **Date solved:** 2026-08-09
- **Status:** ✅ Solved

## Problem
Given a rooted tree (via parent array) and node values, return the weighted sum where each node's contribution is `(height - depth + 1) * nums[node]`. Root is at depth 1, so root gets weight = height and leaves get weight = 1.

## Approach
Two passes:
1. **DFS** to find the tree height (max depth from root to any leaf).
2. **BFS** from root, tracking each node's depth `d`. Accumulate `(height - d + 1) * nums[node]`.

## Complexity
- **Time:** O(n) — DFS visits each node once, BFS visits each node once
- **Space:** O(n) — adjacency list + queue

## Notes / Gotchas
- `parent[0] = -1` (or 0 pointing to itself) for the root — the loop builds `adjList[-1].append(0)` which is harmless since we start BFS from node 0.
- **solution2.py** swaps `list.pop(0)` (O(n) per call → O(n²) BFS) for `deque.popleft()` (O(1) → true O(n) BFS). Always prefer `deque` for queues in Python.
