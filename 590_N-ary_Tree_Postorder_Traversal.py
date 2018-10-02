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

# 1) Recursive approach
# postorder traversal: left-right-root
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        # init empty list to store results
        result = []

        if not root:
            return result

        # postorder traversal: child then root
        def recursive_call(root, result):
            for child in root.children:
                recursive_call(child, result)
            result.append(root.val)
            return result
        return recursive_call(root, result)


# 2) recursive approach without building additional recursive funciton
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        else:
            return [nodes for child in root.children for nodes in self.postorder(child)] + [root.val]

# 3) one-line of 2)
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        return [] if not root else [nodes for child in root.children for nodes in self.postorder(child)] + [root.val]


# 4) Iterative approach use double stacks
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
        if not root:
            return []
        else:
            stack1 = []
            stack2 = []
            stack1.append(root)
            while stack1:
                node = stack1.pop()
                stack2.append(node.val)
                stack1.extend(node.children)

            return stack2[::-1]


# 5) Iterative approach use single stack, improved version of 4)
# push root to stack, then pop from stack to append to the result list
# then extend the children of root to the step, then repeat the previous step
# https://www.geeksforgeeks.org/iterative-postorder-traversal/
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return result

        stack1 = []
        stack1.append(root)

        while(len(stack1)>0):
            node = stack1.pop()
            result.append(node.val)
            stack1.extend(node.children)

        return result[::-1]
