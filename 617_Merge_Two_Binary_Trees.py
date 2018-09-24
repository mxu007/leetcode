# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

# Example 1:
# Input:
#     Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# Output:
# Merged tree:
#          3
#         / \
#        4   5
#       / \   \
#      5   4   7
# Note: The merging process must start from the root nodes of both trees.

# 1) recursive call,first check if both node are None
# O(N) time complexity where m is no.of nodes need to be visited. O(log(N)) space for the call stack, (base 2 log) as it is binary tree
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # Base case where both node is None, then return None
        if t1 is None and t2 is None:
            return None

        # If one of node is None, then assign value 0 and sum with the other node value
        result = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))

        # Recursive call to calculate the left and right child of the result node
        result.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        result.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)

        # return result
        return result

# 2) in-place merge on one tree
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None: return t2
        if t2 is None: return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right,t2.right)


        return t1


# 3) use stack by push and pop (t1.node, t2.node)
# O(N) time to traverse all nodes, where N is the smaller number of nodes in two trees
# O(N) space for a skewed tree
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # if t1 is an empty tree
        if t1 is None:
            return t2
        # init stack
        stack = []
        stack.append((t1,t2))
        while stack:
            t = stack.pop()
            # check if second node is None, if that's the case, directly pop the next element
            if t[0] is None or t[1] is None:
                continue
            t[0].val += t[1].val

            # push left child of two input nodes to stack
            # if left child of first node is None, directly assign value of left child of second node
            if t[0].left is None:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left,t[1].left))

            # push right child of two input nodes to stack
            # if right child of first node is None, directly assign value of right child of second node
            if t[0].right is None:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right,t[1].right))
        return t1
