# 239. Sliding Window Maximum

- **Link:** https://leetcode.com/problems/sliding-window-maximum/
- **Difficulty:** Hard
- **Topics:** Sliding Window, Deque, Monotonic Queue
- **Date solved:** 2026-08-09
- **Status:** ✅ Solved

## Problem
Given an array and window size k, return the max of each sliding window as it moves left to right.

## Approach
Monotonic decreasing deque storing **indices**. For each new element:
1. Evict indices that have fallen outside the window from the front.
2. Pop from the back any index whose value is ≤ current — they can never be the max while the current element is in the window.
3. Append current index.
4. Once the window is full (r ≥ k-1), the front of the deque is always the max.

## Complexity
- **Time:** O(n) — each index is pushed and popped at most once
- **Space:** O(k) — deque holds at most k indices

## Notes / Gotchas
-image.pngStore **indices**, not values — needed to check if the front has expired (`q[0] <= r - k`).
- The deque is monotonically decreasing in value, so `q[0]` is always the index of the current window max.
- Early return for k == 1 avoids edge case (window is always just the element itself).
