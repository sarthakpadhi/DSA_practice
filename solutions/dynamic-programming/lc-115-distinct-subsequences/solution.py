"""
115. Distinct Subsequences
Link: https://leetcode.com/problems/distinct-subsequences/
Difficulty: Hard
Time: O(m*n)   Space: O(m*n)
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            elif i == len(s):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            ans = 0
            if s[i] == t[j]:
                ans += dfs(i + 1, j + 1)
            ans += dfs(i + 1, j)
            dp[(i, j)] = ans
            return ans

        return dfs(0, 0)


if __name__ == "__main__":
    s = Solution()
    assert s.numDistinct("rabbbit", "rabbit") == 3
    assert s.numDistinct("babgbag", "bag") == 5
    print("ok")
