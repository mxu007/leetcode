Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

https://leetcode.com/problems/add-binary/description/

# 1) iteartive approach, O(N) time complexity
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        carry = 0
        i = len(a) -1
        j = len(b) - 1

        while i >= 0 and j >= 0:
            result =  str(carry + int(a[i]) + int(b[j])-2) + result if carry + int(a[i]) + int(b[j]) >= 2 else  str(carry + int(a[i]) + int(b[j])) + result
            carry = 1 if carry + int(a[i]) + int(b[j]) >= 2 else 0
            i,j = i-1, j-1

        while i >= 0:
            result = '0' + result if carry + int(a[i]) > 1 else str(carry + int(a[i])) + result
            carry  = 1 if carry + int(a[i]) > 1 else 0
            i -= 1

        while j >= 0:
            result = '0' + result if carry + int(b[j]) > 1 else str(carry + int(b[j])) + result
            carry  = 1 if carry + int(b[j]) > 1 else 0
            j -= 1

        return '1' + result if carry else result


# 2) cleaner version
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        max_len = max(len(a), len(b))

        a = a.zfill(max_len)
        b = b.zfill(max_len)

        result = ''
        carry = 0

        for i in range(max_len-1, -1, -1):
            r = carry
            r += 1 if a[i] == '1' else 0
            r += 1 if b[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1

        if carry !=0 : result = '1' + result

        return result.zfill(max_len)

# 3) conversion to int, sum and convert it back
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return "{0:b}".format(int(a,2) + int (b,2))

# 4) elegant recursive solution
class Solution:
    def addBinary(self, a, b):
        if len(a)==0: return b
        if len(b)==0: return a
        # b[-1] refers to the last element of list
        # b[0:-1] refers to from first to second last element of list
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + str(int(a[-1]) + int(b[-1]))
