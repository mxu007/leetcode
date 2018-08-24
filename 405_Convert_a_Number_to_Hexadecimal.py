# Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

# Note:

# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the number to hex directly.
# Example 1:

# Input:
# 26

# Output:
# "1a"
# Example 2:

# Input:
# -1

# Output:
# "ffffffff"

# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/

# 1) iterative approach
class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'

        result = []
        # flag to indicate non-negative and negative value
        positive = num >= 0
        # dict for hex value greater than decimal 10
        base_16 = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}

        # 2s complement of Hex
        # finding the hex 2s complement representation of a negative value
        # equals finding hex representation of (fffffff+value+1)
        # ffffffff = 4294967295
        if not positive:
            num = 4294967295 + num + 1

        while(num>0):
            remainder = num % 16
            result.append(str(remainder)) if remainder <= 9 else result.append(base_16[remainder])
            num = num // 16

        result = result[::-1]
        return ''.join(map(str,result))

# 2) recursive approach
class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'

        # flag to indicate non-negative and negative value
        positive = (num>=0)

        # 2s complement of Hex
        # finding the hex 2s complement representation of a negative value
        # equals finding hex representation of (fffffff+value+1)
        # ffffffff = 4294967295
        if not positive: num = 4294967295 + num + 1

        # dict for hex value greater or equal than decimal 10
        base_16 = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}

        def find_hex(num):
            if num == 0:
                return ''
            else:
                remainder = num % 16
                # append to the front and handle case for remainder greater or equal than decimal 10
                return find_hex(num//16) + str(remainder) if remainder <= 9 else find_hex(num//16) + base_16[remainder]

        return find_hex(num)

# 3) bit shift, logic and manipulation
class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = ''
        letter = ('0', '1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')
        if num == 0: return '0'
        if num < 0: num += 2**32
        while num != 0:
            ret = letter[num&15] + ret
            # shift four 4 bits per iteration, which correspond to the hex
            num >>= 4
        return ret
