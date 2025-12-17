# Flower planting with no adjacent
"""
You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes
a bidirectional path between garden xi to garden yi.
In each garden, you want to plant one of 4 types of flowers.

All gardens have at most 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden
such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer,
where answer[i] is the type of flower planted in the (i+1)th garden.
The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.
"""
"""
Example 1:
Input: n = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Explanation:
Gardens 1 and 2 have different types.
Gardens 1 and 2 have different types.
Gardens 3 and 1 have different types.
Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].


Example 2:
Input: n = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]


Example 3:
Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
"""
"""
Constraints:
- 1 <= n <= 104
- 0 <= paths.length <= 2 * 104
- paths[i].length == 2
- 1 <= xi, yi <= n
- xi != yi
- Every garden has at most 3 paths coming into or leaving it.
"""


class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        # build adj list
        adjList = {i: [] for i in range(1, n + 1)}
        for edge in paths:
            u1 = edge[0]
            u2 = edge[1]
            adjList[u1].append(u2)
            adjList[u2].append(u1)

        ans = [0] * n

        for i in range(1, n + 1):
            used_col = set()

            for nei in adjList[i]:
                if ans[nei - 1] != 0:
                    used_col.add(ans[nei - 1])

            for j in range(1, 5):
                if j not in used_col:
                    ans[i - 1] = j
                    break

        return ans


s = Solution()

k1 = s.gardenNoAdj(
    3,
    [
        [1, 2],
        [2, 3],
        [3, 1],
    ]
)

k2 = s.gardenNoAdj(
    4,
    [
        [1, 2],
        [3, 4],
    ]
)

k3 = s.gardenNoAdj(
    4,
    [
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 1],
        [1, 3],
        [2, 4],
    ]
)

print(k1)
print(k2)
print(k3)
