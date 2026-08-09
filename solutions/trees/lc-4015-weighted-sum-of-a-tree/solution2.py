"""
4015. Weighted Sum of a Tree — deque BFS (true O(n))
Link: https://leetcode.com/problems/weighted-sum-of-a-tree/
Difficulty: Medium
Time: O(n)   Space: O(n)
"""
from collections import defaultdict, deque


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

        queue = deque([(0, 1)])
        ans = 0
        while queue:
            currNode, d = queue.popleft()
            ans += (height - d + 1) * nums[currNode]
            for nd in adjList[currNode]:
                queue.append((nd, d + 1))

        return ans
