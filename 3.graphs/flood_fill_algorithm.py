from collections import deque

# Flood fill algorithm
"""
An image is represented by a 2-D array of integers,
each integer representing the pixel value of the image.
Given a coordinate (sr, sc) representing the starting pixel
(row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a flood fill, consider the starting pixel,
plus any pixels connected 4-directionally to the starting pixel of
the same colour as the starting pixel, plus any pixels connected 4-directionally
to those pixels (also with the same colour as the starting pixel), and so on.
Replace the colour of all of the aforementioned pixels with the newColor.
"""

"""
Examples:

Input: image = [ [1, 1, 1], [1, 1, 0], [1, 0, 1] ], sr = 1, sc = 1, newColor = 2
Output: [ [2, 2, 2], [2, 2, 0], [2, 0, 1] ]
Explanation:
From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel),
all pixels connected
by a path of the same color as the starting pixel
(i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2,
because it is not 4-directionally connected to the starting pixel.


Input: image = [ [0, 1, 0], [1, 1, 0], [0, 0, 1] ], sr = 2, sc = 2, newColor = 3
Output: [ [0, 1, 0], [1, 1, 0], [0, 0, 3] ]
Explanation: Starting from the pixel at position (2, 2) (i.e., the blue pixel), we flood fill all adjacent pixels that have the same color as the starting pixel. In this case, only the pixel at position (2, 2) itself is of the same color. So, only that pixel gets colored with the new color, resulting in the updated image.
"""

"""
Constraints:
·  n == image.length

·  m == image[i].length

·  1 <= m, n <= 50

·  0 <= image[i][j], color < 216

·  0 <= sr < n

·  0 <= sc < m
"""


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        visited = set()
        m = len(image)
        n = len(image[0])
        mewVal = image[sr][sc]
        import copy

        newPixel = copy.deepcopy(image)

        q = deque([(sr, sc)])
        visited.add((sr, sc))

        while q:
            node = q.popleft()
            r = node[0]
            c = node[1]
            newPixel[r][c] = newColor

            vals = [
                (r - 1, c),
                (r, c - 1),
                (r+1, c),
                (r, c + 1),
            ]

            for val in vals:
                a, b = val
                if 0 <= a < m and 0 <= b < n:
                    if image[a][b] == mewVal and (a, b) not in visited:
                        visited.add((a, b))
                        q.append((a, b))

        return newPixel


s = Solution()
k1 = s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
k2 = s.floodFill([[0, 1, 0], [1, 1, 0], [0, 0, 1]], 2, 2, 3)
print(k1)
print(k2)
