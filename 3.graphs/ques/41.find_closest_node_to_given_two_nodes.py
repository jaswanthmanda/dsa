import heapq

# Find closest node to given two nodes
"""
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.
'
The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed
edge from node i to node edges[i].
If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2,
such that the maximum between the distance from node1 to that node,
and from node2 to that node is minimized. If there are multiple answers,
return the node with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.
"""
"""
Example 1:
Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation:
The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot
get a node with a smaller maximum distance than 1, so we return node 2.

Example 2:
Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2
Explanation:
The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
The maximum of those two distances is 2. It can be proven that
we cannot get a node with a smaller maximum distance than 2, so we return node 2.
"""
"""
Constraints:
- n == edges.length
- 2 <= n <= 105
- -1 <= edges[i] < n
- edges[i] != i
- 0 <= node1, node2 < n
"""


class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        # build adjlist
        n = len(edges)

        ####### brute force  ###########
        # adjlist = {i: [] for i in range(n)}
        # for i, u in enumerate(edges):
        #     if u != -1:
        #         adjlist[i].append(u)

        # def srt(start, adjlist):
        #     dist = [float("inf")] * n
        #     pq = [(0, start)]
        #     dist[start] = 0

        #     while pq:
        #         steps, node = heapq.heappop(pq)

        #         if steps > dist[node]:
        #             continue

        #         for nei in adjlist[node]:
        #             kas = steps + 1
        #             if dist[nei] > kas:
        #                 dist[nei] = kas
        #                 heapq.heappush(pq, (kas, nei))

        #     return dist

        def get_dist(start):
            dist = [float('inf')]*n
            steps = 0
            cur = start
            while cur != -1 and dist[cur] == float('inf'):
                dist[cur] = steps
                steps += 1
                cur = edges[cur]

            return dist

        node1_dist = get_dist(node1)
        node2_dist = get_dist(node2)

        print(node1_dist)
        print(node2_dist)

        ans = -1
        small_max = float("inf")

        for i in range(n):
            if node1_dist[i] != float("inf") and node2_dist[i] != float("inf"):

                kemp = max(node1_dist[i], node2_dist[i])

                if small_max > kemp:
                    small_max = kemp
                    ans = i

        return ans


s = Solution()

k1 = s.closestMeetingNode([2, 2, 3, -1], 0, 1)

k2 = s.closestMeetingNode([1, 2, -1], 0, 2)

k3 = s.closestMeetingNode([4, 3, 0, 5, 3, -1], 4, 0)

print(k1)
print(k2)
print(k3)
