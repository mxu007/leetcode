Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.



Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000

# 1) use python list iterator, O(N) time and O(N) space
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return [even for even in A if even % 2 == 0] + [odd for odd in A if odd % 2 ==1]

# 2) two pointers, i tracks odd, j tracks even, perform swap, O(N) time and O(1) space
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i,j = 0,0
        # use i record the odd number and use j find the first even number after i,then swap inplace
        while i < len(A):
            if j < i: j = i
            while j < len(A) and A[i] % 2 != 0 and A[j] % 2 != 0: j += 1
            if j >= len(A): break
            A[i], A[j] = A[j], A[i]
            i += 1
        return A

# 3) variant of 2), j tracks even, i tracks the index of swap, O(N) time and O(1) space
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = -1
        for j in range(len(A)):
            if A[j] % 2 == 0:
                i += 1
                A[i], A[j] = A[j], A[i]
        return A
