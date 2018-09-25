# Let's call an array A a mountain if the following properties hold:

# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:
Input: [0,1,0]
Output: 1
Example 2:

Example 2:
Input: [0,2,1,0]
Output: 1
Note:

# 3 <= A.length <= 10000
# 0 <= A[i] <= 10^6
# A is a mountain, as defined above.

# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

# 1) use list.index and max, O(N) time
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))


# 2) enumerate, time limit exceed
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return [i for i,a in enumerate(A) if a == max(A)][0]

# 3) Iterative method, O(N) time
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)):
            if A[i] > A[i+1]:
                return i

# 4) binary search, O(log(N)) time
# squeeze left and right pointer where A[i] < a[i+1] first become False
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 0, len(A)-1
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] < A[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        return left

# 5) standard golden search, might be faster than binary search
# index seach range defined by [left, x1, x2, right] (from smallest to largest)
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        phi_inv = 1 / ((math.sqrt(5) + 1) / 2)

        def cal_x1(left,right):
            return math.ceil(right - (right-left) * phi_inv)
        def cal_x2(left,right):
            return int(left + (right-left) * phi_inv)

        left, right = 0, len(A)-1
        x1, x2 = cal_x1(left, right), cal_x2(left,right)
        while x1 < x2:
            if A[x1] < A[x2]:
                left = x1
                x1 = x2
                x2 = cal_x2(left,right)
            else:
                right = x2
                x2 = x1
                x1 = cal_x1(left,right)

        if A[x1] < A[x1+1]: return x1+1
        elif A[x1-1] > A[x1]: return x1-1
        else: return x1

# 6) golden more advanced golden search
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        phi_inv = 1 / ((math.sqrt(5) + 1) / 2)

        def cal_x1(left,right):
            return right - (round((right-left) * phi_inv))
        def cal_x2(left,right):
            return left + (round((right-left) * phi_inv))

        left, right = 0, len(A)-1
        x1, x2 = cal_x1(left, right), cal_x2(left,right)
        while x1 < x2:
            if A[x1] < A[x2]:
                left = x1
                x1 = x2
                x2 = cal_x1(x1,right)
            else:
                right = x2
                x2 = x1
                x1 = cal_x2(left,x2)
        return x1

