# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

# Also, a self-dividing number is not allowed to contain the digit zero.

# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

# Example 1:
# Input:
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
# Note:

# The boundaries of each input argument are 1 <= left <= right <= 10000.

# https://leetcode.com/problems/self-dividing-numbers/description/

#1) Brute-Force, D*log(R) time
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # Time complexity D*log(R) where D is number of integers between left and right
        # and R is the largest number, the number of digits (length of the longest string) that R has
        # is log10(R) + 1
        # https://math.stackexchange.com/questions/231742/proof-how-many-digits-does-a-number-have-lfloor-log-10-n-rfloor-1

        num_list = []
        # Outter for to loop through the range of numbers
        for i in range(left, right+1):
            flag = False
            # Inner for to loop through each digit of a specific numbers
            for j in str(i):
                if j == "0" or i%int(j)!=0:
                    break
                elif i%int(j)==0:
                    flag = True
            if flag:
                list.append(i)
        return num_list

# 2) One-liner of 1)
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [num for num in range(left,right+1) if all(i!='0' and num % int(i) == 0 for i in str(num) )]

# 3) variant one-liner
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [num for num in range(left,right+1) if '0' not in str(num) and all(num % int(i) == 0 for i in str(num) )]

# 4) improved one-liner
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [num for num in range(left, right+1) if all((i and (num % i==0) for i in map(int, str(num))))]

# 5) using lambda function
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        is_self_dividing = lambda num: '0' not in str(num) and all(num % int(digit) == 0 for digit in str(num))
        return list(filter(is_self_dividing, range(left, right + 1)))

# 6) use divmod
# For integers, the result is the same as (a // b, a % b)
# https://docs.python.org/3/library/functions.html#divmod
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isSelfDividing(ori,num):
            if num < 10:
                if num and ori % num == 0:
                    return True
                else:
                    return False
            q, r = divmod(num, 10)
            if r == 0 or ori % r != 0:
                return False
            else:
                return isSelfDividing(ori,q)

        num_list = []
        for n in range(left,right+1):
            if isSelfDividing(n,n):num_list.append(n)
        return num_list
