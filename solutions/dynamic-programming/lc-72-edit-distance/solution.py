"""
72. Edit Distance
Link: https://leetcode.com/problems/edit-distance/
Difficulty: Medium
Time: O(m*n)   Space: O(m*n)
"""
from collections import defaultdict


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0

        N_1, N_2 = len(word1), len(word2)
        dp = defaultdict(int)

        for j in range(N_2 + 1):
            dp[(N_1, j)] = N_2 - j
        for i in range(N_1 + 1):
            dp[(i, N_2)] = N_1 - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[(i, j)] = dp[(i + 1, j + 1)]
                else:
                    final = min(
                        dp[(i, j + 1)],    # insert a character in word1
                        dp[(i + 1, j)],    # delete a character in word1
                        dp[(i + 1, j + 1)] # replace
                    )
                    dp[(i, j)] = final + 1

        return dp[(0, 0)]
