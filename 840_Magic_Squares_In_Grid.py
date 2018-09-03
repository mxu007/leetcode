# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

# Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).



# Example 1:

# Input: [[4,3,8,4],
#         [9,5,1,9],
#         [2,7,6,2]]
# Output: 1
# Explanation:
# The following subgrid is a 3 x 3 magic square:
# 438
# 951
# 276

# while this one is not:
# 384
# 519
# 762

# In total, there is only one magic square inside the given grid.
# Note:

# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# 0 <= grid[i][j] <= 15

# https://leetcode.com/problems/magic-squares-in-grid/description/

# 1) iterate the nested list
class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # function to check 3x3 list of list whether is a magic grid
        def check_magic(square):
            # flatten the input nested list
            flatten_square = [item for sublist in square for item in sublist]
            # unique, all smaller than 10
            if len(flatten_square) != len(set(flatten_square)) or sum(flatten_square)!=45 or any(item >=10 for item in flatten_square):
                return False
            # check row, column and diag sum
            row = sum(square[0]) == sum(square[1]) == sum(square[2])
            column = sum([row[0] for row in square]) == sum([row[1] for row in square]) == sum([row[2] for row in square])
            diag = sum([square[0][0],square[1][1],square[2][2]]) == sum([square[0][2],square[1][1],square[2][0]])
            return row and column and diag

        count = 0
        row_len = len(grid)
        col_len = len(grid[0])
        for i in range(0,row_len-3+1):
            for j in range(0, col_len-3+1):
                if check_magic([row[j:j+3] for row in grid[i:i+3]]): count += 1

        return count


# 2) use numpy array
import numpy as np
class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # function to check 3x3 list of list whether is a magic grid
        def check_magic(square):
            # unique, all smaller than 10
            if len(np.unique(square)) != 9  or np.sum(square)!=45 or np.any(square >= 10): return False
            # check row, column and diag sum
            row = np.sum(square[0,:]) == np.sum(square[1,:]) == np.sum(square[2,:])
            column = np.sum(square[:,0]) ==np.sum(square[:,1]) == np.sum(square[:,2])
            diag = sum([square[0,0],square[1,1],square[2,2]]) == sum([square[0,2],square[1,1],square[2,0]])
            return row and column and diag

        count = 0
        row_len = len(grid)
        col_len = len(grid[0])
        grid = np.array(grid)
        for i in range(0,row_len-3+1):
            for j in range(0, col_len-3+1):
                if check_magic(grid[i:i+3,j:j+3]): count += 1
        return count
