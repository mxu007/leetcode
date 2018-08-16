# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

# Example:

# Input:

#    1
#     \
#      3
#     /
#    2

# Output:
# 1

# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
# Note: There are at least two nodes in this BST.

# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # init list to store values of nodes in traversal
        nodes = []

        # in order traversal to build the sorted list of node values
        # left-root-right, as it is BST, it is weakly sorted
        def preorder_traversal(root,nodes):
            if root:
                preorder_traversal(root.left,nodes)
                nodes.append(root.val)
                preorder_traversal(root.right,nodes)
            return

        # function to find the minimum diff
        # iterate from left to right as the input list is already sorted
        def find_min_diff(nodes):
            diff = 10**20
            for i in range(0,len(nodes)-1):
                if nodes[i+1] - nodes[i] < diff:
                    diff = nodes[i+1] - nodes[i]
            return diff

        preorder_traversal(root,nodes)
        return(find_min_diff(nodes))
