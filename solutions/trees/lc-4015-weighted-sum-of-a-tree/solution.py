"""
4015. Weighted Sum of a Tree
Link: https://leetcode.com/problems/weighted-sum-of-a-tree/
Difficulty: Medium
Time: O(n)   Space: O(n)
"""
from collections import defaultdict


class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        adjList = defaultdict(list)
        for i in range(len(parent)):
            adjList[parent[i]].append(i)

        def getHeight(currNode):
            if not adjList[currNode]:
                return 1
            return 1 + max(getHeight(i) for i in adjList[currNode])

        height = getHeight(0)

        queue = [(0, 1)]
        ans = 0
        while queue:
            currNode, d = queue.pop(0)
            ans += (height - d + 1) * nums[currNode]
            queue = queue + [(nd, d + 1) for nd in adjList[currNode]]

        return ans
