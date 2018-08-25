# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# https://leetcode.com/problems/maximum-subarray/description/

# 1) itearative approach
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_max, global_max = nums[0], nums[0]
        #local_start, local_end, global_start, global_end = 0, 0, 0, 0

        for i in range(1,len(nums)):
            if local_max <= 0:
                local_max = nums[i]
                #local_start, local_end = i, i
            # if local max is not zero or below, keep adding element
            else:
                local_max += nums[i]
                #local_end = i
            # the update capture the global max
            if local_max > global_max:
                global_max = local_max
                #global_start, global_end = local_start, local_end

        return global_max


# 2) simplified iteartive appraoch
class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum


# 3) divide and conquer approach
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find (nums, start, end):

            # if recursive input only has one item, directly return
            if start == end:
                return nums[start], start, end
            else:
                # calculate the middle index
                middle = (start+end) // 2
                #print(start,end,middle)

                # find the max sum of left half
                sum_1,start_1,end_1 = find(nums,start,middle)
                #print(sum_1,start_1,end_1)

                # find the max sum of the right half
                sum_2,start_2,end_2 = find(nums,middle+1,end)
                #print(sum_2,start_2,end_2)

                # find max sum of left half joined with right right half
                # starting from middle and move to the left
                left_half_sum = nums[middle]
                left_limit = middle
                s = nums[middle]

                for i in range(middle-1, start-1,-1):
                    s += nums[i]
                    if s > left_half_sum:
                        left_half_sum = s
                        left_limit = i

                # starting from middle and move to the right
                right_half_sum = nums[middle+1]
                right_limit = middle+1
                s = nums[middle+1]

                for i in range(middle+2, end+1):
                    s += nums[i]
                    if s > right_half_sum:
                        right_half_sum = s
                        right_limit = i

                sum_3 = left_half_sum + right_half_sum
                max_sum = max(sum_1, sum_2, sum_3)

                #print(sum_1, start_1, end_1, sum_2, start_2, end_2, sum_3, left_limit, right_limit)

                # return the max of left half, right half and joined left and right
                if max_sum == sum_1:
                    return sum_1, start_1, end_1
                elif max_sum == sum_2:
                    return sum_2, start_2, end_2
                return sum_3, left_limit, right_limit

        # handle case where input is None or has single element
        if len(nums)==0:
                return None
        elif len(nums)==1:
                return sum(nums)

        max_sum, max_start, max_end = find(nums,0,len(nums)-1)

        return max_sum


# 4) dynamic programming
# https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts
# similar implementation of iterative approach but with dynamic programming thinking
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [None] * length
        dp[0] = nums[0]
        max_sum = dp[0]

        # keep track of each solution of the sub problem to update the global optimal value
        # maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1) : 0 + A[i];
        for i in range(1,length):
            # dp[i] represent the max sum where element i in the subarray
            dp[i] = nums[i] + dp[i-1] if dp[i-1] > 0 else nums[i]
            # keep track of global max
            max_sum = max(max_sum, dp[i])
            #print(dp[i],max_sum)

        return max_sum



