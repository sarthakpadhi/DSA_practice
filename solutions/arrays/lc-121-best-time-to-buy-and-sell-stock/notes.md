# 121. Best Time to Buy and Sell Stock

- **Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- **Difficulty:** Easy
- **Topics:** Array, Greedy
- **Date solved:** 2026-10-04
- **Status:** ✅ Solved

## Problem
Given daily stock prices, pick one day to buy and a later day to sell. Return the maximum profit, or 0 if no profit is possible.

## Approach
Scan left to right, tracking the lowest price seen so far. At each day, the best sale is that day's price minus the lowest earlier price. Keep the maximum of those differences.

## Complexity
- **Time:** O(n) — one pass
- **Space:** O(1)

## Notes / Gotchas
- `ans` starts at 0, so the answer is never negative when prices only fall.
- Buying and selling on the same day gives profit 0, which the `ans = 0` start already covers.
