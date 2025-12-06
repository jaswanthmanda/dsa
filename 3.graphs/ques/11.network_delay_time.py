import heapq

# Network Delay Time
"""
You are given a network of n nodes, labeled from 1 to n.
You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
where ui is the source node, vi is the target node,
and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k.
Return the minimum time it takes for all the n nodes to receive the signal.
If it is impossible for all the n nodes to receive the signal, return -1.
"""
"""
Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
"""
"""
Constraints:
- 1 <= k <= n <= 100
- 1 <= times.length <= 6000
- times[i].length == 3
- 1 <= ui, vi <= n
- ui != vi
- 0 <= wi <= 100
- All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""


class Solution(object):
    def bfsD(self, start, n, adjList):
        dist = [float("inf")] * n
        pq = [(0, start)]
        dist[start - 1] = 0

        while pq:
            wt, node = heapq.heappop(pq)

            if wt > dist[node - 1]:
                continue

            for nei, nei_wt in adjList[node]:
                kas = nei_wt + wt

                if kas < dist[nei - 1]:
                    dist[nei - 1] = kas
                    heapq.heappush(pq, (kas, nei))

        if float('inf') in dist:
            return -1

        maxDist = max(dist)

        return maxDist

    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # build adjlist
        adjList = {i: [] for i in range(1, n + 1)}
        for edge in times:
            adjList[edge[0]].append((edge[1], edge[2]))
            # adjList[edge[1]].append((edge[0], edge[2]))

        ans = self.bfsD(k, n, adjList)

        if ans == float("inf"):
            return -1

        return ans


s = Solution()

k1 = s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)

k2 = s.networkDelayTime([[1, 2, 1]], 2, 1)

k3 = s.networkDelayTime([[1, 2, 1]], 2, 2)

k4 = s.networkDelayTime([[1, 2, 1], [2, 1, 3]], 2, 2)  # 3

k5 = s.networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 1]], 3, 2)  # -1

print(k1)
print(k2)
print(k3)
print(k4)
print(k5)
