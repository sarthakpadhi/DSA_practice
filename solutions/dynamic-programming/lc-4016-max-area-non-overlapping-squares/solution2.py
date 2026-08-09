"""
4016. Maximum Area of Non-Overlapping Squares — Brute Force + Memoization
Link: https://leetcode.com/problems/maximum-area-of-two-non-overlapping-squares/
Difficulty: Medium
Time: O(sqrt(S/2) * m * n * k^2)   Space: O(m * n * k)
"""
from typing import List


class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        total_sum = sum([sum(i) for i in mat])
        matrix = mat
        if total_sum in (1, 0):
            return 0

        dp = {}

        def checkIfSquare(idx, jdx, k):
            if (idx, jdx, k) in dp:
                return dp[(idx, jdx, k)]
            if idx + k - 1 >= len(matrix): return False
            if jdx + k - 1 >= len(matrix[0]): return False
            sm = 0
            for i in range(idx, idx + k):
                for j in range(jdx, jdx + k):
                    sm += mat[i][j]
            if sm == k * k:
                # propagate: any sub-square starting inside this one is also valid
                for ilx in range(idx, idx + k):
                    for jlx in range(jdx, jdx + k):
                        for k_ in range(1, k - max(ilx - idx, jlx - jdx) + 1):
                            dp[(ilx, jlx, k_)] = True
                return True
            return False

        maxK = min(int((total_sum / 2) ** 0.5), len(matrix), len(matrix[0]))
        for k in range(maxK, 0, -1):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] != 1:
                        continue
                    if checkIfSquare(i, j, k):
                        for i2 in range(len(matrix)):
                            for j2 in range(len(matrix[0])):
                                if (abs(i2 - i) < k) and (abs(j2 - j) < k):
                                    continue
                                if checkIfSquare(i2, j2, k):
                                    return k * k
        return 0
