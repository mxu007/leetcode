# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

# Example 1:
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
# Example 2:
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
# Note:
# cost will have a length in the range [2, 1000].
# Every cost[i] will be an integer in the range [0, 999].

# https://leetcode.com/problems/min-cost-climbing-stairs/description/

# https://leetcode.com/problems/min-cost-climbing-stairs/description/

# 1) dynamic programming, bottom-up appraoch
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        length = len(cost)
        total_cost = [None] * (length)
        total_cost[0], total_cost[1] = cost[0], cost[1]

        # at step i, the total cost equals the min value between come from step i-1 or step i-2
        # plus the cost of step i
        for i in range(2, length):
            total_cost[i] = min(total_cost[i-1],total_cost[i-2]) + cost[i]
            #print(i, total_cost)

        # at top step N, it must comes from either N-1 th step or N-2 th
        # find the min value
        return min(total_cost[length-1], total_cost[length-2])


# 2) dynamic programming, top-bottom appraoch with memorization
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # function to compute minimum cost at each step with memorization
        def compute_min_cost(i,total_cost):
            if total_cost[i] is None:
                total_cost[i] = min(compute_min_cost(i-1,total_cost), compute_min_cost(i-2,total_cost)) + cost[i]
            return total_cost[i]

        # we don't know the cost of the top, so assign it to be zero for the recursive call
        cost.append(0)
        length = len(cost)
        # init global list
        total_cost = [None] * (length)
        total_cost[0], total_cost[1] = cost[0], cost[1]

        # top-bottom appraoch with memorization
        return compute_min_cost(length-1,total_cost)
