# On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

# Now we view the projection of these cubes onto the xy, yz, and zx planes.

# A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.

# Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

# Return the total area of all three projections.

# Input: [[1,2],[3,4]]
# Output: 17
# Explanation:
# Here are the three projections ("shadows") of the shape made with each axis-aligned plane.

# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 14


class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # initialize top, side1 and side2
        top, side_1, side_2 = 0, 0, 0

        # flatten the origianl list of list (2d-array)
        flat_list = [item for sublist in grid for item in sublist]
        top = sum(k >0 for k in flat_list)

        # iterate thru the row
        for i in (grid):
            side_1 += max(i)
        # iterate thru the column
        for j in range(0,len(grid[0])):
            side_2 += max(row[j] for row in grid)

        return (top+side_1+side_2)

