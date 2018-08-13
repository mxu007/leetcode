
# Given a matrix A, return the transpose of A.

# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.



# Example 1:

# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:

# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]


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
