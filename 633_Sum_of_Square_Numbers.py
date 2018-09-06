# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

# Example 1:
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:
# Input: 3
# Output: False

# https://leetcode.com/problems/sum-of-square-numbers/description/

# 1) get all prime divisors and check if every prime divisors p ≡ 3 mod 4 occurs with even exponent
# Fermat Theorem
# Any positive number nn is expressible as a sum of two squares if and only if the prime factorization of nn, every prime of the form (4k+3)(4k+3) occurs an even number of times.
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/

        def get_prime_divisors(n):
            result = []
            while n % 2 == 0:
                result.append(2)
                n = n//2
            for i in range(3,int(n**0.5+1),2):
                while n % i == 0:
                    result.append(i)
                    n = n / i
            if n > 2:
                result.append(n)
            return result

        if c == 0: return True

        divisors_count = collections.Counter(get_prime_divisors(c))

        # https://math.stackexchange.com/questions/787321/how-to-determine-whether-a-number-can-be-written-as-a-sum-of-two-squares
        for divisor in divisors_count:
            if divisor % 4 == 3 and divisors_count[divisor] % 2 ==1:
                return False
        return True

# 2) sqrt function, sqrt equals int, O(√c log(c)) time complexity
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(0,int(c**0.5)+1):
            j = (c - i*i) ** 0.5
            if j == int(j):
                return True

        return False


# 3) binary search on square, exceed time complexity
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def binary_search(left,right,n):
            if (left > right):
                return False
            mid = left + (right-left) //2
            if mid ** 2 == n:
                return True
            elif mid ** 2 > n:
                return binary_search(left,mid-1,n)
            return binary_search(mid+1,right,n)

        for i in range(int(c**0.5)+1):
            j = c -i * i
            if binary_search(0,j,j):
                return True
        return False


# 4) check if it is square
class Solution:
    def judgeSquareSum(self, c):
        def is_square(N):
            return int(N**.5)**2 == N

        return any(is_square(c - a*a)
                    for a in range(int(c**.5) + 1))

# 5) one-liner
class Solution:
    def judgeSquareSum(self, c):
        return any(True for a in range(int(math.sqrt(c)) + 1) if math.sqrt(float(c - a * a)).is_integer())
