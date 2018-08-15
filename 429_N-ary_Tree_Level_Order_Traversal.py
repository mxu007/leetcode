# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example, given a 3-ary tree:


# We should return its level order traversal:



# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]


# Note:

# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.

# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        result = []

        if (not root):
            return result

        # using list to implement queue
        queue = [root]

        # iterat until queue is empty
        while queue:
            # level to store nodes in the current level
            level = []
            # temp_queue to store children of current level nodes
            temp_queue = []

            # iterate all the nodes in currrent level
            for node in queue:
                level.append(node.val)
                # append all children of current level nodes to temp_queue
                if node.children:
                    for child in node.children:
                        temp_queue.append(child)

            # append current level node values as a sublist in the result list
            result.append(level)
            # replace queue with the next level nodes
            queue = temp_queue

        return result





