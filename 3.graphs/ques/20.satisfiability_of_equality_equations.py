# Satisfiablity of equality equations
"""
You are given an array of strings equations that represent relationships between variables where
each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".
Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy
all the given equations, or false otherwise.
"""
"""
Example 1:
Input: equations = ["a==b","b!=a"]
Output: false
Explanation:
If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.


Example 2:
Input: equations = ["b==a","a==b"]
Output: true
Explanation:
We could assign a = 1 and b = 1 to satisfy both equations.
"""
"""
Constraints:
- 1 <= equations.length <= 500
- equations[i].length == 4
- equations[i][0] is a lowercase letter.
- equations[i][1] is either '=' or '!'.
- equations[i][2] is '='.
- equations[i][3] is a lowercase letter.
"""


class DisjointSet:
    def __init__(self, V):
        self.nodes = [i for i in range(V)]
        self.parents = [i for i in range(V)]
        self.sizes = [1 for i in range(V)]

    def findUPar(self, u):
        if u == self.parents[u]:
            return u

        self.parents[u] = self.findUPar(self.parents[u])

        return self.parents[u]

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return

        if self.sizes[ulp_u] < self.sizes[ulp_v]:
            self.parents[ulp_u] = ulp_v
            self.sizes[ulp_v] += self.sizes[ulp_u]
        else:
            self.parents[ulp_v] = ulp_u
            self.sizes[ulp_u] += self.sizes[ulp_v]


class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        ds = DisjointSet(26)

        for edge in equations:
            if "==" in edge:
                kemp = edge.split("==")
                u1 = kemp[0]
                u2 = kemp[1]

                ka1 = ord(u1) - 97
                ka2 = ord(u2) - 97

                ds.unionBySize(ka1, ka2)

        for edge in equations:
            if "!=" in edge:
                kemp = edge.split("!=")
                u1 = kemp[0]
                u2 = kemp[1]

                ka1 = ord(u1) - 97
                ka2 = ord(u2) - 97

                ulp_k1 = ds.findUPar(ka1)
                ulp_k2 = ds.findUPar(ka2)

                if ulp_k1 == ulp_k2:
                    return False

        return True


s = Solution()

k1 = s.equationsPossible(["a==b", "b!=a"])

k2 = s.equationsPossible(["b==a", "a==b"])

k3 = s.equationsPossible(
    [
        "a==b",
        "b!=c",
        "c==a",
    ]
)

print(k1)
print(k2)
print(k3)
