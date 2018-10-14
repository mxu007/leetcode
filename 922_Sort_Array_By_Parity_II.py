# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

# You may return any answer array that satisfies this condition.



# Example 1:

# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


# Note:

# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000

# https://leetcode.com/problems/sort-array-by-parity-ii/description/

# 1) construct odd and even list and append to result alternatively
# O(N) time complexity, O(N) space
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd, even = [a for a in A if a % 2 == 1], [a for a in A if a % 2 == 0]
        j, k, result = 0, 0, []
        for i in range(len(A)):
            if i % 2 == 0:
                result.append(even[j])
                j += 1
            else:
                result.append(odd[k])
                k += 1
        return result

# 2) more concise variant of 1)
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd, even = [a for a in A if a % 2 == 1], [a for a in A if a % 2 == 0]
        result = [None] * len(A)
        result[::2], result[1::2] = even, odd
        return result

# 3) one-liner based on 2)
import itertools
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return list(itertools.chain(*zip([a for a in A if a % 2 == 0],[a for a in A if a % 2 == 1])))
# 4) variant of 2)
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd, even = [a for a in A if a % 2 == 1], [a for a in A if a % 2 == 0]
        return [i for j in zip(even,odd) for i in j]


# 5) one-liner based on 4)
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return [i for j in zip([a for a in A if a % 2 == 0],[a for a in A if a % 2 == 1]) for i in j]

# 6) use odd and even pointers and perform in-line swap, take note the two pointers not pointing to current odd/even numbers, but pointing to the supposed-to-be odd/even numbers, the index pointer i moves from left to right and the correct update performs right to left
# O(N) time, O(1) space
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_pointer = len(A) - 1
        even_pointer = len(A) - 2
        i = 0

        while i < max(odd_pointer, even_pointer):
            while (i + A[i]) % 2:  # one is odd, other is even, so it is misplaced
                if A[i] % 2 == 1:
                    A[i], A[odd_pointer] = A[odd_pointer], A[i]
                    odd_pointer -= 2
                else:
                    A[i], A[even_pointer] = A[even_pointer], A[i]
                    even_pointer -= 2

            i += 1
        return A
