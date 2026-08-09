"""
4016. Maximum Area of Non-Overlapping Squares — Prefix Sums
Link: https://leetcode.com/problems/maximum-area-of-two-non-overlapping-squares/
Difficulty: Medium
Time: O(k_max * m * n)   Space: O(m * n)
"""
from collections import defaultdict
from typing import List


class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        total_sum = sum([sum(i) for i in mat])
        matrix = mat
        if total_sum in (1, 0):
            return 0

        dp = defaultdict(int)
        for idx in range(len(matrix)):
            for jdx in range(len(matrix[0])):
                dp[(idx, jdx)] = (
                    matrix[idx][jdx]
                    + dp[(idx - 1, jdx)]
                    + dp[(idx, jdx - 1)]
                    - dp[(idx - 1, jdx - 1)]
                )

        def checkIfSquare(idx, jdx, k):
            if idx + k - 1 >= len(matrix): return False
            if jdx + k - 1 >= len(matrix[0]): return False
            return (
                dp[(idx + k - 1, jdx + k - 1)]
                - dp[(idx - 1, jdx + k - 1)]
                - dp[(idx + k - 1, jdx - 1)]
                + dp[(idx - 1, jdx - 1)]
            ) == k * k

        maxK = min(int((total_sum / 2) ** 0.5), len(matrix), len(matrix[0]))
        for k in range(maxK, 0, -1):
            corners = []
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if checkIfSquare(i, j, k):
                        corners.append((i, j))
                        i1 = max(c[0] for c in corners)
                        i2 = min(c[0] for c in corners)
                        j1 = max(c[1] for c in corners)
                        j2 = min(c[1] for c in corners)
                        if (i1 - i2 >= k) or (j1 - j2 >= k):
                            return k * k
        return 0
