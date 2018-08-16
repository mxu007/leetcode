# Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

# Example :

# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.

# The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

#           4
#         /   \
#       2      6
#      / \
#     1   3

# while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
# Note:

# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's value is different.

# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
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
