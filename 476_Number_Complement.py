# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

# Note:
# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.
# Example 1:
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
# Example 2:
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

# https://leetcode.com/problems/number-complement/description/

# 1) convert to binary string, iterate the string, O(log(N)) time, as log(N) is no.of bits a number has in its binary form
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Convert num into binary form
        num_bin = "{0:b}".format(num)

        # Get the inverse binary string
        num_bin_inv = ''.join('1' if x == '0' else '0' for x in num_bin)

        # Get the integer of the inverse binary
        num_inv = int(num_bin_inv, 2)
        return (num_inv)

# 2) one-liner
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(''.join(str(int(x)^1) for x in "{0:b}".format(num)),2)

# 3) variant of 2) using bin instead of "{0:b}.format()"
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(''.join(str(int(x)^1) for x in bin(num)[2:]),2)

# 4) variant of 3
class Solution():
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(''.join([str(1-int(x)) for x in bin(num)[2:]]),2)

# 5) use bitwise XOR
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num ^ (2**((int.bit_length(num)))-1)

# 6) right shift 1 to match the bit length of input num
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # left shift to reach the bit length of input num
        n = 1
        while n <= num:
            n <<= 1
        return (n - 1) ^ num

# 7) the complement of num + num equals 2**(bit length of num) -1
# class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # left shift to reach the bit length of input num
        return pow(2,len(str(bin(num)))-2)-1-num


# 8) variant of 6)
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # left shift to reach the bit length of input num
        return pow(2,int.bit_length(num))-1-num

# 9) conventional approach using bin()[2:]
class Solution(object):
    def findComplement(self, num):
        result =''
        for x in bin(num)[2:]:
            if x=='0':
                result+='1'
            else:
                result+='0'
        return int(result,2)

# 10) use bin to convert to binary string then replace 0 to x where x is a temporary placeholder, then convert 1 to 0 and then x to 1
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b = bin(num)
        return int(b[:2] + b[2:].replace('0', 'x').replace('1', '0').replace('x', '1'),2)

# 11) one-liner of 10)
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(bin(num)[2:].replace('0','x').replace('1','0').replace('x','1'),2)

# 12) get length of binary string of input num, make string 1 with same length and apply XOR
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = bin(num)[2:]
        y = '1'*(len(x))
        return (int(x,2) ^ int(y,2))

# 13) one-liner of 12
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return (int(bin(num)[2:],2) ^ int('1'*len(bin(num)[2:]),2))

# 14) bit-wise from right to left, then reverse the string and convert to integer
class Solution:
    def findComplement(self, num):
            """
            :type num: int
            :rtype: int
            """
            result = ''
            while num:
                result += '0' if num & 1 else '1'
                num >>= 1
            return int(''.join(list(reversed(result))), 2)

# 15) get length of binary string of input num, make string 1 with same length and apply subtraction
class Solution:
    def findComplement(self, num):
            """
            :type num: int
            :rtype: int
            """
            allOnes = '1' * (len(bin(num)) -2)
            return int(allOnes, 2) - num

# 16) left shift one, similar to repeat 1 by the length of binary string of num
class Solution:
    def findComplement(self, num):
        return num ^ ((1 << len(bin(num)) - 2) - 1)

# 17) from right to left, because ans starts from 0, any bit is currently 1 will be 0, any bit is currently 0 will be 1 by 2
class Solution:
    def findComplement(self, num):
        num_bin = bin(num)[2:]
        ans = 0
        for i, u in enumerate(num_bin[::-1]):
            if u == '0':
                ans += 2 ** i
        return ans


