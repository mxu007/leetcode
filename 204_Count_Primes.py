# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# https://www.geeksforgeeks.org/sieve-of-eratosthenes/

# 1) Sieve of Eratosthenes method, O(sqrt(n)loglog(n)) time
# sqrt(n) comes rom the while loop condition p*p <= n, loglog(n) comes from the if condition and for loop in while
# as p increment from 1 and if primes[p] filters out non-prime numbers, so the for loop executes n/2 + n/3 + n/5 + n/7 +..
# which is sum of reciprocals of all prime numbers
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [True for i in range(n+1)]
        p = 2
        counter = 0
        while (p*p <= n):
            # https://en.wikipedia.org/wiki/Divergence_of_the_sum_of_the_reciprocals_of_the_primes
            if primes[p] == True:
                for i in range(p*2, n+1, p):
                    primes[i] = False
            p += 1

        return sum(primes[2:-1])


# 2) variant that claims O(n) time ,exceeds time complexity
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = []
        # SPF: smallest prime factor of number
        SPF = [0] * (n)
        for i in range(2, n):
            # for prime number, smallest prime factor is itself
            if SPF[i] == 0:
                SPF[i] = i
                primes.append(i)
            # for each i, iterate all available prime numbers stored in primes
            # to update SPF
            for j in range(0,len(primes)):
                #print(i,j, primes[j], SPF[i], primes, SPF)
                if primes[j] <= SPF[i] and i*primes[j] < n:
                    SPF[i * primes[j]] = primes[j]
                    #print(i,j, primes[j], SPF[i], primes, SPF)

        return len(primes)

# 3) variant of 1), assume all numbers are prime first, then for each number, if it is prime, make multiple of it to be non-prime
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
                return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i*i : n : i] = [False] * len(primes[i*i : n : i])
        return sum(primes)
