from collections import deque

# Word ladder I
"""
Given are the two distinct words startWord and targetWord,
and a list of size N, denoting wordList of unique words of equal size M.
Find the length of the shortest transformation sequence from startWord to targetWord.

Keep the following conditions in mind:
- A word can only consist of lowercase characters.
- Only one letter can be changed in each transformation.
- Each transformed word must exist in the wordList including the targetWord.
- startWord may or may not be part of the wordList

Note:
If there's no possible way to transform the sequence from startWord to targetWord return 0.
"""

"""
Input: wordList = ["des","der","dfr","dgt","dfs"], startWord = "der", targetWord = "dfs"
Output: 3
Explanation:
- The length of the smallest transformation sequence from "der" to "dfs" is 3
- i.e. "der" -> (replace ‘e’ by ‘f’) -> "dfr" -> (replace ‘r’ by ‘s’) -> "dfs".
- So, it takes 3 different strings for us to reach the targetWord. Each of these strings are present in the wordList.


Input: wordList = ["geek", "gefk"], startWord = "gedk", targetWord= "geek"
Output: 2
Explanation:
- The length of the smallest transformation sequence from "gedk" to "geek" is 2
- i.e. "gedk" -> (replace ‘d’ by ‘e’) -> "geek" .
- So, it takes 2 different strings for us to reach the targetWord. Each of these strings are present in the wordList.
"""
"""
Constraints:
- 1 ≤ wordList.length ≤ 100
- 1 ≤ wordList[i].length ≤ 10
- startWord.length == targetWord.length == wordList[i].length
- startWord, targetWord, and wordList[i] consist of lowercase English letters.
- startWord!= targetWord
"""


class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        ka = set(wordList)
        visited = set()
        q = deque()

        q.append((startWord, 1))

        while q:
            word, level = q.popleft()
            # print(word, level)

            if word == targetWord:
                return level

            for cha in range(len(word)):
                for i in range(26):
                    wordLis = list(word)
                    wordLis[cha] = chr(97 + i)
                    temp_word = "".join(wordLis)
                    if temp_word in ka and temp_word not in visited:
                        visited.add(temp_word)
                        q.append((temp_word, level + 1))

        return 0


s = Solution()

k1 = s.wordLadderLength(
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

k2 = s.wordLadderLength(
    "gedk",
    "gefk",
    [
        "geek",
        "gefk",
    ],
)

print(k1)
print(k2)
