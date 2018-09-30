# Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

# For example,

# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3

# And the value to search: 2
# You should return this subtree:

#       2
#      / \
#     1   3
# In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

# Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

# 1) binary search, O(log(N)) time for height balanced tree
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # case where root is null
        if root is None:
            return []
        # case where root.val matches with target value
        elif root.val == val:
            return root
        # as it is binary serach tree, if val is greater than root.val
        # we shall search the right child of root
        elif root.val < val:
            return self.searchBST(root.right, val)
        # search left child of root if target val is smaller than root.val
        return self.searchBST(root.left, val)

# 2) variant of 1)
class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root and val < root.val:
            return self.searchBST(root.left, val)
        elif root and val > root.val:
            return self.searchBST(root.right, val)
        return root

# 3）iterative solution by moving the head/root based on the value comparing with val
# O(N) time
class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root and val < root.val:
            return self.searchBST(root.left, val)
        elif root and val > root.val:
            return self.searchBST(root.right, val)
        return root

# 4) use stack to store the nodes, last-in first-out properties to simulate the recursive call
# O(N) time for worst-case, average O(log(N)) time
class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        stack = [root]
        while(len(stack)>0 and root):
            root = stack.pop()
            if root and root.val == val:
                return root
            elif root and root.val < val:
                stack.append(root.right)
            elif root and root.val > val:
                stack.append(root.left)
        return root

# 5) Morris Traversal O(N) time and O(1) space
# https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        current, pre = root, None
        while current:
            print(current.val)
            if current.val == val:
                return current
            if not current.left:
                current = current.right
            else:
                pre = current.left
                while pre.right and pre.right != current:
                    pre = pre.right
                if not pre.right:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    current = current.right
        return None
