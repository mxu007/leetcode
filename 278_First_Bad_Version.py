# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Example:

# Given n = 5, and version = 4 is the first bad version.

# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true

# Then 4 is the first bad version.

# https://leetcode.com/problems/first-bad-version/description/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# 1) binary search using while loop, O(log(n)) time complexity
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right-left) // 2
            if not isBadVersion(mid-1) and isBadVersion(mid):
                return mid
            elif isBadVersion(mid-1) and isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return -1

# 2) binary search using recursive call
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n

        def binary_search (left, right):
            if left <= right:
                mid = left + (right-left) // 2
                if not isBadVersion(mid-1) and isBadVersion(mid):
                    return mid
                elif isBadVersion(mid-1) and isBadVersion(mid):
                    return binary_search(left, mid - 1)
                else:
                    return binary_search(mid+1, right)
            else:
                return -1

        return binary_search(left,right)

# 3) improved version of binary search to reduce # of calls on isBadVersion
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = left + (right-left) // 2
            print("before", left, right, mid, isBadVersion(mid))
            # if mid is bad, set right poiner to mid
            if isBadVersion(mid):
                right = mid
            # if mid is not bad, set left to be mid+1 (as mid is already tested not bad)
            else:
                left = mid + 1
            print("after", left, right, mid, isBadVersion(mid))
        return left

# 4) use Python bisect
import bisect
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        class Wrap:
            def __getitem__(self, i):
                return isBadVersion(i)
        # 0, n are specifying low and high for the list genreated by Wrap
        # https://docs.python.org/3/library/bisect.html
        return bisect.bisect(Wrap(), False, 0, n)


