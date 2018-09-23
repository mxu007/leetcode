# There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

# The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

# Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

# Example 1:

# Input: "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.


# Example 2:

# Input: "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.

# https://leetcode.com/problems/robot-return-to-origin/description/

# 1) if-else case, O(N) time
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0

        for i in moves:
            if (i == "R"):
                x += 1
            elif (i == "L"):
                x -= 1
            elif (i == "U"):
                y += 1
            else:
                y -= 1
        return (x==y==0)

# 2) use dictionary
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        mappings = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}
        return sum ([mappings[move][0] for move in moves ]) == 0 and sum ([mappings[move][1] for move in moves ]) == 0


# 3) use map, sum and zip
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        mappings = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}
        l = [mappings[move] for move in moves]
        # input "UD"
        # print(list(l))
        # [(0, 1), (0, -1)]
        # print(list(map(sum,zip(*l))))
        # [0, 0]
        # print(list(zip(l)))
        # [((0, 1),), ((0, -1),)]
        # print(list(zip(*l)))
        # [(0, 0), (1, -1)]
        # * operator to unpack argument list
        return (list(map(sum,zip(*l)))) == [0,0]


# 4) use list.count()
def judgeCircle(self, moves):
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

# 5) use map to count the character
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        l = map(moves.count, ['R','L','U','D'])
        return (l[0]==l[1])&(l[2]==l[3])


# 6) use collection.Counter, which is the python count dictionary
def judgeCircle(self, moves):
    c = collections.Counter(moves)
    return c['L'] == c['R'] and c['U'] == c['D']
