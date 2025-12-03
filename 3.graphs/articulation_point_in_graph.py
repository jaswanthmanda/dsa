# Articulation point in graph
"""
Given an undirected graph with V vertices and adjacency list adj. Find all the vertices removing which
q(and edges through it) would increase the number of connected components in the graph.
The graph may be initially disconnected..

Return the vertices in ascending order.
If there are no such vertices then returns a list containing -1.

Note: Indexing is zero-based i.e nodes numbering from (0 to V-1).
There might be loops present in the graph.
"""
"""
Examples:
Input: V = 7, adj=[[1,2,3], [0], [0,3,4,5], [2,0], [2,6], [2,6], [4,5]] 
Output: [0, 2]
Explanation:
If we remove node 0 or node 2, the graph will be divided into 2 or more components.


Input: V = 5, adj=[[1], [0,4], [3,4], [2,4], [1,2,3]] 
Output: [1, 4]
Explanation:
If we remove either node 1 or node 4, the graph breaks into multiple components.
"""
"""
Constraints:
- E= Number of Edges
- 1 ≤ V, E ≤ 10^4
"""


class Solution:
    def __init__(self):
        self.timer = 1

    # Helper function to make DFS calls while
    # identifying articulation points
    def dfs(self, node, parent, vis, tin, low, mark, adj):

        # Mark the node as visited
        vis[node] = True

        # Time of insertion and the lowest time of
        # insert for node will be current time
        tin[node] = low[node] = self.timer

        # Increment the timer
        self.timer += 1

        # To count the number of children of the node
        child = 0

        # Traverse all its neighbor
        for it in adj[node]:
            # Skip the parent
            if it == parent:
                continue

            # If a neighbor is not  visited
            if not vis[it]:
                # recurse
                self.dfs(it, node, vis, tin, low, mark, adj)

                low[node] = min(low[node], low[it])

                # If the lowest time of insertion of the node
                # found to be greater than the time of insertion.
                if low[it] >= tin[node] and parent != -1:
                    # Mark the node as an articulation point
                    mark[node] = True

                # Increment the child counter
                child += 1

            # Else if the neighbor is already visited
            else:

                # Update the lowest time of insertion of the node
                low[node] = min(low[node], tin[it])

        # If the node is not a starting ndoe
        # and has more than one child
        if child > 1 and parent == -1:

            # Mark the node as an articulation point
            mark[node] = True

    # Function to determine the articulation
    # points in the given graph
    def articulationPoints(self, n, adj):
        # Visited array
        vis = [False] * n

        # To store the time of insertion (discovery time) of nodes
        tin = [-1] * n

        # To store the lowest time of insert of the nodes
        low = [-1] * n

        # To mark if a node is an articulation point
        mark = [False] * n

        # Start DFS traversal of the graph
        for i in range(n):

            # If a node is not visited
            if not vis[i]:

                # Perform DFS starting from that node
                self.dfs(i, -1, vis, tin, low, mark, adj)

        # To store the nodes that are articulation point
        ans = []

        # Traverse all nodes
        for i in range(n):

            # If a node is marked as an articulation point
            if mark[i]:
                # Add it to the result
                ans.append(i)

        # If there are no articulation points, return -1
        if len(ans) == 0:
            return [-1]

        # Return the result
        return ans


s = Solution()

k1 = s.articulationPoints(
    7,
    [
        [1, 2, 3],
        [0],
        [0, 3, 4, 5],
        [2, 0],
        [2, 6],
        [2, 6],
        [4, 5],
    ],
)

k2 = s.articulationPoints(
    5,
    [
        [1],
        [0, 4],
        [3, 4],
        [2, 4],
        [1, 2, 3],
    ],
)

print(k1)
print(k2)
