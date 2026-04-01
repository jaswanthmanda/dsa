# Word Search 1

from typing import List


def present(
    board: List[List[str]],
    word: str,
    n: int,
    m: int,
) -> bool:
    # Write your code here
    m = len(board)
    n = len(board)

    def dfs(i, j, k):
        # k = index in word

        # if all characters matched
        if k == len(word):
            return True

        # out of bound or mismatch
        if i < 0 or j < 0 or i >= n or j >= n or board[i][j] != word[k]:
            return False

        # mark visited
        temp = board[i][j]
        board[i][j] = "#"

        # explore 4 directions
        found = (
            dfs(i + 1, j, k + 1)
            or dfs(i - 1, j, k + 1)
            or dfs(i, j - 1, k + 1)
            or dfs(i, j + 1, k + 1)
        )

        # backtract
        board[i][j] = temp

        return found

    for i in range(n):
        for j in range(m):
            if dfs(i, j, 0):
                return True

    return False
