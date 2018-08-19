# Given a binary tree, return the tilt of the whole tree.

# The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

# The tilt of the whole tree is defined as the sum of all nodes' tilt.

# Example:
# Input:
#          1
#        /   \
#       2     3
# Output: 1
# Explanation:
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1
# Note:

# The sum of node values in any subtree won't exceed the range of 32-bit integer.
# All the tilt values won't exceed the range of 32-bit integer.

# https://leetcode.com/problems/binary-tree-tilt/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1) efficient appraoch, from bottom up
class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # define self.result to make it accessible and be abled to update in the recursive call
        self.result = 0

        # recursive function to sum the left and right tree
        def recur_sum(root):
            # left-right-root traversal (post-order)
            if (not root):
                return 0
            left, right = recur_sum(root.left), recur_sum(root.right)
            # update result
            self.result += abs(left - right)
            # return sum of root, left and right and return to the parent
            return root.val + left + right

        # call the recur_sum function and update result
        recur_sum(root)

        return(self.result)

# less efficient appraoch
class Solution:
    def findTilt(self, root):
        # recursive function to calculate the tree sum
        def treeSum(root):
            if root == None:
                return 0
            else:
                return root.val + treeSum(root.left) + treeSum(root.right)

        # recursively fnd the tilt
        # total tilt equals root's left tree sum - root's right tree sum and plus tilts of left and right children
        if root == None:
            return 0
        else:
            return abs(treeSum(root.left) - treeSum(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)
