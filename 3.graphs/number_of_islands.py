# Number of islands
"""
Given a grid of size N x M (N is the number of rows and M is the number of columns in the grid)
consisting of '0's (Water) and ‘1's(Land).
Find the number of islands.

An island is surrounded by water and is formed by
connecting adjacent lands horizontally or
vertically or diagonally i.e., in all 8 directions.
"""

"""
Examples:

Input: grid = [ ["1", "1", "1", "0", "1"], ["1", "0", "0", "0", "0"], ["1", "1", "1", "0", "1"], ["0", "0", "0", "1", "1"] ]
Output: 2
Explanation:
This grid contains 2 islands. Each '1' represents a piece of land, and the islands are formed by connecting adjacent lands horizontally or vertically.
Despite some islands having a common edge, they are considered separate
islands because there is no land connectivity in any of the eight directions between them. Therefore, the grid contains 2 islands.

Input: grid = [ ["1", "0", "0", "0", "1"], ["0", "1", "0", "1", "0"], ["0", "0", "1", "0", "0"], ["0", "1", "0", "1"," 0"] ]
Output: 1
Explanation:
In the given grid, there's only one island as all the '1's are connected either horizontally,
vertically, or diagonally, forming a single contiguous landmass surrounded by water on all sides.


Constraints:
·  N == grid.length

·  M == grid[i].length

·  1 <= N, M <= 300

·  grid[i][j] is '0' or '1'.
"""

class Solution:
    def numIslands(self, grid):
