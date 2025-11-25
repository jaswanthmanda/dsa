from collections import deque

# Word ladder II
"""
Given two distinct words startWord and targetWord,
and a list denoting wordList of unique words of equal lengths.
Find all shortest transformation sequence(s) from startWord to targetWord.
You can return them in any order possible.

In this problem statement, we need to keep the following conditions in mind:

A word can only consist of lowercase characters.
Only one letter can be changed in each transformation.
Each transformed word must exist in the wordList including the targetWord.
startWord may or may not be part of the wordList.
Return an empty list if there is no such transformation sequence.
"""
"""
Input: startWord = "der", targetWord = "dfs", wordList = ["des", "der", "dfr", "dgt", "dfs"]
Output: [ [ “der”, “dfr”, “dfs” ], [ “der”, “des”, “dfs”] ]
Explanation:
The length of the smallest transformation sequence here is 3.
Following are the only two shortest ways to get to the targetWord from the startWord:
"der" -> ( replace 'r' by 's' ) -> "des" -> ( replace 'e' by 'f') -> "dfs".
"der" -> ( replace 'e' by 'f' ) -> "dfr" -> ( replace 'r' by 's' ) -> "dfs".

Input: startWord = "gedk", targetWord= "geek", wordList = ["geek", "gefk"]
Output: [ [ “gedk”, “geek” ] ]
Explanation:
The length of the smallest transformation sequence here is 2.
Following is the only shortest way to get to the targetWord from the startWord :
"gedk" -> ( replace 'd' by 'e' ) -> "geek".
"""
"""
Constraints:
- N= Number of Words
- M= Length of Word
- 1 ≤ N ≤ 100
- 1 ≤ M ≤ 10
"""


class Solution:
    def findSequences(self, beginWord, endWord, wordList):
        ka = set(wordList)
        visited_level = set()
        visited_level.add(beginWord)
        q = deque([([beginWord], 0)])
        ans = []
        min_lev = float('inf')
        prev_lev = 0

        while q:
            stac, lev = q.popleft()

            if min_lev != float('inf') and lev > min_lev:
                return ans

            if prev_lev < lev:
                ka -= visited_level
                visited_level.clear()
                prev_lev = lev

            word = stac[-1]
            visited_level.add(word)
            if word == endWord:
                if min_lev > lev:
                    min_lev = lev
                if lev == min_lev:
                    ans.append(stac)
            else:
                for ch in range(len(word)):
                    for i in range(26):
                        wordLis = list(word)
                        wordLis[ch] = chr(97 + i)
                        temp_word = "".join(wordLis)

                        if temp_word in ka and temp_word not in visited_level:
                            kk = stac + [temp_word]
                            # visited_level.add(temp_word)
                            q.append((kk, lev + 1))

        return ans


s = Solution()

k1 = s.findSequences(
    "der",
    "dfs",
    [
        "des",
        "der",
        "dfr",
        "dgt",
        "dfs",
    ],
)

k2 = s.findSequences(
    "gedk",
    "geek",
    [
        "geek",
        "gefk",
    ],
)

print(k1)
print(k2)
