# We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.

# Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

# Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:

# Given the 8 x 8 grid below, we want to construct the corresponding quad tree:



# It can be divided according to the definition above:


# The corresponding quad tree should be as following, where each node is represented as a (isLeaf, val) pair.

# For the non-leaf nodes, val can be arbitrary, so it is represented as *.



# Note:

# N is less than 1000 and guaranteened to be a power of 2.
# If you want to know more about the quad tree, you can refer to its wiki.

# https://leetcode.com/problems/construct-quad-tree/description/


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

# 1) elegant using recursive call
class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        # get size of the input
        N = len(grid)
        # when input is empty
        if N == 0:
            return None
        # if all grid elements equal 1 or 0, use all function
        # https://docs.python.org/3/library/functions.html#all
        elif all(grid[i][j] == 1 for i in range(N) for j in range(N)):
            return Node(True, True, None, None, None, None)
        elif all(grid[i][j] == 0 for i in range(N) for j in range(N)):
            return Node(False, True, None, None, None, None)
        # subset grid into topleft, topright, bottomleft and bottomright and perform recursive call
        else:
            half = (N+1) // 2
            topleft = [ x[:half] for x in grid[:half]]
            topright = [ x[half:] for x in grid[:half]]
            bottomleft = [ x[:half] for x in grid[half:]]
            bottomright = [ x[half:] for x in grid[half:]]
            return Node(None, False, self.construct(topleft), self.construct(topright), self.construct(bottomleft), self.construct(bottomright))


# 2) top-down them bottom-up approach, more complex
class Solution:
    def construct(self, grid):
        def dfs(i, j, N):
            # handle case where only single element as input
            if N == 1:
                node = Node(grid[i][j] == 1, True, None, None, None, None)
            else:
                # get topleft, topright, bottomleft and bottomright thru recursive call
                topleft = dfs(i, j, N // 2)
                topright = dfs(i, j + N // 2, N // 2)
                bottomleft = dfs(i + N // 2, j, N// 2)
                bottomright = dfs(i + N // 2, j + N // 2, N // 2)
                # set Node if topleft, topright, bottomleft and bottomright all equal to 0 or 1
                # value of non-left node can be arbitrary
                value = topleft.val
                if topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf and topleft.val == topright.val == bottomleft.val == bottomright.val:
                    node = Node(value, True, None, None, None, None)
                # not homogeneous topleft, topright, bottomleft and bottomright
                else:
                    node = Node(value, False, topleft, topright, bottomleft, bottomright)
            return node
        return grid and dfs(0, 0, len(grid)) or None

