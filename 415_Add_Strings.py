# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# https://leetcode.com/problems/add-strings/description/

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # if any of the input string is empty
        if len(num1)== 0:
            return num2
        elif len(num2) == 0:
            return num1

        # init i,j,k,carry and result
        i,j = len(num1)-1, len(num2)-1
        carry = 0
        k = 0
        result = 0

        # iterate until any of the string exhausted
        while i>=0 and j>=0:
            temp = (ord(num1[i])-48 + ord(num2[j])-48)
            carry = 1 if temp >= 10 else 0
            temp = temp % 10
            result += temp * (10 ** k) + carry * (10 ** (k+1))
            i,j,k = i-1,j-1,k+1

        # sum the remaining avaiable string
        while i>=0:
            result += (ord(num1[i])-48) * (10 ** k)
            i,k = i-1, k+1

        while j>=0:
            result += (ord(num2[j])-48) * (10 ** k)
            j,k = j-1, k+1


        return str(result)

