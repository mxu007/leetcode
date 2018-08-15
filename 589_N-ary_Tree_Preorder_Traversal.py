# Given an n-ary tree, return the preorder traversal of its nodes' values.


# For example, given a 3-ary tree:


# Return its preorder traversal as: [1,3,5,6,2,4].


# Note: Recursive solution is trivial, could you do it iteratively?


# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        # iterative approach
        # push root to stack, then pop from stack to append to the result list
        # then extend the children of root to the step, make sure right-most children are appended to list/stack first, so when the stack pop, it pops the left child first
        # https://www.geeksforgeeks.org/iterative-preorder-traversal/
        result = []
        if root is None:
            return result
        stack1 = []
        stack1.append(root)

        while(len(stack1)>0):
            node = stack1.pop()
            result.append(node.val)

            stack1.extend(node.children[::-1])

        return result
