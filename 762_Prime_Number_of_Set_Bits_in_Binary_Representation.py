# Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

# (Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

# Example 1:

# Input: L = 6, R = 10
# Output: 4
# Explanation:
# 6 -> 110 (2 set bits, 2 is prime)
# 7 -> 111 (3 set bits, 3 is prime)
# 9 -> 1001 (2 set bits , 2 is prime)
# 10->1010 (2 set bits , 2 is prime)
# Example 2:

# Input: L = 10, R = 15
# Output: 5
# Explanation:
# 10 -> 1010 (2 set bits, 2 is prime)
# 11 -> 1011 (3 set bits, 3 is prime)
# 12 -> 1100 (2 set bits, 2 is prime)
# 13 -> 1101 (3 set bits, 3 is prime)
# 14 -> 1110 (3 set bits, 3 is prime)
# 15 -> 1111 (4 set bits, 4 is not prime)
# Note:

# L, R will be integers L <= R in the range [1, 10^6].
# R - L will be at most 10000.

# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/

class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """

        # function to count set bits of an integer
        # Brian Kernighan’s Algorithm
        # https://www.geeksforgeeks.org/count-set-bits-in-an-integer/
        def countSetBits(n):
         # base case
            if (n == 0):
                return 0
            else:
                return 1 + countSetBits(n & (n - 1))

        # get of list of set bits count
        set_bits_count = []

        for val in range(L, R+1):
            set_bits_count.append(countSetBits(val))

        # maximum value of R is 10^6, its binary reprensentation is 11110100001001000000 (20 digits)
        # prime numbers <= 20 are: 2,3,5,7,11,13,17,19
        prime_numbers = [2,3,5,7,11,13,17,19]

        return(len([i for i in set_bits_count if i in prime_numbers]))
