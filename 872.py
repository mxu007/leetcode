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

import itertools

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

        # alternative genreative method for flattening the nested list
        def flatten_generative(lst):
            for x in lst:
                if isinstance(x, list):
                    for x in flatten_generative(x):
                        yield x
                else:
                    yield x

        leaves_1 = (flatten_recursive(getLeaves(root1)))
        leaves_2 = list(flatten_generative(getLeaves(root2)))

        print(leaves_1, leaves_2)

        return(leaves_1==leaves_2)


