# We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# Note: The input number n will not exceed 100,000,000. (1e8)

# https://leetcode.com/problems/perfect-number/description/

# 1) Use iteration to find all divisor, sum divisor, O(sqrt(N)) time complexity
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def get_divisors(num):
            divisors = [1]
            for i in range(2,int(num**0.5+1)):
                if (num%i==0):
                    if num/i==i: divisors.append(i)
                    else: divisors.extend([i,num//i])
            return divisors

        return num == sum(get_divisors(num)) if num > 1 else False


# 2) get divisor and sum at the same time
class Solution:
    def checkPerfectNumber(self, num):
        total, i = 1, 2
        while i * i < num:
            if num % i == 0:
                total += i + num / i
            i += 1
        return num > 1 and total == num


# 3) iterate from 1 to N, O(N) time complexity
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        total = -num
        for i in range(1, num):
            if i * i > num:
                break
            if num % i == 0:
                total += i + num / i
                if num / i == i:
                    total -= i
        return total == num
