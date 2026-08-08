"""
2497. Maximum Star Sum of a Graph
Link: https://leetcode.com/problems/maximum-star-sum-of-a-graph/
Difficulty: Medium
Time: O(n + e·log e)   Space: O(n + e)
"""
from collections import defaultdict
from typing import List


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        maxSoFar = vals[0]

        for currNode in range(len(vals)):
            validVals = [vals[i] for i in adjList[currNode] if vals[i] > 0]
            validVals.sort(reverse=True)
            currSum = sum(validVals[:k]) + vals[currNode]
            maxSoFar = max(maxSoFar, currSum)

        return maxSoFar
