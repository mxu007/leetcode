# Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

# Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

# So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

# Note:
# Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be warmed.
# All the heaters follow your radius standard and the warm radius will the same.
# Example 1:
# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
# Example 2:
# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.

# https://leetcode.com/problems/heaters/description/

# 1) brute-force, O(MN), exceed time limit
class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        min_dists = []
        for house in houses:
            min_dist = min([abs(heater-house) for heater in heaters])
            min_dists.append(min_dist)

        return max(min_dists)

# 2) sort houses and heaters, then just iterate the houses
# Nlog(N) for sorting, the iteration is simply N as index of heaters is not reset every time it enters the while loop
class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        i, radius = 0, 0
        for house in houses:
            while i < len(heaters) and heaters[i] < house:
                i += 1
            # first heater on after the current house
            if i == 0:
                radius = max(radius, heaters[i]-house)
            # last heater, so just compare current radium with distance between last house and last heater
            # as the house is sorted
            elif i == len(heaters):
                return max(radius, houses[-1]-heaters[-1])
            # handle case in between first and last heaters
            else:
                radius = max(radius, min(heaters[i]-house, house-heaters[i-1]))
        return radius

# 3) sort house and radius, locate two closest heaters for each house
class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters) + [float('inf')]
        i, radius = 0, 0
        for house in sorted(houses):
            while house >= sum(heaters[i:i+2]) / 2.0:
                i += 1
            radius = max(radius, abs(heaters[i] - house))
        return radius

# 4) sort and apply binary search, O(Mlog(N)) time complexity
class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        max_dist = 0
        for house in houses:
            left, right = 0, len(heaters) - 1
            # ensure we have two candicates at least
            # we don't want to find the exact match, we want to find closest two heaters
            while right - left > 1:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid
                else:
                    right = mid
            max_dist = max(max_dist, min(abs(heaters[left]-house),abs(heaters[right]-house)))

        return max_dist

