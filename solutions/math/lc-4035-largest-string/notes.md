# 4035. Largest String

- **Link:** https://leetcode.com/problems/largest-string/
- **Difficulty:** Medium
- **Topics:** Bit Manipulation, String, Math
- **Date solved:** 2026-08-09
- **Status:** ✅ Solved

## Problem
Convert each integer to a string by mapping its set bits to characters: bit j → `chr('a' + j)` for j ≤ 25, or `'z' * 2^(j-25)` for higher bits.

## Approach
For each number, get its binary representation and reverse it to process LSB first (so bit position j is easy to index). For each set bit, produce the corresponding character(s), then reverse the collected characters to restore order.

## Complexity
- **Time:** O(n · b) — n numbers, each with up to b bits
- **Space:** O(n · b)
