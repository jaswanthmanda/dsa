# Floyd Warshall Algo
"""
Given a graph of V vertices numbered from 0 to V-1.
Find the shortest distances between every pair of vertices in a given edge-weighted directed graph.
The graph is represented as an adjacency matrix of size n x n.
Matrix[i][j] denotes the weight of the edge from i to j.
If matrix[i][j]=-1, it means there is no edge from i to j.
"""
"""
Input: matrix = [[0, 2, -1, -1],[1, 0, 3, -1],[-1, -1, 0, 1],[3, 5, 4, 0]]
Output: [[0, 2, 5, 6], [1, 0, 3, 4], [4, 6, 0, 1], [3, 5, 4, 0]] 
Explanation:
matrix[0][0] is storing the distance from vertex 0 to vertex 0, the distance from vertex 0 to vertex 1 is 2 and so on.

Input: matrix = [[0,25],[-1,0]]
Output: [[0, 25],[-1, 0]]
Explanation:
The matrix already contains the shortest distance.
"""
"""
Constraints:
- 1 <= n <= 100
- -1 <= matrix[ i ][ j ] <= 1000
"""


class Solution:
    def shortestDistance(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = float("inf")

        for via in range(n):
            for j in range(n):
                for k in range(n):
                    matrix[j][k] = min(
                        matrix[j][k],
                        matrix[j][via] + matrix[via][k],
                    )

        for a in range(n):
            for b in range(n):
                if matrix[a][b] == float("inf"):
                    matrix[a][b] = -1

        return matrix


s = Solution()

k1 = s.shortestDistance(
    [
        [0, 2, -1, -1],
        [1, 0, 3, -1],
        [-1, -1, 0, 1],
        [3, 5, 4, 0],
    ]
)

k2 = s.shortestDistance(
    [
        [0, 25],
        [-1, 0],
    ]
)

print(k1)
print(k2)
