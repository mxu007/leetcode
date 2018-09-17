# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
# Example 1:

# Input: A = "ab", B = "ba"
# Output: true
# Example 2:

# Input: A = "ab", B = "ab"
# Output: false
# Example 3:

# Input: A = "aa", B = "aa"
# Output: true
# Example 4:

# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:

# Input: A = "", B = "aa"
# Output: false
 
# Note:

# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist only of lowercase letters.

# https://leetcode.com/problems/buddy-strings/description/

# 1) O(N) time and O(1) space
class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # if length differs or set of characters differ, return False directly
        if len(A) != len(B) or set(A) != set(B): return False
        # if A and B are equal, returns if we have at least 1 repetitive character in the list
        if A == B:
            return len(A) - len(set(A)) >= 1
        else:     
            indices = []
            counter = 0
            for i in range(len(A)):
                if A[i] != B[i]:
                    counter += 1
                    indices.append(i)
                # if two list have more than 2 indices with different characters, return false
                if counter > 2:
                    return False
            # check if the swap can happen
            return A[indices[0]] == B[indices[1]] and A[indices[1]] == B[indices[0]]
            
# 2) improved and more concise version of 1)
class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B): return False
        if A == B and len(set(A)) < len(A): return True
        dif = [(a, b) for a, b in zip(A, B) if a != b]
        # print(dif, dif[0], dif[1][::-1])
        # e.g. A = "aaaaaaabc"
        # B = "aaaaaaacb"
        # [('b', 'c'), ('c', 'b')] ('b', 'c') ('b', 'c')
        return len(dif) == 2 and dif[0] == dif[1][::-1]
