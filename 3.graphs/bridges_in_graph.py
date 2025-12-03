# Bridges in graph
"""
Given an undirected connected Graph with V vertices (Numbered from 0 to V-1) and E edges.
An edge is represented [ai, bi] denoting that there is an edge from vertex ai to bi.
An edge is called a bridge if its removal makes some vertex unable to reach another vertex.

Return all bridges in the graph in any order.
"""
"""
Examples:
Input: V = 4, E = [ [0,1],[1,2],[2,0],[1,3] ]
Output: [ [1, 3] ]
Explanation:
The edge [1, 3] is the critical edge because if we remove the edge the graph will be divided into 2 components.


Input: V = 3, E = [[0,1],[1,2],[2,0]]
Result: []
Explanation:
There no bridges in the graph.
"""
"""
Constraints:
- 2 <= V, E <= 104
- 0 <= ai, bi <= V - 1
"""


"""
class Solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, vis, adj, tin, low, bridges):
        # Mark the node as visited
        vis[node] = 1

        # Time of insertion and the lowest time of
        # insert for node will be the current time
        tin[node] = low[node] = self.timer

        # Increment the current time
        self.timer += 1

        # Traverse all its neighbors
        for it in adj[node]:
            # Skip the parent
            if it == parent:
                continue

            # If a neighbor is not visited
            if vis[it] == 0:
                # Make a recursive DFS call
                self.dfs(it, node, vis, adj, tin, low, bridges)

                # Once the recursive DFS call returns, update
                # the lowest time of insertion for the node
                low[node] = min(low[it], low[node])

                # If the lowest time of insertion of the 
                # node is found to be greater than the 
                # time of insertion of the neighbor
                if low[it] > tin[node]:
                    # The edge represents a bridge
                    bridges.append([it, node])
            else:
                # Update the lowest time of insertion of the node
                low[node] = min(low[node], tin[it])

    def criticalConnections(self, n, connections):
        # Adjacency list
        adj = [[] for _ in range(n)]
        
        # Add all the edges to the adjacency list
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        # Visited array
        vis = [0] * n
        
        # To store the time of insertion (discovery time) of nodes
        tin = [0] * n
        
        # To store the lowest time of insert of the nodes
        low = [0] * n
        
        # To store the bridges of the graph
        bridges = []
        
        # Start a DFS traversal from node 0 with its parent as -1
        self.dfs(0, -1, vis, adj, tin, low, bridges)
        
        # Return the computed result
        return bridges


# Main function
if __name__ == "__main__":
    V = 4
    E = [
        [0, 1],
        [1, 2],
        [2, 0],
        [1, 3]
    ]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to identify the bridges in a graph
    ans = sol.criticalConnections(V, E)
    
    print("The critical connections in the given graph are:")
    for bridge in ans:
        print(bridge[0], bridge[1])
"""


class Solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, vis, adj, tin, low, bridges):
        # Mark the node as visited
        vis[node] = 1

        # Time of insertion and the lowest time of
        # insert for node will be the current time
        tin[node] = low[node] = self.timer

        # Increment the current time
        self.timer += 1

        # Traverse all its neighbors
        for it in adj[node]:
            # Skip the parent
            if it == parent:
                continue

            # If a neighbor is not visited
            if vis[it] == 0:
                # Make a recursive DFS call
                self.dfs(it, node, vis, adj, tin, low, bridges)

                # Once the recursive DFS call returns, update
                # the lowest time of insertion for the node
                low[node] = min(low[it], low[node])

                # If the lowest time of insertion of the
                # node is found to be greater than the
                # time of insertion of the neighbor
                if low[it] > tin[node]:
                    bridges.append([it, node])
            else:
                # Update the lowest time of insertion of node
                low[node] = min(low[node], tin[it])

    def criticalConnections(self, V, E):
        # Adjacency list
        adj = [[] for _ in range(V)]

        # Add all the edges to the adjacency list
        for edge in E:
            u, v = edge[0], edge[1]
            adj[u].append(v)
            adj[v].append(u)

        # Visited array
        vis = [0] * V

        # To store the time of insertion (discovery time) of nodes
        tin = [0] * V

        # To store the lowest time of insert of the nodes
        low = [0] * V

        # To store the briges of the graph
        bridges = []

        # Start a DFS traversal from node 0 with its parent as -1
        self.dfs(0, -1, vis, adj, tin, low, bridges)

        # Return the computed result
        return bridges


s = Solution()

k1 = s.criticalConnections(
    4,
    [
        [0, 1],
        [1, 2],
        [2, 0],
        [1, 3],
    ],
)

k2 = s.criticalConnections(
    3,
    [
        [0, 1],
        [1, 2],
        [2, 0],
    ],
)

print(k1)
print(k2)
