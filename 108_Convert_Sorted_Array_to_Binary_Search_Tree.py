# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:

# Given the sorted array: [-10,-3,0,5,9],

# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
# https://www.geeksforgeeks.org/sorted-array-to-balanced-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        # if empty input list
        if (not nums):
            return None
        # get the middle of input list
        middle = (len(nums)) // 2
        # set the root
        root = TreeNode(nums[middle])
        # recursively call for left and right children
        print(nums, middle, nums[:middle])
        root.left = self.sortedArrayToBST(nums[:middle])
        print(nums, middle, nums[middle+1:])
        root.right = self.sortedArrayToBST(nums[middle+1:])

        return root

# Your input
# [-10,-3,0,5,9]
# Your stdout
# [-10, -3, 0, 5, 9] 2 [-10, -3]
# [-10, -3] 1 [-10]
# [-10] 0 []
# [-10] 0 []
# [-10, -3] 1 []
# [-10, -3, 0, 5, 9] 2 [5, 9]
# [5, 9] 1 [5]
# [5] 0 []
# [5] 0 []
# [5, 9] 1 []
