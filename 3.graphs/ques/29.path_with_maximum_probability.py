from collections import deque

# Path with maximum probability
"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by
an edge list where edges[i] = [a, b] is an
undirected edge connecting the nodes a and b with a
probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum
probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will
be accepted if it differs from the correct answer by at most 1e-5.
"""
"""
Example 1:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation:
There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:
Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation:
There is no path between 0 and 2.
"""
"""
Constraints:
- 2 <= n <= 10^4
- 0 <= start, end < n
- start != end
- 0 <= a, b < n
- a != b
- 0 <= succProb.length == edges.length <= 2*10^4
- 0 <= succProb[i] <= 1
- There is at most one edge between every two nodes.
"""


class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        if end_node >= n:
            return float(0)

        # build adj list
        adjlist = {i: [] for i in range(n)}
        for i, edge in enumerate(edges):
            adjlist[edge[0]].append((edge[1], succProb[i]))
            adjlist[edge[1]].append((edge[0], succProb[i]))

        # vis = set([start_node])
        q = deque([(start_node, float(1))])
        dist = [float("-inf")] * n
        dist[start_node] = float(1)

        while q:
            node, sp = q.popleft()

            if sp < dist[node]:
                continue

            for nei, nei_p in adjlist[node]:
                kas = nei_p * sp
                if dist[nei] < kas:
                    dist[nei] = kas
                    q.append((nei, kas))

        return dist[end_node] if dist[end_node] != float("-inf") else float(0)


s = Solution()

k1 = s.maxProbability(
    3,
    [
        [0, 1],
        [1, 2],
        [0, 2],
    ],
    [
        0.5,
        0.5,
        0.2,
    ],
    0,
    2,
)

k2 = s.maxProbability(
    3,
    [
        [0, 1],
        [1, 2],
        [0, 2],
    ],
    [
        0.5,
        0.5,
        0.3,
    ],
    0,
    2,
)

k3 = s.maxProbability(
    3,
    [
        [0, 1],
    ],
    [
        0.5,
    ],
    0,
    2,
)

print(k1)
print(k2)
print(k3)
