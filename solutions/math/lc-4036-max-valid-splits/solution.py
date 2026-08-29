"""
4036. Maximum Valid Splits
Link: https://leetcode.com/problems/maximum-valid-splits/
Difficulty: Medium
Time: O(n^3)   Space: O(n^2)
"""
import math


class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        N = len(nums)
        dp = [[0] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = nums[i]
            for j in range(i + 1, N):
                dp[i][j] = 1 if dp[i][j - 1] == 1 else math.gcd(nums[j], dp[i][j - 1])

        def safe(i, j):
            return dp[i][j] if i <= j else 0

        cnt = 0
        tmp = sum(1 for idx in range(N - 1) if dp[0][idx] == dp[idx + 1][N - 1])
        cnt = max(cnt, tmp)

        for s in range(N):
            tmp = 0
            for idx in range(N - 1):
                if idx == s:
                    continue
                if idx < s:
                    left = safe(0, idx)
                    right = math.gcd(safe(idx + 1, s - 1), safe(s + 1, N - 1))
                else:
                    left = math.gcd(safe(0, s - 1), safe(s + 1, idx))
                    right = safe(idx + 1, N - 1)
                if left == right:
                    tmp += 1
            cnt = max(cnt, tmp)

        return cnt
