# 2497. Maximum Star Sum of a Graph

- **Link:** https://leetcode.com/problems/maximum-star-sum-of-a-graph/
- **Difficulty:** Medium
- **Topics:** Graph, Greedy, Sorting
- **Date solved:** 2026-08-08
- **Status:** ✅ Solved

## Problem
A star graph is a node and any subset of its neighbors. Find the maximum star sum (node value + sum of chosen neighbor values) across all nodes, picking at most k neighbors per node.

## Approach
Greedy. For each node, collect neighbors with positive values, sort descending, take top k. No need to consider negative neighbors — they can only reduce the sum. Check every node as the center and track the running max.

## Complexity
- **Time:** O(n + e·log e) — building adj list is O(e), sorting neighbors per node sums to O(e·log e) overall
- **Space:** O(n + e)

## Notes / Gotchas
- Only include neighbors with `vals[i] > 0` — negative values never help.
- A node with no edges is still a valid star (just itself), so initialising `maxSoFar = vals[0]` and iterating all nodes handles isolated nodes naturally.
