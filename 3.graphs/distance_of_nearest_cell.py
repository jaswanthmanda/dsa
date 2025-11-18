# Distance of nearest cell having one
"""
Given a binary grid of N x M. Find the distance of the nearest 1 in the grid for each cell.

The distance is calculated as |i1 - i2| + |j1 - j2|, where i1, j1 are the row number and column number
of the current cell, and i2, j2 are the row number and column number of the nearest cell having value 1.
"""
"""
Examples:
Input: grid = [ [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1] ]
Output: [ [1, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0] ]
Explanation: 0's at (0,0), (0,3), (1,2), (1,3), (2,0) and (2,1) are at a distance of 1 from 1's at (0,1),(0,2), (0,2), (2,3), (1,0) and (1,1) respectively.


Input: grid = [ [1, 0, 1], [1, 1, 0], [1, 0, 0] ]
Output: [ [0, 1, 0], [0, 0, 1], [0, 1, 2] ]
Explanation: 0's at (0,1), (1,2), (2,1) and (2,2) are at a distance of 1, 1, 1 and 2 from 1's at (0,0),(0,2), (2,0) and (1,1) respectively.

Constraints:
- 1 <= N, M <= 500
- grid[i][j] == 0 or 1
- There is atleast one 1 in the grid
"""

class Solution:
    def nearest(self, grid):
