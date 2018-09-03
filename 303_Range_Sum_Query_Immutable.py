# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.

# https://leetcode.com/problems/range-sum-query-immutable/description/

# 1) use global list
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.items = list(nums)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.items[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


# 2) use cumulative sum
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.accu = [0]
        for num in nums:
            # self.accu += self.accu[-1] + num, equivalent as self.accu += [self.accu[-1] + num], equivalent as elf.accu.append(self.accu[-1]+num)
            self.accu += self.accu[-1] + num,
        print(self.accu)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu[j+1] - self.accu[i]

# 3) mutate the original list, dp bottom-up approach
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = nums
        for i in range(1,len(nums)):
            self.dp[i] += self.dp[i-1]
            # [-2, -2, 1, -4, -2, -3]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j] - (self.dp[i-1] if i > 0 else 0)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


# 4) use global dictionary, but memory limit exceed
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum_dict = {}
        for i in range(len(nums)):
            sum_i = 0
            for j in range(i,len(nums)):
                sum_i += nums[j]
                self.sum_dict[(i,j)] = sum_i

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum_dict[(i,j)]
