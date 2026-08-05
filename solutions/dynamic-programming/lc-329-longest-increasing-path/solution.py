"""
329. Longest Increasing Path in a Matrix
Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
Difficulty: Hard
Time: O(m*n)   Space: O(m*n)
"""
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R = len(matrix)
        C = len(matrix[0])
        memo = {}

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            best = 1
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            memo[(r, c)] = best
            return best

        return max(dfs(r, c) for r in range(R) for c in range(C))


if __name__ == "__main__":
    s = Solution()
    assert s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
    assert s.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
    assert s.longestIncreasingPath([[1]]) == 1
    print("ok")
