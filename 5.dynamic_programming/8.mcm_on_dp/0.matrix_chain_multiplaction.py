# Matrix chain multiplication
"""
Given a chain of matrices A1, A2, A3,.....An, you have to figure out the most efficient way to multiply these matrices.
In other words, determine where to place parentheses to minimize the number of multiplications.

Given an array nums of size n. Dimension of matrix Ai ( 0 < i < n ) is nums[i - 1] x nums[i].
Find a minimum number of multiplications needed to multiply the chain.
"""
"""
Example 1:
Input : nums = [10, 15, 20, 25]
Output : 8000
Explanation :
There are two ways to multiply the chain - A1*(A2*A3) or (A1*A2)*A3.
If we multiply in order- A1*(A2*A3), then number of multiplications required are 11250.
If we multiply in order- (A1*A2)*A3, then number of multiplications required are 8000.
Thus minimum number of multiplications required is 8000.


Example 2:
Input : nums = [4, 2, 3]
Output : 24
Explanation :
There is only one way to multiply the chain - A1*A2.
Thus minimum number of multiplications required is 24.
"""
"""
Constraints:
- 2 <= n <= 100
- 1 <= nums[i] <= 100
"""


class Solution:
    def matrixMultiplication(self, nums):
        # your code goes here
        pass
