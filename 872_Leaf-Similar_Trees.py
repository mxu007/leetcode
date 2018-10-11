# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
# #         self.right = None

# Note:

# Both of the given trees will have between 1 and 100 nodes.

# https://leetcode.com/problems/leaf-similar-trees/description/

# 1) recursively construct the list of leaf nodes then flatten the nested list to do the comparison
# O(N) time to visit every node, O(log(N)) space for call stack in balanced binary tree
class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        # recursive call to get the leaves, the returned can be nested list
        def getLeaves(root):
            leaves = []
            if root != None:
                if root.left == None and root.right==None:
                    leaves.append(root.val)
                    return leaves

                # recursive call for the left child
                leaves.append(getLeaves(root.left))
                # recursive call for the right child
                leaves.append(getLeaves(root.right))

            return leaves

        # recursive call for the nested list
        def flatten_recursive(lst):
            return sum( ([x] if not isinstance(x, list) else flatten_recursive(x)
                 for x in lst), [] )

        leaves_1 = flatten_recursive(getLeaves(root1))
        leaves_2 = flatten_recursive(getLeaves(root2))
        return(leaves_1==leaves_2)

# 2) recursively construct the list of leaf nodes then iteratively flatten the nested list to do the comparison
class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        # recursive call to get the leaves, the returned can be nested list
        def getLeaves(root):
            leaves = []
            if root != None:
                if root.left == None and root.right==None:
                    leaves.append(root.val)
                    return leaves
                leaves.append(getLeaves(root.left))
                leaves.append(getLeaves(root.right))

            return leaves

        # alternative genreative method for flattening the nested list
        def flatten_generative(lst):
            for x in lst:
                if isinstance(x, list):
                    for x in flatten_generative(x):
                        yield x
                else:
                    yield x

        leaves_1 = list(flatten_generative(getLeaves(root1)))
        leaves_2 = list(flatten_generative(getLeaves(root2)))

        return(leaves_1==leaves_2)

# 3) pass-by-reference to construct the leave node lists
class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaves_1, leaves_2 = [], []

        def getLeaves(leaves,root):
            if root:
                if root.left is None and root.right is None: leaves.append(root.val)
                getLeaves(leaves,root.left)
                getLeaves(leaves,root.right)

        getLeaves(leaves_1,root1)
        getLeaves(leaves_2,root2)

        return leaves_1 == leaves_2

# 4) dfs and use yield
# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
# O(N) time and O(log(N)) space for the call stack
# itertools.zip_longest zip two iterator
import itertools
class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if not node: return
            if not node.left and not node.right: yield node.val
            for i in dfs(node.left): yield i
            for i in dfs(node.right): yield i
        return all(a == b for a, b in itertools.zip_longest(dfs(root1), dfs(root2)))

# 5) standard dfs and return
class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if not node: return
            if not node.left and not node.right:
                return [node.val]
            left,right = dfs(node.left), dfs(node.right)
            return left + right
        return dfs(root1) == dfs(root2)


# 6) use stack to itearte the tree, s is the external empty stack passed to function iterative
class Solution:
    def leafSimilar(self, root1, root2):

        def iterative(root,s):
            if root is not None:
                stack = []
                stack.append(root)
                while stack:
                    x = stack.pop()
                    if x.left is None and x.right is None:
                        s.append(x.val)
                        continue
                    if x.left is not None:
                        stack.append(x.left)
                    if x.right is not None:
                        stack.append(x.right)
            return s

        return iterative(root1,[]) == iterative(root2,[])

# 7) variant of 6)
class Solution:
    def leafSimilar(self, root1, root2):
        return self.iterative(root1,[]) == self.iterative(root2,[])

    def iterative(self, root,s):
        if root is not None:
            stack = []
            stack.append(root)
            while stack:
                x = stack.pop()
                if x.left is None and x.right is None:
                    s.append(x.val)
                    continue
                if x.left is not None:
                    stack.append(x.left)
                if x.right is not None:
                    stack.append(x.right)
        return s

# 8) variant of 5), clean and concise solution
class Solution():
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.findleaf(root1) == self.findleaf(root2)

    def findleaf(self, root):
        if not root: return []
        if not (root.left or root.right): return [root.val]
        return self.findleaf(root.left) + self.findleaf(root.right)

