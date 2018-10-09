# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

# Example 1:

# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


# Note:

# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.

# https://leetcode.com/problems/shortest-distance-to-a-character/

import itertools

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # init max area
        max_area = 0

        # function to calculate area from three points on cartesian plane
        # https://www.mathopenref.com/coordtrianglearea.html
        # https://en.wikipedia.org/wiki/Shoelace_formula
        def triangle_area(a,b,c):
            x1, y1 = a
            x2, y2 = b
            x3, y3 = c
            return (abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))))

        # use itertools to create combinations from the input list
        combinations = list(itertools.combinations(points,3))

        # iterate thru the combinations to compute the area
        for i in range(0,len(combinations)):
            area = triangle_area(combinations[i][0], combinations[i][1], combinations[i][2])
            # update max_area if it is smaller than area of current combination
            if max_area < area: max_area = area

        return (max_area)



