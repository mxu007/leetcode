# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

# Example 1:
# Input: [3, 2, 1]

# Output: 1

# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]

# Output: 2

# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]

# Output: 1

# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.

# https://leetcode.com/problems/third-maximum-number/description/

# 1) iterate the nums and compare with first, second and third, cannot sort as the problem specifies O(N) time
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second, third = -sys.maxsize - 1, -sys.maxsize - 1, -sys.maxsize - 1
        for num in nums:
            if num > first:
                first, second, third = num, first, second
            elif second < num < first:
                second, third = num, second
            elif third < num < second:
                third = num
        return third if third != -sys.maxsize - 1 else first


# 2) use heapq, heapq.nlargest(n,B) takes O(mlog(n)) where m is number of elements in nums
# https://stackoverflow.com/questions/23038756/how-does-heapq-nlargest-work
# https://stackoverflow.com/questions/29109741/what-is-the-time-complexity-of-getting-first-n-largest-elements-in-min-heap?lq=1
import heapq
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        B = set(nums)
        A = heapq.nlargest(3, B)
        A.sort()
        if len(A) != 3 :
            return A[-1]
        else:
            return A[0]
