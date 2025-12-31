import heapq

# Maximize amount after two days of conversions
"""
You are given a string initialCurrency, and you start with 1.0 of initialCurrency.

You are also given four arrays with currency pairs (strings) and rates (real numbers):

- pairs1[i] = [startCurrencyi, targetCurrencyi] denotes that you can convert from startCurrencyi to targetCurrencyi at a rate of rates1[i] on day 1.

- pairs2[i] = [startCurrencyi, targetCurrencyi] denotes that you can convert from startCurrencyi to targetCurrencyi at a rate of rates2[i] on day 2.

- Also, each targetCurrency can be converted back to its corresponding startCurrency at a rate of 1 / rate.

You can perform any number of conversions, including zero, using rates1 on day 1, followed by any number of additional conversions, including zero, using rates2 on day 2.

Return the maximum amount of initialCurrency you can have after performing any number of conversions on both days in order.

Note: Conversion rates are valid, and there will be no contradictions in the rates for either day.
The rates for the days are independent of each other.
"""
"""
Example 1:
Input: initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0,3.0], pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], rates2 = [4.0,5.0,6.0]
Output: 720.00000
Explanation:
To get the maximum amount of EUR, starting with 1.0 EUR:

- On Day 1:
 - Convert EUR to USD to get 2.0 USD.
 - Convert USD to JPY to get 6.0 JPY.
- On Day 2:
 - Convert JPY to USD to get 24.0 USD.
 - Convert USD to CHF to get 120.0 CHF.
 - Finally, convert CHF to EUR to get 720.0 EUR.

Example 2:
Input: initialCurrency = "NGN", pairs1 = [["NGN","EUR"]], rates1 = [9.0], pairs2 = [["NGN","EUR"]], rates2 = [6.0]
Output: 1.50000
Explanation:
Converting NGN to EUR on day 1 and EUR to NGN using the inverse rate on day 2 gives the maximum amount.

Example 3:
Input: initialCurrency = "USD", pairs1 = [["USD","EUR"]], rates1 = [1.0], pairs2 = [["EUR","JPY"]], rates2 = [10.0]
Output: 1.00000
Explanation:
In this example, there is no need to make any conversions on either day.
"""
"""
Constraints:
- 1 <= initialCurrency.length <= 3
- initialCurrency consists only of uppercase English letters.
- 1 <= n == pairs1.length <= 10
- 1 <= m == pairs2.length <= 10
- pairs1[i] == [startCurrencyi, targetCurrencyi]
- pairs2[i] == [startCurrencyi, targetCurrencyi]
- 1 <= startCurrencyi.length, targetCurrencyi.length <= 3
- startCurrencyi and targetCurrencyi consist only of uppercase English letters.
- rates1.length == n
- rates2.length == m
- 1.0 <= rates1[i], rates2[i] <= 10.0
- The input is generated such that there are no contradictions or cycles in the conversion graphs for either day.
- The input is generated such that the output is at most 5 * 1010.
"""


class Solution(object):
    def maxAmount(self, initialCurrency, pairs1, rates1, pairs2, rates2):
        """
        :type initialCurrency: str
        :type pairs1: List[List[str]]
        :type rates1: List[float]
        :type pairs2: List[List[str]]
        :type rates2: List[float]
        :rtype: float
        """
        items = set()

        for u, v in pairs1:
            items.add(u)
            items.add(v)

        for u, v in pairs2:
            items.add(u)
            items.add(v)

        dist = [
            {item: {item1: 0.0 for item1 in items} for item in items},
            {item: {item1: 0.0 for item1 in items} for item in items},
        ]

        # insert 0's
        for item in items:
            dist[0][item][item] = 1.0
            dist[1][item][item] = 1.0

        # insert rate 1 vals
        for rate, kk in zip(rates1, pairs1):
            x, y = kk[0], kk[1]

            dist[0][x][y] = rate
            dist[0][y][x] = 1/rate

        # floyd warshall algo
        # rate 1
        for itemk in items:
            for itemi in items:
                for itemj in items:
                    dist[0][itemi][itemj] = max(dist[0][itemi][itemj], dist[0][itemi][itemk] * dist[0][itemk][itemj])

        # insert rate 2 vals
        for rate, kk in zip(rates2, pairs2):
            x, y = kk[0], kk[1]

            dist[1][x][y] = rate
            dist[1][y][x] = 1/rate

        # floyd warshall algo
        # rate 2
        for itemk in items:
            for itemi in items:
                for itemj in items:
                    dist[1][itemi][itemj] = max(dist[1][itemi][itemj], dist[1][itemi][itemk] * dist[1][itemk][itemj])

        # combine both days
        ans = 1.0
        for mid in items:
            ans = max(ans, dist[0][initialCurrency][mid] * dist[1][mid][initialCurrency])

        return ans


s = Solution()

k1 = s.maxAmount(
    "EUR",
    [
        ["EUR", "USD"],
        ["USD", "JPY"],
    ],
    [
        2.0,
        3.0,
    ],
    [
        ["JPY", "USD"],
        ["USD", "CHF"],
        ["CHF", "EUR"],
    ],
    [
        4.0,
        5.0,
        6.0,
    ],
)

k2 = s.maxAmount(
    "NGN",
    [
        ["NGN", "EUR"],
    ],
    [
        9.0,
    ],
    [
        ["NGN", "EUR"],
    ],
    [
        6.0,
    ],
)

k3 = s.maxAmount(
    "USD",
    [
        ["USD", "EUR"],
    ],
    [
        1.0,
    ],
    [
        ["EUR", "JPY"],
    ],
    [
        10.0,
    ],
)

print(k1)
print(k2)
print(k3)
