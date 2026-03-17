# greedy

"""
Greedy Intuition

1. Greedy choice: Always pick the “best” option locally at each step.

2. Optimal substructure: Choosing the local optimum at each step leads to a global optimum.

3. Check: Sorting is often the first step (by end time, by weight/value ratio, etc.).

Common patterns:

- Interval scheduling / activity selection → sort by end time.

- Minimize coins / change → pick largest denomination first.

- Huffman coding / frequency-based → pick least frequent nodes.

- Task scheduling → pick task with earliest deadline.
"""


def greedy_problems(items):
    # Step 1: sort according to greedy criterion
    items.sort(key=lambda x: x[1])

    result = []
    current = 0  # or some initial value

    for item in items:
        if item[0] >= current:
            result.append(item)
            current = item[1]

    return result


# Example usage: Interval scheduling
intervals = [(1, 3), (2, 5), (3, 6)]
print(greedy_problems(intervals))  # output: [(1, 3), (2, 6)]

"""
Key Points:
- Sort first -> most greedy algorithms start with a sort
- Pick & update state -> decide if current choice is feasible
- No backtracking -> greedy is fast but only works greedy choice property holds
"""
