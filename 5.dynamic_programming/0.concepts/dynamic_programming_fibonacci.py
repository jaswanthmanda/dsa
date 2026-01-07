from datetime import datetime

# Dynamic Programming Fibonacci
"""
Dynamic programming can be applied where we can split a big problem into overlapping sub-problems (overlapping recursions) (indication)

Dynamic programming consists of two methods:
- Memoization
- tabulation

Memoization (top-down approach):
Memoization is the concept where we will have to save already solved problem step which is to memorize the result and use if after wards

Tabulation (bottom-up approach):
solving the problem by filling table from the smallest cases up to the final answer,
where we start from the very bottom cases and try to solve towards up in this we could optimize time and space.
"""

# N
N = 25


# Normal fibo (using recursion)
def normal_fibo(n: int):
    if n <= 1:
        return n

    return normal_fibo(n - 1) + normal_fibo(n - 2)


# fibonacci using dynamic programming (memoization method)
# top-down approach
# maintain a dp array to store already processed result
dp = [-1] * (N + 1)


def fibo_memoization_recursion(n: int, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fibo_memoization_recursion(n - 1, dp) + fibo_memoization_recursion(n - 2, dp)

    return dp[n]


# fibonacci using memoization eliminating recursion stack space
# top-down approach (for loop)
def fibo_memoization_for_loop(n: int):
    # maintain the same dp array as shown above
    dp = [-1] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# fibonacci using dynamic programming (tabulation method)
# bottom-up approach
def fibo_tabulation(n: int):
    # handle edge case
    if n <= 1:
        return n

    # maintain prev var's which is the smallest case
    # and switch the prev vars such that there is no space complexity
    prev2 = 0
    prev = 1
    curr = 0

    for i in range(2, n + 1):
        curr = prev2 + prev
        prev2 = prev
        prev = curr

    return curr


# normal fibo
timer_start = datetime.now()

k1 = normal_fibo(N)

print("1,", datetime.now() - timer_start)

# fibo using dp arr (recursion)
timer_start = datetime.now()
k2 = fibo_memoization_recursion(N, dp)

print("2,", datetime.now() - timer_start)

# fibo using dp arr (memoization - for loop)
timer_start = datetime.now()
k3 = fibo_memoization_for_loop(N)

print("3,", datetime.now() - timer_start)

# fibo using tabulation (no space compl.)
timer_start = datetime.now()
k4 = fibo_tabulation(N)

print("4,", datetime.now() - timer_start)

print(k1)
print(k2)
print(k3)
print(k4)
