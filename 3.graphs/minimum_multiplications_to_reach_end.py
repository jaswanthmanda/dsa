from collections import deque

# Minimum multiplications to reach end
"""
Given start, end, and an array arr of n numbers.
At each step,
the start is multiplied by any number in the array and then a mod operation
with 100000 is done to get the new start.

Find the minimum steps in which the end can be achieved starting from the start.
If it is not possible to reach the end, then return -1.
"""
"""
Input: arr = [2, 5, 7], start = 3, end = 30
Output: 2
Explanation:
Step 1: 3*2 = 6 % 100000 = 6 
Step 2: 6*5 = 30 % 100000 = 30
Therefore, in minimum 2 multiplications, we reach the end number which is treated as a destination node of a graph here.

Input: arr = [3, 4, 65], start = 7, end = 66175
Output: 4
Explanation:
Step 1: 7*3 = 21 % 100000 = 21 
Step 2: 21*3 = 6 % 100000 = 63 
Step 3: 63*65 = 4095 % 100000 = 4095 
Step 4: 4095*65 = 266175 % 100000 = 66175
Therefore, in minimum 4 multiplications we reach the end number which is treated as a destination node of a graph here.
"""
"""
Constraints:
- 1 <= n <= 104
- 1 <= arr[i] <= 104
- 1 <= start, end < 105
"""


class Solution:
    def minimumMultiplications(self, arr, start, end):
        MOD = 100000
        dist = [-1] * MOD
        dist[start] = 0

        q = deque([start])

        while q:
            node = q.popleft()

            if node == end:
                return dist[node]

            for i in arr:
                newNode = (node * i) % MOD
                if dist[newNode] == -1:
                    dist[newNode] = dist[node] + 1
                    q.append(newNode)

        return -1


s = Solution()

k1 = s.minimumMultiplications([2, 5, 7], 3, 30)

k2 = s.minimumMultiplications([3, 4, 65], 7, 66175)

print(k1)
print(k2)
