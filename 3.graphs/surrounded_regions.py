import copy
from collections import deque

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
        m = len(mat)
        n = len(mat[0])
        visited = set()

        newVal = copy.deepcopy(mat)

        def bfs(row, col):
            q = deque([(row, col)])
            visited.add((row, col))
            stack = []
            touches_edge = False

            while q:
                r, c = q.popleft()
                stack.append((r, c))

                vals = [
                    (r - 1, c),
                    (r + 1, c),
                    (r, c - 1),
                    (r, c + 1),
                ]

                for val in vals:
                    a, b = val[0], val[1]
                    if (
                        0 <= a < m
                        and 0 <= b < n
                        and mat[a][b] == "O"
                        and (a, b) not in visited
                    ):
                        if a in [0, m - 1] or b in [0, n - 1]:
                            touches_edge = True
                        visited.add((a, b))
                        q.append((a, b))

            if touches_edge:
                return []

            return stack

        def replaceVals(stacs):
            if len(stacs) == 0:
                return

            while stacs:
                c, d = stacs.pop()

                newVal[c][d] = "X"

        for i in range(m):
            for j in range(n):
                if (
                    i not in [0, m - 1]
                    and j not in [0, n - 1]
                    and mat[i][j] == "O"
                    and (i, j) not in visited
                ):
                    stac = bfs(i, j)
                    replaceVals(stac)

        return newVal


sk = Solution()

k1 = sk.fill(
    [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
)

k2 = sk.fill(
    [
        ["X", "X", "X"],
        ["X", "O", "X"],
        ["X", "X", "X"],
    ]
)

print(k1)
print(k2)
