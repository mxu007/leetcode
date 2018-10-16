# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


# Example 1:

# Input:
# matrix = [
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ]
# Output: True
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.
# Example 2:

# Input:
# matrix = [
#   [1,2],
#   [2,2]
# ]
# Output: False
# Explanation:
# The diagonal "[1, 2]" has different elements.

# Note:

# matrix will be a 2D array of integers.
# matrix will have a number of rows and columns in range [1, 20].
# matrix[i][j] will be integers in range [0, 99].

# https://leetcode.com/problems/toeplitz-matrix/description/[]

# 1) use list comprehension, O(MN) where M is row count and N is column count
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # height and width
        h, w = len(matrix), len(matrix[0])

        # get diagonal elements
        # https://stackoverflow.com/questions/23069388/listing-elements-in-a-nested-lists-diagonally
        diagonals = [[matrix[h-1-q][p-q] for q in range(min(p, h-1), max(0, p-w+1)-1, -1)] for p in range(h+w-1)]
        print(diagonals)

        # check by each diagonal
        for diagonal in diagonals:
            if len(set(diagonal)) > 1:
                return False
        return True


# 2) use numpy array
# https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python/6313407#6313407
import numpy as np
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        matrix = np.array(matrix)
        diags = [matrix.diagonal(i) for i in range(-matrix.shape[0]+1, matrix.shape[1])]
        return all([len(set(diag))==1 for diag in diags])

# 3) one-liner using numpy of 2)
import numpy as np
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all([len(set(diag))==1 for diag in [np.array(matrix).diagonal(i) for i in range(-np.array(matrix).shape[0]+1, np.array(matrix).shape[1])]])

# 4) adding offset to each row and get column items
# 1 2 3    |X|X|1|2|3|    | | |1|2|3|
# 4 5 6 => |X|4|5|6|X| => | |4|5|6| | => [[7],[4,8],[1,5,9],[2,6],[3]]
# 7 8 9    |7|8|9|X|X|    |7|8|9| | |
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        def get_rows(grid):
            return [[c for c in r] for r in grid]

        def get_cols(grid):
            return zip(*grid)

        b = [None] * (len(matrix) - 1)
        matrix = [b[i:] + r + b[:i] for i, r in enumerate(get_rows(matrix))]
        return all([len(set([c for c in r if c is not None]))==1 for r in get_cols(matrix)])

# 5) check current row with next row, O(MN) time, read two rows at a time
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        i = 0
        while i < len(matrix) - 1:
            if matrix[i][:-1] != matrix[i+1][1:]:
                return False
            i += 1
        return True

# 6) one-liner of 5)
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all(matrix[i][:-1] == matrix[i+1][1:] for i in range(len(matrix)-1))

# 7) variant of 5), scan row by row, pop last element of current row and compare with next row
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if matrix is None:
            return False

        for x in matrix:
            index = matrix.index(x)
            print(x, index)
            if index == len(matrix)-1:
                return True
            print(x.pop())
            if x != matrix[index+1][1:]:
                return False
        return True

# 8) one-liner of 7) and 5), in 5) it checks row by row, in 8) it checks element by element
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all([matrix[i][j] == matrix[i+1][j+1] for i in range(len(matrix)-1) for j in range(len(matrix[0])-1)])
