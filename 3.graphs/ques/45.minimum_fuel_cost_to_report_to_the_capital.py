from collections import deque

# Minimum fuel cost to report to the capital
"""
There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities
numbered from 0 to n - 1 and exactly n - 1 roads.
The capital city is city 0.
You are given a 2D integer array roads where roads[i] = [ai, bi] denotes
that there exists a bidirectional road connecting cities ai and bi.

There is a meeting for the representatives of each city. The meeting is in the capital city.

There is a car in each city. You are given an integer seats that indicates the number of seats in each car.

A representative can use the car in their city to travel or change the car and ride with another representative.
The cost of traveling between two cities is one liter of fuel.

Return the minimum number of liters of fuel to reach the capital city.
"""
"""
Example 1:
Input: roads = [[0,1],[0,2],[0,3]], seats = 5
Output: 3
Explanation:
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative2 goes directly to the capital with 1 liter of fuel.
- Representative3 goes directly to the capital with 1 liter of fuel.
It costs 3 liters of fuel at minimum.
It can be proven that 3 is the minimum number of liters of fuel needed.


Example 2:
Input: roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
Output: 7
Explanation:
- Representative2 goes directly to city 3 with 1 liter of fuel.
- Representative2 and representative3 go together to city 1 with 1 liter of fuel.
- Representative2 and representative3 go together to the capital with 1 liter of fuel.
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative5 goes directly to the capital with 1 liter of fuel.
- Representative6 goes directly to city 4 with 1 liter of fuel.
- Representative4 and representative6 go together to the capital with 1 liter of fuel.
It costs 7 liters of fuel at minimum.
It can be proven that 7 is the minimum number of liters of fuel needed.

Example 3:
Input: roads = [], seats = 1
Output: 0
Explanation:
No representatives need to travel to the capital city.
"""
"""
Constraints:
- 1 <= n <= 105
- roads.length == n - 1
- roads[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- roads represents a valid tree.
- 1 <= seats <= 105
"""

"""
from math import ceil
from collections import defaultdict

class Solution:
    def minimumFuelCost(self, roads, seats):
        if not roads:
            return 0
        
        adj = defaultdict(list)
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)
        
        self.fuel = 0
        
        def dfs(u, parent):
            people = 1  # representative of city u
            
            for v in adj[u]:
                if v == parent:
                    continue
                child_people = dfs(v, u)
                
                # Cars needed for child subtree to move up to u
                cars = (child_people + seats - 1) // seats
                self.fuel += cars
                
                people += child_people
            
            return people
        
        dfs(0, -1)
        return self.fuel
"""


class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        if len(roads) == 0:
            return 0

        # build adjlist
        n = roads[0][0]
        for u, v in roads:
            n = max(n, u, v)

        n = n + 1

        adjlist = {i: [] for i in range(n)}
        indegree = [0 for i in range(n)]
        for u, v in roads:
            adjlist[u].append(v)
            adjlist[v].append(u)

        return sum(dist)


s = Solution()

k1 = s.minimumFuelCost([[0, 1], [0, 2], [0, 3]], 5)

k2 = s.minimumFuelCost([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2)

print(k1)
print(k2)
