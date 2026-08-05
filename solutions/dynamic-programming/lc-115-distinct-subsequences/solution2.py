"""
115. Distinct Subsequences — bottom-up DP (no recursion stack)
Link: https://leetcode.com/problems/distinct-subsequences/
Difficulty: Hard
Time: O(m*n)   Space: O(m*n)
"""
from collections import defaultdict


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = defaultdict(int)

        for i in range(len(s) + 1):
            dp[(i, len(t))] = 1

        for j in range(len(t) - 1, -1, -1):
            for i in range(len(s) - 1, -1, -1):
                ans = 0
                if s[i] == t[j]:
                    ans += dp[(i + 1, j + 1)]
                ans += dp[(i + 1, j)]
                dp[(i, j)] = ans

        return dp[(0, 0)]


if __name__ == "__main__":
    s = Solution()
    assert s.numDistinct("rabbbit", "rabbit") == 3
    assert s.numDistinct("babgbag", "bag") == 5
    print("ok")
