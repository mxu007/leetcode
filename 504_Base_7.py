# Given an integer, return its base 7 string representation.

# Example 1:
# Input: 100
# Output: "202"
# Example 2:
# Input: -7
# Output: "-10"
# Note: The input will be in range of [-1e7, 1e7].

# https://leetcode.com/problems/base-7/description/


# 1) Iteartive appraoch
class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "0"

        # init result list
        result = []
        # flag for positive and zero
        positive = (num >= 0)
        print(positive)

        # reverse number if negative input, add negative sign only at return
        if not positive:
            num = -num
        # iterative appraoch to get remainder
        while(num>0):
            result.append(num % 7)
            num = num // 7
        # reverse the result list
        result = result[::-1]
        # return
        return ''.join(map(str,result)) if positive else '-' + ''.join(map(str,result))


# 2) Recursive approach
class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        positive = (num >= 0)
        if not positive: num = -num

        def find_seven(num):
            if num == 0:
                return 0
            else:
                return num % 7 + 10 * find_seven(num//7)

        return str(find_seven(num)) if positive else str(-find_seven(num))

