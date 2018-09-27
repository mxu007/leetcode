# Given a matrix A, return the transpose of A.

# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

# Example 1:

# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:

# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]

# https://leetcode.com/problems/transpose-matrix/

# 1) use a new nested list, O(MN) time and O(MN) space (for new nested list)
# where M,N are no.of rows and columns for the input matrix
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # init new matrix
        transpose_matrix = []

        # iterate through columns
        for j in range(0,len(A[0])):
            # construct columns from rows in A
            transpose_matrix.append(list(row[j] for row in A))

        return transpose_matrix

# 2) one-liner use zip and list
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(zip(*A))

# 3) simplification of 1)
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

# 4) reverse index sequence
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n_row,n_col=len(A),len(A[0])
        transpose_matrix=[[0]*n_row for i in range(n_col)]
        for i in range(n_row):
            for j in range(n_col):
                transpose_matrix[j][i]=A[i][j]
        return transpose_matrix
