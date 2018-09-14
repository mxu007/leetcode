# A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

# -2: turn left 90 degrees
# -1: turn right 90 degrees
# 1 <= x <= 9: move forward x units
# Some of the grid squares are obstacles.

# The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

# If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

# Return the square of the maximum Euclidean distance that the robot will be from the origin.



# Example 1:

# Input: commands = [4,-1,3], obstacles = []
# Output: 25
# Explanation: robot will go to (3, 4)
# Example 2:

# Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# Output: 65
# Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)

# https://leetcode.com/problems/walking-robot-simulation/description/

# 1) iterative approach, fail time complexity requirement
class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        x, y, direction = 0, 0, 0
        max_dist = 0
        # direction 0: north, 1: east, 2: south, 3: west
        for command in commands:
            if command == -1:
                direction = (direction + 1) % 4
            elif command == -2:
                direction = (direction - 1) % 4 if direction else 4-1

            else:
                steps_taken = 0
                while steps_taken < command:
                    if direction == 0:
                        if [x,y+1] not in obstacles: y = y + 1
                    elif direction == 1:
                        if [x+1,y] not in obstacles: x = x + 1
                    elif direction == 2:
                        if [x,y-1] not in obstacles: y = y - 1
                    elif direction == 3:
                        if [x-1,y] not in obstacles: x = x - 1
                    steps_taken += 1
            if x**2 + y**2 > max_dist: max_dist = x**2 + y**2

        return max_dist

# 2) use a python dictionary to improve obstacle checking time complexity as O(1) to find key for dictionary
# O(N+K) time complexity where N is length of commands and K is length of obstacles
import collections
class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        x, y, direction = 0, 0, 0
        max_dist = 0
        dict_x = collections.defaultdict()
        dict_y = collections.defaultdict()

        for obstacle in obstacles:
            if obstacle[0] not in dict_x:
                dict_x[obstacle[0]] = [obstacle[1]]
            else:
                dict_x[obstacle[0]].append(obstacle[1])

            if obstacle[1] not in dict_y:
                dict_y[obstacle[1]] = [obstacle[0]]
            else:
                dict_y[obstacle[1]].append(obstacle[0])

        # direction 0: north, 1: east, 2: south, 3: west
        for command in commands:
            if command == -1:
                direction = (direction + 1) % 4
            elif command == -2:
                direction = (direction - 1) % 4 if direction else 4-1

            else:
                steps_taken = 0
                while steps_taken < command:
                    if direction == 0:
                        if x not in dict_x or y+1 not in dict_x[x]: y = y + 1
                    elif direction == 1:
                        if y not in dict_y or x+1 not in dict_y[y]: x = x + 1
                    elif direction == 2:
                        if x not in dict_x or y-1 not in dict_x[x]: y = y - 1
                    elif direction == 3:
                        if y not in dict_y or x-1 not in dict_y[y]: x = x - 1
                    steps_taken += 1
            if x**2 + y**2 > max_dist: max_dist = x**2 + y**2

        return max_dist

# 3) further improvement of #2) to cut down unnecessary iterations
import collections
class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        x, y, direction = 0, 0, 0
        max_dist = 0
        dict_x = collections.defaultdict()
        dict_y = collections.defaultdict()

        for obstacle in obstacles:
            if obstacle[0] not in dict_x:
                dict_x[obstacle[0]] = [obstacle[1]]
            else:
                dict_x[obstacle[0]].append(obstacle[1])

            if obstacle[1] not in dict_y:
                dict_y[obstacle[1]] = [obstacle[0]]
            else:
                dict_y[obstacle[1]].append(obstacle[0])

        # direction 0: north, 1: east, 2: south, 3: west
        for command in commands:
            if command == -1:
                direction = (direction + 1) % 4
            elif command == -2:
                direction = (direction - 1) % 4

            else:
                if direction == 0 and x not in dict_x: y += command
                elif direction == 1 and y not in dict_y: x += command
                elif direction == 2 and x not in dict_x: y -= command
                elif direction == 3 and y not in dict_y: x -= command
                else:
                    steps_taken = 0
                    while steps_taken < command:
                        if direction == 0 and y+1 not in dict_x[x]: y = y + 1
                        elif direction == 1 and x+1 not in dict_y[y]: x = x + 1
                        elif direction == 2 and y-1 not in dict_x[x]: y = y - 1
                        elif direction == 3 and x-1 not in dict_y[y]: x = x - 1
                        steps_taken += 1

            if x**2 + y**2 > max_dist: max_dist = x**2 + y**2

        return max_dist

# 4) use map and set. O(N+K) time complexity where N is length of commands and K is length of obstacles
class Solution(object):
    def robotSim(self, commands, obstacles):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2:  #left
                di = (di - 1) % 4
            elif cmd == -1:  #right
                di = (di + 1) % 4
            else:
                for k in xrange(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)

        return ans



