"""
4016. Maximum Area of Non-Overlapping Squares — DP (Optimal)
Link: https://leetcode.com/problems/maximum-area-of-two-non-overlapping-squares/
Difficulty: Medium
Time: O(m * n)   Space: O(m * n)
"""
from typing import List


class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        total_sum = sum([sum(i) for i in mat])
        matrix = mat
        if total_sum in (1, 0):
            return 0

        R, C = len(matrix), len(matrix[0])

        # endDp[i][j] = side length of largest all-1 square with bottom-right at (i, j)
        endDp = [[0] * C for _ in range(R)]
        maxSide = 0
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        endDp[i][j] = 1
                    else:
                        endDp[i][j] = 1 + min(
                            endDp[i - 1][j],
                            endDp[i][j - 1],
                            endDp[i - 1][j - 1]
                        )
                maxSide = max(maxSide, endDp[i][j])

        if maxSide == 0:
            return 0

        # bucket[k] holds all cells whose largest ending square has side k
        buckets = [[] for _ in range(maxSide + 1)]
        for i in range(R):
            for j in range(C):
                buckets[endDp[i][j]].append((i, j))

        max_i = max_j = float('-inf')
        min_i = min_j = float('inf')
        count = 0

        for k in range(maxSide, 0, -1):
            for i, j in buckets[k]:
                count += 1
                max_i = max(i, max_i)
                min_i = min(i, min_i)
                max_j = max(j, max_j)
                min_j = min(j, min_j)
                if count >= 2 and (max_i - min_i >= k or max_j - min_j >= k):
                    return k * k

        return 0
