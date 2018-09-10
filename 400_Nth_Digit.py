
# 1) cal_total_digits calculate number of digits given a integer num
# log(n)^2 time complexity
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10: return n

        # log(n) time complexity to calculate total digit counts
        def cal_total_digits (num):
            total_digits = 0
            i = 1
            while (i<=num):
                total_digits += (num - i + 1)
                i *= 10
            return total_digits
        j = 1
        # log(n) time for the while loop
        while(cal_total_digits(10**j-1) <= n):
            curr_count = cal_total_digits(10**j-1)
            j += 1

        remain = n - curr_count
        target = remain // j + 10**(j-1) - 1
        mod = remain % j
        return int(str(target+1)[mod-1]) if mod else int(str(target)[-1])

# 2) O(n) time complexity, exceed time limit
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, size = 1, 1
        while n > size:
            n, start = n - size, start + 1
            size = len(str(start))
        return int(str(start)[n-1])

# 3) more concise approach of 1), O(log(n) time complexity
# udpate remaining digit count n with every steps
class Solution(object):
    def findNthDigit(self, n):
        start, size, step = 1, 1, 9
        while n > size * step:
            n, size, step, start = n - (size * step), size + 1, step * 10, start * 10
        return int(str(start + (n - 1) // size)[(n - 1) % size])
