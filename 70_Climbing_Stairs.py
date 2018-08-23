
# 1) dp without memorization
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n== 2:
            return 2
        else:
            # to reach step n, either come from step n-1 or step n-2
            return (self.climbStairs(n-2) + self.climbStairs(n-1))

# 2) dp with memorization
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n== 2:
            return 2

        # global list result
        result = [None] * (n+1)
        result[0],result[1],result[2] = 0,1,2

        # with memorization
        def compute(i,result):
            if result[i] is None:
                result[i] = (compute(i-1,result)+compute(i-2,result))
            return result[i]

        return compute(n, result)

# 3) dp with bottom up using list, O(N) space complexity
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n== 2:
            return 2

        result = [None] * (n+1)
        result[0],result[1],result[2] = 0,1,2

        for i in range(3,n+1):
            result[i] = result[i-1] + result[i-2]

        return result[n]


# 4) dp with bottom up without using list
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n== 2:
            return 2

        prev_prev, prev = 1, 2

        for i in range(3,n+1):
            curr = prev_prev + prev
            prev_prev = prev
            prev = curr

        return curr
