# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



# Example:

# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16

# Explanation: The perimeter is the 16 yellow stripes in the image below:

# 1) nested loop and dynamic programming
# O(MN) time complexity, O(1) space
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        perimeter = 0

        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    offset = (1 if (i-1>=0 and grid[i-1][j]==1) else 0)+ (1 if (j-1>=0 and grid[i][j-1]==1) else 0) + (1 if (i+1<m and grid[i+1][j]==1) else 0) + (1 if (j+1<n and grid[i][j+1]==1) else 0)
                    perimeter += (4 - offset)
                    #print((i,j),offset,perimeter)
        return perimeter

