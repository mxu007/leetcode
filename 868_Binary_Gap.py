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

# 1) create a list to store position of binary 1
# then iterate through the list to find the pair-wise distance and find the max distance
# O(N) time and O(N) space where N is no.of binary positions
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
            return max([x - target_pos[j-1] for j,x in enumerate(target_pos)][1:])


# 2) 2-liner of 1)
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        target_pos = [i for i, char in enumerate(format(N, "b")) if char == '1']
        return max([x - target_pos[j-1] for j,x in enumerate(target_pos)][1:]) if len(target_pos) > 1 else 0

# 3) variant using zip
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        target_pos = [i for i, char in enumerate(format(N, "b")) if char == '1']
        return max([nex - pre for pre, nex in zip(target_pos, target_pos[1:])] or [0])

# 4) O(1) space and O(N) time, just iterate the binary string
# i to store index of previous 1, dist to store current matrix distance
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        pre = dist = 0
        for i, char in enumerate(bin(N)[2:]):
            if char == "1":
                dist = max(dist, i - pre)
                pre = i
        return dist

# 5) a flag to control the counter update
# iterate from left to right to find consecutive 1s. dist stores the current largest distance, variant of 4), also O(1) space
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        dist = 0
        counting = False
        counter = 0
        binary = bin(N)[2:]

        for index in range(0, len(binary)):

            if (binary[index] == '1') and (counting == False):
                counting = True

            elif (binary[index] != '1') and (counting == True):
                counter += 1

            elif (binary[index] == '1') and (counting == True):
                counter += 1
                if counter > dist:
                    dist = counter
                counter = 0

        return dist

# 6) strip('0') removes trailing and leading zeros, split('1') removes all 1 and separate the string into list of elements, then iterate and check length of each element
# N & N-1 removes 2^n, e.g. 8 (1000) & 7(0111) --> 0
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        return max(len(char) for char in bin(N)[2:].strip('0').split('1')) + 1 if N & (N-1) else 0

# 7) nested for loop, first locate '1', then serach from the RHS of the found 1 to update current maximum length
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = bin(N)[2:]
        result = 0

        for i in range(len(s)):
            if s[i] == "1":
                for j in range(i+1, len(s)):
                    if s[j] == "1":
                        result = max(result, j - i)
                        break
        return result

# 8) binary shift right 1 to check the bit of N, use variable flag to control the counting, variant of 5)
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        maxdist = 0
        i = 1
        dist = 0
        flag = False

        while i < N:
            b = (N & i)
            # print b, maxdist
            if b == 0:
                if flag:
                    dist += 1
            else:
                flag = True
                if dist > maxdist:
                    maxdist = dist
                dist = 1
            i = i<<1
        return maxdist
