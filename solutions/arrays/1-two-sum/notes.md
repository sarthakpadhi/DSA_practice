# 1. Two Sum

- **Link:** https://leetcode.com/problems/two-sum/
- **Difficulty:** Easy
- **Topics:** Array, Hash Table
- **Date solved:** 2026-08-04
- **Status:** ✅ Solved

## Problem
Given an array and a target, return indices of the two numbers that add up to target.

## Approach
Brute force is O(n²) with two loops. The optimal trick: as you scan, store each
value's index in a hash map. For each number check if `target - n` was already seen.
One pass.

## Complexity
- **Time:** O(n)
- **Space:** O(n)

## Notes / Gotchas
- Store the number *after* checking, so you don't match an element with itself.
- Return order: the earlier index comes first naturally.
