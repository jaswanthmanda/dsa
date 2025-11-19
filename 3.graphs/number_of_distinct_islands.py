# Number of distinct islands
"""
You are given a 2D matrix grid of size N × M, where each cell contains either 0 or 1.
Find the number of distinct
islands where a group of connected 1s
(horizontally or vertically) forms an island.
Two islands are considered to be same if and only if
one island is equal to another (not rotated or reflected).
"""

"""
Input: grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1],[0, 0, 0, 1, 1]]
Output: 1
Explanation:
Same colored islands are equal. We have 2 equal islands, so we have only 1 distinct island.


Input: grid = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1],[1, 1, 0, 1, 1]]
Output: 3
Explanation:
Same colored islands are equal. We have 4 islands, but 2 of them are equal, So we have 3 distinct islands..
"""
class Solution:
    def countDistinctIslands(self, grid):
