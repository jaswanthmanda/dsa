from collections import deque

# Number of provinces
"""
Given an undirected graph with V vertices.
Two vertices u and v belong to a single province if there
is a path from u to v or v to u.
Find the number of provinces.
The graph is given as an n x n matrix adj where adj[i][j] = 1 if the ith
city and the jth city are directly connected, and adj[i][j] = 0 otherwise.

A province is a group of directly or indirectly connected cities and
no other cities outside of the group.
"""

"""
Examples:

Input: adj=[ [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1] ]
Output: 2
Explanation:
In this graph, there are two provinces: [1, 4] and [2, 3].
City 1 and city 4 have a path between
them, and city 2 and city 3 also have a path between them.
There is no path between any city in province 1 and any city in province 2.


Input: adj= [ [1, 0, 1], [0, 1, 0], [1, 0, 1] ]
Output: 2
Explanation:
The graph clearly has 2 Provinces [1,3] and [2]. As city 1 and city 3 has a path between them they belong to a single province. City 2 has no path to city 1 or city 3 hence it belongs to another province.

Constraints:
- 1 <= V <= 300
- V == adj.length
- V == adj[i].length
- adj[i][j] is 1 or 0.
- adj[i][i] == 1
- a[i][j] == adj[j][i]
"""


class Solution:
    def numProvinces(self, adj):
        n = len(adj)
        visited = set()
        provinces = 0

        def bfs(start):
            q = deque([start])
            visited.add(start)

            while q:
                node = q.popleft()

                for nei in range(n):
                    if adj[node][nei] == 1 and nei not in visited:
                        visited.add(nei)
                        q.append(nei)

        for i in range(n):
            if i not in visited:
                bfs(i)
                provinces += 1

        return provinces


s = Solution()
k1 = s.numProvinces([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]])
k2 = s.numProvinces([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(k1)
print(k2)
