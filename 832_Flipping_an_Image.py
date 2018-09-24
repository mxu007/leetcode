# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

# Example 1:

# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# Example 2:

# Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Notes:

# 1 <= A.length = A[0].length <= 20
# 0 <= A[i][j] <= 1

# https://leetcode.com/problems/flipping-an-image/description/

# 1) O(NM) time, where M is no.of rows and N is no.of columns
# iterate the row, flipped and reverse
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B=[]
        for vec in A:
            bits = []
            for num in vec:
                bits.append(1) if num==0 else bits.append(0)
            B.append(bits[::-1])

        return B

# 2) 1-digit to get the binary reverse
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i] = [(1- digit) for digit in A[i]][::-1]
            print(A[i])
        return A

# 3) one-liner
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return ([[1- digit for digit in row][::-1] for row  in A])

# 4) variant of 3
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return ([[digit^1 for digit in row[-1::-1]] for row  in A])
