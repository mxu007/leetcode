# On a N * N grid, we place some 1 * 1 * 1 cubes.

# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

# Return the total surface area of the resulting shapes.



# Example 1:

# Input: [[2]]
# Output: 10
# Example 2:

# Input: [[1,2],[3,4]]
# Output: 34
# Example 3:

# Input: [[1,0],[0,2]]
# Output: 16
# Example 4:

# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 32
# Example 5:

# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 46


# Note:

# 1 <= N <= 50
# 0 <= grid[i][j] <= 50

# https://leetcode.com/problems/surface-area-of-3d-shapes/description/

# https://leetcode.com/problems/surface-area-of-3d-shapes/discuss/163414/C%2B%2BJava1-line-Python-Minus-Hidden-Area/169349
# 1) subtract hidden area due to intersection with neighboring tower, think like tower by tower
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # init
        N,result = len(grid),0
        for i in range(N):
            for j in range(N):
                # add to result
                if grid[i][j]:
                    result += 2 + 4* grid[i][j]
                # subtract hidden surface due to intersaction with other tower on same column (same j)
                # since both tower lost the joined surface, hence * 2
                # shared surface is min height between two neighboring joined tower
                if i: result -= min(grid[i][j],grid[i-1][j]) * 2
                # subtract hidden surface due to intersaction with other tower on same row (same i)
                if j: result -= min(grid[i][j],grid[i][j-1]) * 2

        return result


# 2) for each tower, alwasy add top and bottom (+=2), then look at north,east,south and west towers and compare height
# add non-intersected area
class Solution(object):
    def surfaceArea(self, grid):
        N = len(grid)

        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0
                        ans += max(grid[r][c] - nval, 0)

        return ans

