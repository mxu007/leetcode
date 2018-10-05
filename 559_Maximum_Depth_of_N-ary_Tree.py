# Given a n-ary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# For example, given a 3-ary tree:


# We should return its max depth, which is 3.

# Note:

# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.

# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# 1) recursive call, O(N) time to visit every node, where N is no.of nodes
# O(log(N)) space for the call stack for a balanced tree
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # Three cases: empty root, only root with no children, and root has children

        if not root:
            return 0
        elif not root.children:
            return 1
        else:
            return max([self.maxDepth(node) for node in root.children]) + 1

# 2) one-liner of 1
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return max([self.maxDepth(node) for node in root.children+[None]]) + 1 if root else 0

# 3) use map to achieve the recursive call
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # Three cases: empty root, only root with no children, and root has children

        if not root:
            return 0
        elif not root.children:
            return 1
        else:
            return max(map(self.maxDepth, root.children)) + 1

# 4) iterative approach using DFS, O(N) time to visit all the nodes
# O(N) space for the stack
# depth is the variable stores the largest depth
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # Three cases: empty root, only root with no children, and root has children

        stack = []
        if root:
            stack.append((1,root))

        depth = 0
        while len(stack) > 0:
            current_depth, node = stack.pop()
            if node:
                depth = max(depth, current_depth)
                for child in node.children:
                    stack.append((current_depth+1, child))
        return depth

# 5) breadth-first-search BFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        depth, stack = 0, [root]

        # outer while stops when the algo reaches the bottom of tree
        while stack:
            next_level = []
            # inner while stops when all nodes at current layber being popped
            while stack:
                node = stack.pop()
                if node.children:
                    next_level.extend(node.children)
            stack = next_level
            depth += 1

        return depth

# 6) simplication of 4)
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        if not root: return 0
        depth, stack = 0, [root]

        while stack:
            depth += 1
            stack = [child for node in stack for child in node.children if child]
        return depth

# 7) variant of 1)
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # Three cases: empty root, only root with no children, and root has children

        if not root: return 0
        depth = 0
        for child in root.children:
            depth = max(depth, self.maxDepth(child))
        return depth + 1

# 8) shorter version of 7
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # Three cases: empty root, only root with no children, and root has children
        if not root: return 0
        depth = max([0] + [self.maxDepth(node) for node in root.children])
        return depth + 1

# 9 one-liner of 8
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # Three cases: empty root, only root with no children, and root has children
        return max([0] + [self.maxDepth(node) for node in root.children]) + 1 if root else 0
