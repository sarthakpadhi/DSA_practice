"""
239. Sliding Window Maximum
Link: https://leetcode.com/problems/sliding-window-maximum/
Difficulty: Hard
Time: O(n)   Space: O(k)
"""
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxSoFar = []
        q = deque()

        if k == 1:
            return nums

        for r in range(len(nums)):
            while q and r >= k and q[0] <= r - k:
                q.popleft()

            while q and nums[q[-1]] <= nums[r]:
                q.pop()

            q.append(r)

            if r >= k - 1:
                maxSoFar.append(nums[q[0]])

        return maxSoFar
