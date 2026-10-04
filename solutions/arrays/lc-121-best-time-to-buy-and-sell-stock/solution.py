class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minSoFar = prices[0]
        ans = 0
        for right in prices:
            minSoFar = min(right, minSoFar)
            ans = max(right - minSoFar, ans)

        return ans
