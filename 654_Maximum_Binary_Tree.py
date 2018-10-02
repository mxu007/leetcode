# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.

# Example 1:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:

#       6
#     /   \
#    3     5
#     \    /
#      2  0
#        \
#         1
# Note:
# The size of the given array will be in the range [1,1000].

# https://leetcode.com/problems/maximum-binary-tree/description/

# 1) recursive approach, check length of input nums first, then find max, construct node, set node.left and node.right
# O(N) time for worst-case imbalanced tree (input array is a sorted array from smallest to largest)
# O(N) space for worst-case imbalanced tree requires N call stacks
class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) > 0:
            max_index = nums.index(max(nums))
            tNode = TreeNode(max(nums))
            tNode.left = self.constructMaximumBinaryTree(nums[:max_index])
            tNode.right = self.constructMaximumBinaryTree(nums[max_index+1:])
            return tNode
        return None

# 2) use stack, O(N^2) time complexity given a sorted array in ascending order
# https://leetcode.com/problems/maximum-binary-tree/discuss/106147/c-9-lines-on-log-n-map-plus-stack-with-binary-search
class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []
        for i in range(len(nums)):
            current = TreeNode(nums[i])
            left = None
            # handle the case where the current val is larger than existing values in the stack, pop those values in the stack
            while stack and stack[-1].val < nums[i]:
                left = stack[-1]
                stack.pop()
            current.left = left
            # build the link between existing stack top with current val
            if stack:
                stack[-1].right = current
            stack.append(current)

        return stack[0]
