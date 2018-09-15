# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
# Example 1:

# Input: 1
# Output: "A"
# Example 2:

# Input: 28
# Output: "AB"
# Example 3:

# Input: 701
# Output: "ZY"

# https://leetcode.com/problems/excel-sheet-column-title/description/

# 1) handle three cases, logN time complexity
import string
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        num_to_alpha = {}
        result = ""
        for i, strg in enumerate(string.ascii_uppercase):
            num_to_alpha[i+1] = strg
        num_to_alpha[0] = 'Z'

        j = 1
        while n > 0:
            # if n is multiple of 26 and greater than max val of current index, means we need a additional alphabet to the left
            if n % 26 == 0 and n > 26**j:
                # get remainder
                result = num_to_alpha[n%(26**j)//(26**(j-1))] + result
                # subtract n
                n = n - (n%(26**j)) if n%(26**j) else n - 26**j
            # if n is multiple of 26 and smaller than max val of current index
            elif n%26 == 0 and n <= 26**j:
                result = num_to_alpha[n//(26**(j-1))] + result
                n -= 26 ** j
            # if n is not the multiple of 26
            else:
                result = num_to_alpha[n%26] + result
                n -= (26 ** (j-1)) * (n%26)
            j += 1
        return result

# 2) clever solution to -1 each time
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        r = ''
        while(n>0):
            n -= 1
            r = chr(n%26+65) + r
            n //= 26
        return r

# 3) variant of 2)
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while n > 0:
            result.append(capitals[(n-1)%26])
            n = (n-1) // 26
        result.reverse()
        return ''.join(result)

# 4) recursive solution
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 26:
            return chr(n -1 + 65)
        return self.convertToTitle((n-1)//26) + chr((n-1)% 26 + 65)


# 5) neat solution, simplification of 1)
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ""
        while n != 0:
            c = n % 26
            if c == 0 :
                c = 26
            n -= c
            n //= 26
            s = str(chr(c + 64)) + s
        return s
