import heapq

# Minimum Cost to convert string I
"""
You are given two 0-indexed strings source and target, both of length n
and consisting of lowercase English
letters. You are also given
two 0-indexed character arrays original and changed,
and an integer array cost,
where cost[i] represents the
cost of changing the character original[i] to the character changed[i].

You start with the string source. In one operation, you can pick a character x
from the string and change it to the character y
at a cost of z if there exists any
index j such that cost[j] == z, original[j] == x, and changed[j] == y.

Return the minimum cost to convert the string source to the
string target using any number of operations.
If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].
"""
"""
Example 1:
Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
Output: 28
Explanation:
To convert the string "abcd" to string "acbe":
- Change value at index 1 from 'b' to 'c' at a cost of 5.
- Change value at index 2 from 'c' to 'e' at a cost of 1.
- Change value at index 2 from 'e' to 'b' at a cost of 2.
- Change value at index 3 from 'd' to 'e' at a cost of 20.

The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.

Example 2:
Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
Output: 12
Explanation:
To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing
the character 'c' to 'b' at a cost of 2, for a total cost
of 1 + 2 = 3.
To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.

Example 3:
Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]
Output: -1
Explanation:
It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.
"""
"""
Constraints:
- 1 <= source.length == target.length <= 105
- source, target consist of lowercase English letters.
- 1 <= cost.length == original.length == changed.length <= 2000
- original[i], changed[i] are lowercase English letters.
- 1 <= cost[i] <= 106
- original[i] != changed[i]
"""


class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        n = len(original)

        # build adjlist
        adjlist = {chr(97 + i): [] for i in range(26)}
        for i in range(n):
            adjlist[original[i]].append((changed[i], cost[i]))

        def srt(start, target):
            dist = {chr(97 + i): float("inf") for i in range(26)}
            pq = [(0, start)]
            dist[start] = 0

            while pq:
                dis, node = heapq.heappop(pq)

                if dist[node] < dis:
                    continue

                for nei, cos in adjlist[node]:
                    kas = dis + cos
                    if kas < dist[nei]:
                        dist[nei] = kas
                        heapq.heappush(pq, (kas, nei))

            return dist[target]

        src_list = list(source)
        trt_list = list(target)

        total_cost = 0

        for i in range(len(src_list)):
            if src_list[i] == trt_list[i]:
                continue

            val = srt(src_list[i], trt_list[i])

            if val == float("inf"):
                return -1

            total_cost += val

        return total_cost


class SolutionOptimal(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        INF = float("inf")

        n = len(original)

        # build adjlist
        adjlist = {chr(97 + i): [] for i in range(26)}
        for i in range(n):
            adjlist[original[i]].append((changed[i], cost[i]))

        dist = [[INF] * 26 for _ in range(26)]

        # cost to stay the same
        for i in range(26):
            dist[i][i] = 0

        # fill direct cost
        for i in range(n):
            u = ord(original[i]) - 97
            v = ord(changed[i]) - 97
            dist[u][v] = min(dist[u][v], cost[i])

        # floyd-warshall algo
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # compute total cost
        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue

            u = ord(s) - 97
            v = ord(t) - 97
            if dist[u][v] == INF:
                return -1

            total_cost += dist[u][v]

        return total_cost


s = SolutionOptimal()

k1 = s.minimumCost(
    "abcd",
    "acbe",
    ["a", "b", "c", "c", "e", "d"],
    ["b", "c", "b", "e", "b", "e"],
    [2, 5, 5, 1, 2, 20],
)


k2 = s.minimumCost("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2])

k3 = s.minimumCost("abcd", "abce", ["a"], ["e"], [10000])

print(k1)
print(k2)
print(k3)
