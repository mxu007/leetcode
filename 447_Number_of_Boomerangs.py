# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

# Example:
# Input:
# [[0,0],[1,0],[2,0]]

# Output:
# 2

# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

# https://leetcode.com/problems/number-of-boomerangs/description/

# efficient implementation using dictionary and get method
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        counter = 0

        # function to calculate square distance between points
        # avoid square root to improve computation efficiency
        def cal_dist(a,b):
            x_a, y_a = a[0], a[1]
            x_b, y_b = b[0], b[1]
            return (x_a-x_b)**2 + (y_a-y_b)**2

        # iterate all the points
        for a in points:
            # init dictionary for the point a being currently iterated
            dist_dict = {}
            # iterate remaining points to construct dist-count pair
            for b in points:
                dist = cal_dist(a,b)
                dist_dict[dist] = dist_dict.get(dist,0) + 1
            # add permutations of 2 with same distance to the current point a
            for key in dist_dict:
                counter += dist_dict[key] * (dist_dict[key]-1)

        return counter

# inefficient memory allocation
import itertools as it
import math
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def cal_dist(a,b):
            x_a, y_a = a[0], a[1]
            x_b, y_b = b[0], b[1]
            # print(x_a,x_b,y_a,y_b)
            # print("dist:", math.sqrt( (x_a-x_b)**2 + (y_a-y_b)**2 ))
            return math.sqrt( (x_a-x_b)**2 + (y_a-y_b)**2 )

        counter = 0
        boomerangs = list(it.combinations(points, 3))
        #print(boomerangs)

        for boomerang in boomerangs:
            pairs = list(it.permutations(boomerang))
            for pair in pairs:
                # print(pair)
                if cal_dist(pair[0],pair[1]) == cal_dist(pair[0],pair[2]):
                    counter += 1
        return counter
