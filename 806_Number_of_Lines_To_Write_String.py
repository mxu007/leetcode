# We are to write the letters of a given string S, from left to right into lines.
# Each line has maximum width 100 units, and if writing a letter would cause the
# width of the line to exceed 100 units, it is written on the next line. We are
# given an array widths, an array where widths[0] is the width of 'a', widths[1]
# is the width of 'b', ..., and widths[25] is the width of 'z'.

# Now answer two questions: how many lines have at least one character from S, and
# what is the width used by the last such line? Return your answer as an integer
# list of length 2.

# Example :
# Input:
# widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
# S = "bbbcccdddaaa"
# Output: [2, 4]
# Explanation:
# All letters except 'a' have the same length of 10, and
# "bbbcccdddaa" will cover 9 * 10 + 2 * 4 = 98 units.
# For the last 'a', it is written on the second line because
# there is only 2 units left in the first line.
# So the answer is 2 lines, plus 4 units in the second line.

# Example :
# Input:
# widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
# S = "abcdefghijklmnopqrstuvwxyz"
# Output: [3, 60]
# Explanation:
# All letters have the same length of 10. To write all 26 letters,
# we need two full lines and one line with 60 units.

# Note:

# The length of S will be in the range [1, 1000].
# S will only contain lowercase letters.
# widths is an array of length 26.
# widths[i] will be in the range of [2, 10].

# https://leetcode.com/problems/number-of-lines-to-write-string/description/

# 1) use dictionary, O(n) time to traverse the S, where n is no.of elements in S
# O(1) space, constant space to create the dictionary mappings
class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """

        # Construct list of alphabets
        alphabets = []
        for letter in range(97,123):
            alphabets.append(chr(letter))

        # Build dictionary to store alphabet-width pair
        width_dict = {}
        for i, letter in enumerate(alphabets):
            width_dict[letter] = widths[i]

        # Initiate row an space count
        row_count = 1
        space_count = 0

        # Iterate through input S
        for s in S:
            if (width_dict[s]+space_count == 100):
                row_count += 1
                space_count = 0
            elif (width_dict[s]+space_count > 100):
                row_count += 1
                space_count = width_dict[s]
            else:
                space_count += width_dict[s]

        return row_count, space_count

# 2) more concise version of 1)
import string
class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        width_dict = {letter:widths[i] for i,letter in enumerate(string.ascii_lowercase)}
        # or widths_dict = dict(zip(string.ascii_lowercase, widths))
        row_count, space_count = 1, 0
        for s in S:
            if (width_dict[s]+space_count > 100):
                row_count += 1
                space_count = width_dict[s]
            else:
                space_count += width_dict[s]

        return [row_count, space_count]


# 3) using ord() function and simplying the if logic
import string
class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        row_count, space_count = 1, 0
        for s in S:
            width = widths[ord(s)-ord('a')]
            row_count += 1 if space_count + width > 100 else 0
            space_count = width if space_count + width > 100 else space_count + width
        return [row_count,space_count]
