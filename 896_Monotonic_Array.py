# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.



# Example 1:

# Input: [1,2,2,3]
# Output: true
# Example 2:

# Input: [6,5,4,4]
# Output: true
# Example 3:

# Input: [1,3,2]
# Output: false
# Example 4:

# Input: [1,2,4,5]
# Output: true
# Example 5:

# Input: [1,1,1]
# Output: true


# Note:

# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000

# https://leetcode.com/problems/monotonic-array/description/

# 1) use a variable to store flag
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2: return True
        Flag = None
        for i in range(1,len(A)):
            if A[i] != A[i-1] and Flag == None:
                Flag = (A[i] > A[i-1])
            if Flag:
                temp = (A[i] >= A[i-1])
                if temp != Flag: return False
            elif Flag != None:
                temp = (A[i] > A[i-1])
                if temp != Flag: return False
        return True

# 2) use sort
class Solution:
    def isMonotonic(self, A):
        """
        :type A:
        :rtype: bool
        """
        return sorted(A) == A or sorted(A) == A[::-1]

# 3) pairwise comparison using zip, and tuple comparison
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        result = {(i>j)-(i<j) for i,j in zip(A,A[1:])}
        #print(result >= {1,-1})
        return not (result >= {1,-1})

