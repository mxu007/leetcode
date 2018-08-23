# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

# Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

# Given two (axis-aligned) rectangles, return whether they overlap.

# Example 1:

# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
# Example 2:

# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
# Notes:

# Both rectangles rec1 and rec2 are lists of 4 integers.
# All coordinates in rectangles will be between -10^9 and 10^9.

# https://leetcode.com/problems/rectangle-overlap/description/

# 1) compare bottom left and top right corner coordinates
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # # if the second rectangle is on the left, right, top or bottom of the first rectangle
        return False if rec2[2] <= rec1[0] or rec2[0] >= rec1[2] or rec2[1] >= rec1[3] or rec2[3] <= rec1[1] else True

# 2) calculate if overlapping area is greater than 0
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # rec1: x1,y1, x2,y2
        # rec2: x3,y3, x4,y4
        # the left (smaller) one between x4 and x2 minus the right (larger) one between x1 and x3
        # the bottom (smaller) one between y2 and y4 minus the upper (larger) one between y3 and y1
        width = max(min(rec1[2],rec2[2])-max(rec1[0],rec2[0]),0)
        height = max(min(rec1[3],rec2[3])-max(rec1[1],rec2[1]),0)
        return width * height > 0
