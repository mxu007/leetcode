# We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

# Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

# (Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

# Example 1:
# Input: [1,null,0,0,1]
# Output: [1,null,0,null,1]

# Explanation:
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.


# Example 2:
# Input: [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]



# Example 3:
# Input: [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]

# Note:

# The binary tree will have at most 100 nodes.
# The value of each node will only be 0 or 1.

# https://leetcode.com/problems/binary-tree-pruning/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1) two recursive functions, has_one check whether a subtree has at least one 1
# recur_prune recursively prune subtree based on check done by has_one function
class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def has_one(root):
            if root:
                if root.val == 1: return True
                return has_one(root.left) or has_one(root.right)
            return False

        def recur_prune(root):
            if root:
                if not has_one(root):
                    return None
                if not has_one(root.left):
                    root.left = None
                if not has_one(root.right):
                    root.right = None
                root.left = recur_prune(root.left)
                root.right = recur_prune(root.right)
            return root

        return recur_prune(root)

# 2) more concise solution
# O(N) time to visit each node, log(N) space given a balanced tree for the call stack
# the else condition take care cases where root.val == 0
# if root.val == 0 and root has children, return root
# if root.val == 0 and it has no children (meaning a leaf node), return None
# root.left = self.pruneTree(root.left) and root.right = self.pruneTree(root.right) preceed the following
# commands to remove the leaf 0 node
class Solution():
    def pruneTree(self, root):
        if not root: return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val:
            return root
        else:
            return root if root.left or root.right else None

# 3) variant of 2)
class Solution():
    def pruneTree(self, root):
        if not root: return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        # remove the leaf 0 node
        if not root.left and not root.right and not root.val: return None
        return root

# 4) concise 2-liner of 3)
class Solution():
    def pruneTree(self, root):
        if root: root.left, root.right = self.pruneTree(root.left), self.pruneTree(root.right)
        if root and (root.left or root.right or root.val): return root

# 5) stack approach, O(N) time
# push to stack with visit info
# visited in terms of processing as the node
# once visited, will not add its children to the stack any more
# but still process the node whenever it is popped up
class Solution():
    def pruneTree(self, root):
        stack = [(0,root)]
        while(stack):
            visited, node = stack.pop()
            if node is None:
                continue
            if not visited:
                stack.extend([(1,node), (0,node.left), (0,node.right)])
            else:
                if node.left and not (node.left.val or node.left.left or node.left.right):
                    node.left = None
                if node.right and not(node.right.val or node.right.left or node.right.right):
                    node.right = None
        return root

