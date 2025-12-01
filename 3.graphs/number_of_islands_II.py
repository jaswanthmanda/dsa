# Number of islands II
"""
Given n, m denoting the row and column of the 2D matrix, and an array
A of size k denoting the number of operations.
Matrix elements are 0 if there is water or 1 if there is land.
Originally, the 2D matrix
is all 0 which means there is no land in the matrix.
The array has k operator(s) and each operator has
two integers A[i][0], A[i][1] means that you can
change the cell matrix[A[i][0]][A[i][1]] from sea to island.
Return how many islands are there in the matrix after each operation.

The answer array will be of size k.
"""
"""
Input: n = 4, m = 5, k = 4, A = [[1,1],[0,1],[3,3],[3,4]] 
Output: [1, 1, 2, 2]
"""
"""
Input: n = 4, m = 5, k = 12, A = [[0,0],[0,0],[1,1],[1,0],[0,1],[0,3],[1,3],[0,4], [3,2], [2,2],[1,2], [0,2]] 
Output: [1, 1, 2, 1, 1, 2, 2, 2, 3, 3, 1, 1]
"""
"""
Constraints:
- 1 <= n, m <= 1000
- 1 <= k <= 104
- 0 <= A[i][0] < n
- 0 <= A[i][1] < m
"""

class Solution:
    def numOfIslands(self, n, m, A):
        