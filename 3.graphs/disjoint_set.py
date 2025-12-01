# Disjoint Set
"""
Design a disjoint set (also called union-find)
data structure that supports the following operations:

DisjointSet(int n) initializes the disjoint set with n elements.
void unionByRank(int u, int v) merges the sets containing u and v using the rank heuristic.
void unionBySize(int u, int v) merges the sets containing u and v using the size heuristic.
bool find(int u, int v) checks if the elements u and v are in the same set
and returns true if they are, otherwise false.
"""
"""
Input:
["DisjointSet", "unionByRank", "unionBySize", "find", "find"]
[[5], [0, 1], [2, 3], [0, 1], [0, 3]]

Output:
[null, null, null, true, false]

Explanation:
DisjointSet ds = new DisjointSet(5); // Initialize a disjoint set with 5 elements
ds.unionByRank(0, 1); // Merge sets containing 0 and 1 using rank
ds.unionBySize(2, 3); // Merge sets containing 2 and 3 using size
ds.find(0, 1); // Returns true as 0 and 1 are in the same set
ds.find(0, 3); // Returns false as 0 and 3 are not in the same set


# second case
Input:
["DisjointSet", "unionBySize", "unionBySize", "find", "find"]
[[3], [0, 1], [1, 2], [0, 2], [0, 1]]

Output:
[null, null, null, true, true]

Explanation:
DisjointSet ds = new DisjointSet(3); // Initialize a disjoint set with 3 elements
ds.unionBySize(0, 1); // Merge sets containing 0 and 1 using size
ds.unionBySize(1, 2); // Merge sets containing 1 and 2 using rank
ds.find(0, 2); // Returns true as 0 and 2 are in the same set
ds.find(0, 1); // Returns true as 0 and 1 are in the same set
"""
"""
Constraints:
- 1 <= n <= 104
- 0 <= u, v < n
- At most 5 * 104 calls will be made to unionByRank, unionBySize, and find
"""


class DisjointSet:
    def __init__(self, n: int):
        # Resize the arrays
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    # Helper function to find ultimate
    # parent along with path compression
    def findUPar(self, node):
        # Base case
        if node == self.parent[node]:
            return node

        # Backtracking step for path_compression
        self.parent[node] = self.findUPar(self.parent[node])

        return self.parent[node]

    # Function to determine if two nodes
    # are in the same component or not
    def find(self, u: int, v: int) -> bool:
        # Return true if both have same ultimate parent
        return self.findUPar(u) == self.findUPar(v)

    # Function to perform union of
    # two nodes based on ranks
    def unionByRank(self, u: int, v: int) -> None:
        # Get the ultimate parents of both nodes
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        # return if nodes already belong to the same component
        if ulp_u == ulp_v:
            return

        # Otherwise, join the node to the other
        # node having higher ranks among the two
        if self.rank[ulp_u] < self.rank[ulp_v]:
            # Update the parent of ulp_u
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            # Update the parent of ulp_v
            self.parent[ulp_v] = ulp_u
        else:
            # Update the parent
            self.parent[ulp_u] = ulp_v
            # Update the rank
            self.rank[ulp_u] += 1

    # Function to perform union of
    # two nodes based on sizes
    def unionBySize(self, u: int, v: int) -> None:
        # Get the ultimate parents of both nodes
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        # Return if nodes already belong to the same component
        if ulp_u == ulp_v:
            return

        # Otherwise, join the node belonging to the smaller
        # component to the node belonging to bigger component
        if self.size[ulp_u] < self.size[ulp_v]:
            # Update the parent
            self.parent[ulp_v] = ulp_u
            # Update the size
            self.size[ulp_u] += self.size[ulp_v]
        else:
            # Update the parent
            self.parent[ulp_u] = ulp_v
            # Update the size
            self.size[ulp_v] += self.size[ulp_u]


# point 1
# ["DisjointSet", "unionByRank", "unionBySize", "find", "find"]
# [[5], [0, 1], [2, 3], [0, 1], [0, 3]]
# [null, null, null, true, false]
s1 = DisjointSet(5)
result1 = []
result1.append(s1.unionByRank(0, 1))
result1.append(s1.unionBySize(2, 3))
result1.append(s1.find(0, 1))
result1.append(s1.find(0, 3))

# point 2
# ["DisjointSet", "unionBySize", "unionBySize", "find", "find"]
# [[3], [0, 1], [1, 2], [0, 2], [0, 1]]
s2 = DisjointSet(3)
result2 = []
result2.append(s2.unionBySize(0, 1))
result2.append(s2.unionBySize(1, 2))
result2.append(s2.find(0, 2))
result2.append(s2.find(0, 1))

print(result1)
print(result2)
