from collections import deque

# Most profitable path in a tree
"""
There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node 0.
You are given a 2D integer array
edges of length n - 1 where edges[i] = [ai, bi]
indicates that there is an edge between nodes ai and bi in the tree.

At every node i, there is a gate. You are also given an array of even integers amount, where amount[i] represents:

- the price needed to open the gate at node i, if amount[i] is negative, or,
- the cash reward obtained on opening the gate at node i, otherwise.

The game goes on as follows:
- Initially, Alice is at node 0 and Bob is at node bob.
- At every second, Alice and Bob each move to an adjacent node. Alice moves towards some leaf node, while Bob moves towards node 0.
- For every node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:
 - If the gate is already open, no price will be required, nor will there be any cash reward.
 - If Alice and Bob reach the node simultaneously, they share the price/reward for opening the gate there. In other words, if the price to open the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate is c, both of them receive c / 2 each.
- If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node 0, he stops moving. Note that these events are independent of each other.

Return the maximum net income Alice can have if she travels towards the optimal leaf node.
"""
"""
Example 1:
Input: edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]
Output: 6
Explanation:
The above diagram represents the given tree. The game goes as follows:
- Alice is initially on node 0, Bob on node 3. They open the gates of their respective nodes.
  Alice's net income is now -2.
- Both Alice and Bob move to node 1.
  Since they reach here simultaneously, they open the gate together and share the reward.
  Alice's net income becomes -2 + (4 / 2) = 0.
- Alice moves on to node 3. Since Bob already opened its gate, Alice's income remains unchanged.
  Bob moves on to node 0, and stops moving.
- Alice moves on to node 4 and opens the gate there. Her net income becomes 0 + 6 = 6.
Now, neither Alice nor Bob can make any further moves, and the game ends.
It is not possible for Alice to get a higher net income.


Example 2:
Input: edges = [[0,1]], bob = 1, amount = [-7280,2350]
Output: -7280
Explanation:
Alice follows the path 0->1 whereas Bob follows the path 1->0.
Thus, Alice opens the gate at node 0 only. Hence, her net income is -7280.
"""
"""
Constraints:
- 2 <= n <= 105
- edges.length == n - 1
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- edges represents a valid tree.
- 1 <= bob < n
- amount.length == n
- amount[i] is an even integer in the range [-104, 104].
"""


class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        """
        :type edges: List[List[int]]
        :type bob: int
        :type amount: List[int]
        :rtype: int
        """
        # build adjlist
        n = len(amount)

        adjlist = {i: [] for i in range(n)}
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)

        bobTime = [float("inf")] * n

        def bfs(start, adjlist):
            parents = [-1] * n

            q = deque([0])
            vis = set([0])

            while q:
                node = q.popleft()

                for nei in adjlist[node]:
                    if nei != 0 and nei not in vis:
                        parents[nei] = node
                        vis.add(nei)
                        q.append(nei)

            # calc time
            t = 0
            cur = bob
            while cur != -1:
                bobTime[cur] = t
                cur = parents[cur]
                t += 1

        bfs(bob, adjlist)

        # alice ops
        vis_set = set()
        self.max_prof = float("-inf")

        def dfs(start, adjlist, curr_prof, time):
            vis_set.add(start)
            if time < bobTime[start]:
                curr_prof += amount[start]
            elif bobTime[start] == time:
                curr_prof += amount[start] // 2

            if start != 0 and len(adjlist[start]) == 1:
                self.max_prof = max(self.max_prof, curr_prof)
            else:
                for nei in adjlist[start]:
                    if nei not in vis_set:
                        k_time = time + 1
                        dfs(nei, adjlist, curr_prof, k_time)

        dfs(0, adjlist, 0, 0)

        return self.max_prof


s = Solution()

k1 = s.mostProfitablePath(
    [[0, 1], [1, 2], [1, 3], [3, 4]],
    3,
    [-2, 4, 2, -4, 6],
)

k2 = s.mostProfitablePath(
    [[0, 1]],
    1,
    [-7280, 2350],
)

print(k1)
print(k2)
