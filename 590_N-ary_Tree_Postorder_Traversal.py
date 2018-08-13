# Given an n-ary tree, return the postorder traversal of its nodes' values.


# For example, given a 3-ary tree:


# Return its postorder traversal as: [5,6,3,2,4,1].


# Note: Recursive solution is trivial, could you do it iteratively?

# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        # init empty list to store results
        result = []

# 1) Recursive approach
        if root == None:
            return result

        # postorder traversal: child then root
        def recursive_call(root, result):
            for child in root.children:
                recursive_call(child, result)
            result.append(root.val)

        recursive_call(root, result)

# 2) Iterative approach

# push root to stack, then pop from stack to append to the result list
# then extend the children of root to the step, then repeat the previous step
# https://www.geeksforgeeks.org/iterative-postorder-traversal/
        if root == None:
            return result

        stack1 = []
        stack1.append(root)

        while(len(stack1)>0):
            node = stack1.pop()
            result.append(node.val)
            stack1.extend(node.children)

        return result[::-1]
