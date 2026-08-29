"""
4035. Largest String
Link: https://leetcode.com/problems/largest-string/
Difficulty: Medium
Time: O(n * b)   Space: O(n * b)
"""


class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        ans = []
        for i in nums:
            binary = list(bin(i)[2:])[::-1]
            tmp = []
            for j in range(len(binary)):
                if binary[j] == "1":
                    if j <= 25:
                        tmp.append(chr(ord("a") + j))
                    else:
                        tmp = tmp + ["z"] * 2 ** (j - 25)
            ans.append("".join(tmp[::-1]))
        return ans
