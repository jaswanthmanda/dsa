from collections import deque

# Minimize the maximum edge weight of graph
"""
You are given two integers, n and threshold, as well as a directed weighted graph of n nodes numbered from 0 to n - 1.
The graph is represented by a 2D integer array edges, where edges[i] = [Ai, Bi, Wi] indicates that there is an edge going
from node Ai to node Bi with weight Wi.

You have to remove some edges from this graph (possibly none), so that it satisfies the following conditions:

- Node 0 must be reachable from all other nodes.
- The maximum edge weight in the resulting graph is minimized.
- Each node has at most threshold outgoing edges.

Return the minimum possible value of the maximum edge weight after removing the necessary edges.
If it is impossible for all conditions to be satisfied, return -1.
"""
"""
Example 1:
Input: n = 5, edges = [[1,0,1],[2,0,2],[3,0,1],[4,3,1],[2,1,1]], threshold = 2
Output: 1
Explanation:
Remove the edge 2 -> 0. The maximum weight among the remaining edges is 1.


Example 2:
Input: n = 5, edges = [[0,1,1],[0,2,2],[0,3,1],[0,4,1],[1,2,1],[1,4,1]], threshold = 1
Output: -1
Explanation:
It is impossible to reach node 0 from node 2.


Example 3:
Input: n = 5, edges = [[1,2,1],[1,3,3],[1,4,5],[2,3,2],[3,4,2],[4,0,1]], threshold = 1
Output: 2
Explanation:
Remove the edges 1 -> 3 and 1 -> 4. The maximum weight among the remaining edges is 2.


Example 4:
Input: n = 5, edges = [[1,2,1],[1,3,3],[1,4,5],[2,3,2],[4,0,1]], threshold = 1
Output: -1
"""
"""
Constraints:
- 2 <= n <= 105
- 1 <= threshold <= n - 1
- 1 <= edges.length <= min(105, n * (n - 1) / 2).
- edges[i].length == 3
- 0 <= Ai, Bi < n
- Ai != Bi
- 1 <= Wi <= 106
- There may be multiple edges between a pair of nodes, but they must have unique weights.
"""


class Solution(object):
    def minMaxWeight(self, n, edges, threshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        # collect and sort unique weights
        weights = sorted(set(w for _, _, w in edges))

        # build adjlist
        adjlist = {i: [] for i in range(n)}

        for u, v, w in edges:
            adjlist[u].append((v, w))

        def feasible(X):
            # Step 1: build graph using only edges with w <= X
            g = [[] for _ in range(n)]
            for u in adjlist:
                for v, w in adjlist[u]:
                    if w <= X:
                        g[u].append(v)

            # Step 2: reverse graph
            rg = [[] for _ in range(n)]
            for u in range(n):
                for v in g[u]:
                    rg[v].append(u)

            # Step 3: BFS from node 0 on reversed graph
            q = deque([0])
            visited = [False] * n
            visited[0] = True

            parent = [-1] * n
            while q:
                v = q.popleft()
                for u in rg[v]:
                    if not visited[u]:
                        visited[u] = True
                        parent[u] = v
                        q.append(u)

            # If some node can't find reach 0 -> impossible
            if not all(visited):
                return False

            # Step 4: enforce outgoing degree <= threshold
            out_count = [0] * n
            for u in range(n):
                if u != 0:
                    p = parent[u]
                    out_count[p] += 1
                    if out_count[p] > threshold:
                        return False

            return True

        # Binary Search on answer
        lo, hi = 0, len(weights) - 1
        result = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(weights[mid]):
                result = weights[mid]
                hi = mid - 1
            else:
                lo = mid + 1

        return result


s = Solution()

k1 = s.minMaxWeight(
    5,
    [
        [1, 0, 1],
        [2, 0, 2],
        [3, 0, 1],
        [4, 3, 1],
        [2, 1, 1],
    ],
    2,
)

k2 = s.minMaxWeight(
    5,
    [
        [0, 1, 1],
        [0, 2, 2],
        [0, 3, 1],
        [0, 4, 1],
        [1, 2, 1],
        [1, 4, 1],
    ],
    1,
)

k3 = s.minMaxWeight(
    5,
    [
        [1, 2, 1],
        [1, 3, 3],
        [1, 4, 5],
        [2, 3, 2],
        [3, 4, 2],
        [4, 0, 1],
    ],
    1,
)

k4 = s.minMaxWeight(
    5,
    [
        [1, 2, 1],
        [1, 3, 3],
        [1, 4, 5],
        [2, 3, 2],
        [4, 0, 1],
    ],
    1,
)

print(k1)
print(k2)
print(k3)
print(k4)
