# Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

# If there aren't two consecutive 1's, return 0.



# Example 1:

# Input: 22
# Output: 2
# Explanation:
# 22 in binary is 0b10110.
# In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
# The first consecutive pair of 1's have distance 2.
# The second consecutive pair of 1's have distance 1.
# The answer is the largest of these two distances, which is 2.
# Example 2:

# Input: 5
# Output: 2
# Explanation:
# 5 in binary is 0b101.
# Example 3:

# Input: 6
# Output: 1
# Explanation:
# 6 in binary is 0b110.
# Example 4:

# Input: 8
# Output: 0
# Explanation:
# 8 in binary is 0b1000.
# There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.

# https://leetcode.com/problems/binary-gap/description/


class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """

        # init list to store pos of 1
        target_pos = []

        # convert input into binary
        string_N = format(N, "b")
        print(string_N, len(string_N))

        # if there is no consecutive 1 pair
        if (sum(int(x) for x in string_N) <= 1):
            return 0

        else:
            # iterate the binary string and find pos of 1s
            for i in range(0,len(string_N)):
                if int(string_N[i]) == 1:
                    target_pos.append(i)

            print(target_pos)
            print([x - target_pos[j-1] for j,x in enumerate(target_pos)][1:])
            # iterate the target_pos and calculate consecutive difference, find the max value
            return (max([x - target_pos[j-1] for j,x in enumerate(target_pos)][1:]) )
