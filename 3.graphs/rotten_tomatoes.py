# Rotten Oranges
"""
Given an n x m grid, where each cell has the following values : 



2 - represents a rotten orange

1 - represents a Fresh orange

0 - represents an Empty Cell

Every minute, if a fresh orange is adjacent to a rotten orange in 4-direction ( upward, downwards, right, and left ) it becomes rotten. 



Return the minimum number of minutes required such that none of the cells has a Fresh Orange. If it's not possible, return -1.
"""

"""
Examples:
Input: grid = [ [2, 1, 1] , [0, 1, 1] , [1, 0, 1] ]
Output: -1
Explanation: Orange at (3,0) cannot be rotten.

Input: grid = [ [2,1,1] , [1,1,0] , [0,1,1] ] 
Output: 4
"""

class Solution:
    def orangesRotting(self, grid):
