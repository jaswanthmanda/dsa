# Fruit into basket


class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        # n
        n = len(fruits)

        i = 0
        j = 1
        curr = 1
        hash_map = {}
        hash_map[fruits[i]] = 1

        ans = 0

        while j < n:
            hash_map[fruits[j]] = hash_map.get(fruits[j], 0) + 1
            curr += 1

            # shrink if more than 2 types
            while len(hash_map) > 2:
                if hash_map[fruits[i]] > 1:
                    hash_map[fruits[i]] -= 1
                else:
                    del hash_map[fruits[i]]
                i += 1
                curr -= 1

            ans = max(ans, curr)
            j += 1

        return ans
