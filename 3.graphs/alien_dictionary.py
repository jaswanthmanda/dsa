# Alien Dictionary
"""
Given a sorted dictionary of an alien language having N words and K starting alphabets of a standard dictionary.
Find the order of characters in the alien language.
There may be multiple valid orders for a particular test case, thus you may return any valid order as a string.
The output will be True if the order returned by the function is correct, else False denoting an incorrect order.
If the given arrangement of words is inconsistent with any possible letter ordering, return an empty string "".
"""
"""
Input: N = 5, K = 4, dict = ["baa","abcd","abca","cab","cad"]
Output: b d a c
Explanation: 
We will analyze every consecutive pair to find out the order of the characters.
The pair “baa” and “abcd” suggests 'b' appears before 'a' in the alien dictionary.
The pair “abcd” and “abca” suggests 'd' appears before 'a' in the alien dictionary.
The pair “abca” and “cab” suggests 'a' appears before 'c' in the alien dictionary.
The pair “cab” and “cad” suggests 'b' appears before 'd' in the alien dictionary.
So, ['b', 'd', 'a', 'c'] is a valid ordering.


Input: N = 3, K = 3, dict = ["caa","aaa","aab"]
Output: c a b
Explanation:
Similarly, if we analyze the consecutive pair
for this example, we will figure out ['c', 'a', 'b'] is
a valid ordering.
"""
"""
Constraints:
- 1 ≤ N, M ≤ 300
- 1 ≤ K ≤ 26
- 1 ≤ K ≤ 26
"""


class Solution:
    def findOrder(self, dict, N, K):
        # Build a adj list
        adj = {chr(97 + i): [] for i in range(K)}

        for i in range(N - 1):
            k = list(dict[i])
            lm = list(dict[i + 1])
            if len(k) > len(lm) and dict[i].startswith(dict[i+1]):
                return None

            kk = min(len(k), len(lm))
            for jk in range(kk):
                if k[jk] != lm[jk]:
                    # print(k[jk], lm[jk])
                    adj[k[jk]].append(lm[jk])
                    break

        visited = set()
        pathVis = set()
        stack = []

        def dfs(node):
            if node in pathVis:
                return None

            if node in visited:
                return stack

            pathVis.add(node)

            for nei in adj[node]:
                if dfs(nei) is None:
                    return None

            pathVis.remove(node)
            visited.add(node)
            stack.append(node)

            return stack

        for il in range(K):
            if dfs(chr(97 + il)) is None:
                return ""

        ans = ""
        while stack:
            chaa = stack.pop()
            ans += chaa

        return " ".join(ans)


s = Solution()

k1 = s.findOrder(
    [
        "baa",
        "abcd",
        "abca",
        "cab",
        "cad",
    ],
    5,
    4,
)

k2 = s.findOrder(
    [
        "caa",
        "aaa",
        "aab",
    ],
    3,
    3,
)

print(k1)
print(k2)
