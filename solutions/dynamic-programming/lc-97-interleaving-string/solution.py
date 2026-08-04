"""
97. Interleaving String
Link: https://leetcode.com/problems/interleaving-string/
Difficulty: Medium
Time: O(m*n)   Space: O(m*n)
"""
from collections import defaultdict


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = defaultdict(int)
        dp[(0, 0)] = 1

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == j == 0:
                    continue
                if i == 0:
                    dp[(i, j)] = int((dp[(i, j - 1)] and s2[j - 1] == s3[i + j - 1]))
                elif j == 0:
                    dp[(i, j)] = int((dp[(i - 1, j)] and s1[i - 1] == s3[i + j - 1]))
                else:
                    dp[(i, j)] = int(
                        (dp[(i - 1, j)] and s1[i - 1] == s3[i + j - 1])
                        or (dp[(i, j - 1)] and s2[j - 1] == s3[i + j - 1])
                    )

        return bool(dp[len(s1), len(s2)])


if __name__ == "__main__":
    s = Solution()
    assert s.isInterleave("aabcc", "dbbca", "aadbbcbcac") == True
    assert s.isInterleave("aabcc", "dbbca", "aadbbbaccc") == False
    assert s.isInterleave("", "", "") == True
    print("ok")
