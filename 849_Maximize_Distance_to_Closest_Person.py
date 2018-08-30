# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

# There is at least one empty seat, and at least one person sitting.

# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

# Return that maximum distance to closest person.

# Example 1:

# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation:
# If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# Example 2:

# Input: [1,0,0,0]
# Output: 3
# Explanation:
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# Note:

# 1 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.

# https://leetcode.com/problems/maximize-distance-to-closest-person/description/

# 1) use two list to store groupent consecutive zeroes and index for consecutive zeroes
# 2-pass
class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # count consecutive 0s
        zero_group = []
        zero_groups = []
        for i in range(len(seats)):
            # seat is empty, append to zero_group
            if seats[i] == 0:
                zero_group.append(i)
                # reach end of input list
                if i == len(seats)-1: zero_groups.append(zero_group)
            # seat is occupied, append zero_group to all
            elif seats[i] == 1 and len(zero_group) > 0:
                zero_groups.append(zero_group)
                zero_group = []

        # iterate the index of zeros
        max_dist = 0
        for zero_group in zero_groups:
            # if consecutive index starts from 0 or ends with len(seats)-1
            # distance is length of consecutive index
            if 0 in zero_group or len(seats) -1 in zero_group:
                length = len(zero_group)
            else:
                length = len(zero_group) // 2 + len(zero_group) % 2
            if length > max_dist: max_dist = length

        return max_dist

# 2) use itertools groupby
# if there is an empty seat on left edge, the distance is seats.index(!)
# on the right edge, seats[::-1].index(1)
# http://ls.pwd.io/2013/05/create-groups-from-lists-with-itertools-groupby/
import itertools
class Solution(object):
    def maxDistToClosest(self, seats):
        ans = 0
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K+1)//2)

        return max(ans, seats.index(1), seats[::-1].index(1))


# 3 two pointers to move based on 0 or 1
# r moves for 0, l moves for 1
# single-pass
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        l, r, res, temp = 0, 0, 1, 0
        for i, v in enumerate(seats):
            if v == 0:
                r += 1
            elif v == 1:
                r = i
                if seats[l] == 0:  # if starts with zero
                    res = r - l
                else:
                    temp = (r-l-1) // 2 if (r-l-1) % 2 == 0 else (r-l) // 2 # odd or even

                    if temp > res:
                        res = temp
                l = i

        return res if res > r-l else r-l  # if starts with 1 and ends with zero

