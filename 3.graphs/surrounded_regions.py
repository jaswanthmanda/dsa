# Surrounded Regions
"""
You are given a matrix mat of size N x M where each cell contains either 'O' or 'X'.
Your task is to replace all 'O' cells that are completely surrounded by 'X' with 'X'.

Rules:
- An 'O' (or a group of connected 'O's) is considered surrounded if it is not connected to any border of the matrix.

- Two 'O' cells are considered connected if they are adjacent horizontally or vertically (not diagonally).

- A region of connected 'O's that touches the border (i.e., first row, last row, first column, or last column) is not surrounded and should not be changed.
"""

"""
Input: mat = [ ["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"] ]
Output: [ ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"] ]

The 'O' cells at positions (1,1), (1,2), (2,2), and (3,1) are surrounded by 'X' cells in all directions (horizontally and vertically).
However, the 'O' region at (3,1) is adjacent to an edge of the board, so it cannot be completely surrounded by 'X' cells. Therefore, it remains unchanged.


Input: mat = [ ["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"] ]
Output: [ ["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"] ]
Explanation: The only 'O' cell at position (1,1) is completely surrounded by 'X' cells in all directions (horizontally and vertically). Hence, it is replaced with 'X' in the output.
"""
"""
Constraints:
  N == mat.length
  M == mat[i].length
  1 <= N, M <= 300
  mat[i][j] is 'X' or 'O'.
"""

class Solution:
    def fill(self, mat):
