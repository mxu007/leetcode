# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

# Each LED represents a zero or one, with the least significant bit on the right.


# For example, the above binary watch reads "3:25".

# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

# Example:

# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
# Note:
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

# https://leetcode.com/problems/binary-watch/description/


# 1) short and elegant solution
import itertools
class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # convert hour and minute to binary string then count number of 1
        return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if bin(h).count('1') + bin(m).count('1') == num ]


# 2) using itertools and list
import itertools
class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # init the result
        result = []
        # possible value of hours and minutes
        hours = [8,4,2,1]
        minutes = [32,16,8,4,2,1]

        # from input num, generate all possible permutations for hour and minute
        allocations = [[i,j] for i in range(num+1) for j in range(num+1) if i+j == num]
        print("allocations:" , allocations)

        # iterate the permutation of allocations
        for allocation in allocations:
            print("allocation:", allocation[0], allocation[1])
            # for each allocation: genreate combinations of hour and minute
            alloc_hours = [list(comb) for comb in itertools.combinations(hours, allocation[0])] if allocation[0] > 0 else [[0]]
            alloc_minutes = [list(comb) for comb in itertools.combinations(minutes, allocation[1])] if allocation[1] > 0 else [[0]]
            print(alloc_hours, alloc_minutes, len(alloc_hours), len(alloc_minutes))
            # iterate each possible hour and minute pairs
            # ignore case where hour is greater or equal than 12 and minutes greater or equal than 60
            for alloc_hour in alloc_hours:
                for alloc_minute in alloc_minutes:
                    sum_hour = sum(alloc_hour)
                    sum_minute = sum(alloc_minute)
                    if (sum_hour<12 and sum_minute < 60):
                    #https://stackoverflow.com/questions/13806708/formatting-time-for-a-digital-clock
                        result.append("%d:%02d" %(sum_hour, sum_minute))
        return(result)



