# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.

# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/

# 1) use two pointers to locate the left and right edge of subarray, O(Nlog(N)) time complexity
# O(N) additional space
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        sorted_nums = sorted(nums)
        if nums == sorted_nums: return 0
        i, j = 0, len(nums)-1

        while i < len(nums)-1:
            if(sorted_nums[i] != nums[i]):
                left = i
                break
            else:
                i += 1
        while j > 0:
            if(sorted_nums[j] != nums[j]):
                right = j
                break
            else:
                j -= 1

        return j - i + 1


# 2) using stack, rising slope and falling slope
# O(N) time complexity, O(N) space (as for the stack)
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution/
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        left, right = len(nums), 0
        for i in range(len(nums)):
            while(len(stack)>0 and nums[stack[-1]] > nums[i]):
                left = min(left, stack.pop())
            stack.append(i)

        stack = []
        for j in range(len(nums)-1,-1,-1):
            while(len(stack)>0 and nums[stack[-1]] < nums[j]):
                right = max(right, stack.pop())
            stack.append(j)

        return right - left + 1 if right > left else 0

# 3) rising slope and falling slope
# O(N) time and O(1) space, save the need for stack to store index, but requires additoinal two for loops to locate the correct indices
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution/
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = sys.maxsize, -sys.maxsize - 1

        flag = False
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                flag = True
            if flag:
                low = min(low, nums[i])

        flag = False
        for j in range(len(nums)-2, -1, -1):
            if nums[j] > nums[j+1]:
                flag = True
            if flag:
                high = max(high, nums[j])

        #  traverse over numsnums and determine the correct position of low and high by comparing these elements with the other array elements
        for i in range(len(nums)):
            if low < nums[i]:
                break

        for j in range(len(nums)-1,-1,-1):
            if high > nums[j]:
                break

        return j-i+1 if j>i else 0

# 4) a more concise and pythonic version of # 1)
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, sorted_nums = len(nums), sorted(nums)
        if nums == sorted_nums: return 0
        l, r = min(i for i in range(n) if nums[i] != sorted_nums[i]), max(i for i in range(n) if nums[i] != sorted_nums[i])
        return r - l + 1
