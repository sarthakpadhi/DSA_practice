"""
4016. Maximum Area of Non-Overlapping Squares — Brute Force
Link: https://leetcode.com/problems/maximum-area-of-two-non-overlapping-squares/
Difficulty: Medium
Time: O(sqrt(S) * m * n * k^2 * m * n)   Space: O(1)
"""
from typing import List


class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        total_sum = sum([sum(i) for i in mat])
        matrix = mat
        if total_sum in (1, 0):
            return 0

        def checkIfSquare(idx, jdx, k):
            if idx + k - 1 >= len(matrix): return False
            if jdx + k - 1 >= len(matrix[0]): return False
            sm = 0
            for i in range(idx, idx + k):
                for j in range(jdx, jdx + k):
                    sm += mat[i][j]
            return sm == k * k

        maxK = int(total_sum ** 0.5)
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
