# Given an array of characters, compress it in-place.

# The length after compression must always be smaller than or equal to the original array.

# Every element of the array should be a character (not int) of length 1.

# After you are done modifying the input array in-place, return the new length of the array.


# Follow up:
# Could you solve it using only O(1) extra space?


# Example 1:
# Input:
# ["a","a","b","b","c","c","c"]

# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
# Example 2:
# Input:
# ["a"]

# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]

# Explanation:
# Nothing is replaced.
# Example 3:
# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
# Notice each digit has it's own entry in the array.
# Note:
# All characters have an ASCII value in [35, 126].
# 1 <= len(chars) <= 1000.

# https://leetcode.com/problems/string-compression/description/

# 1) compress in-place, use two pointers and variable count to store number of consecutive occurence
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # two pointers, i for slow, j for fast, iterate the list
        i, count = 0, 1
        for j in range(1,len(chars)):
            # char different than slow
            if chars[j] != chars[i]:
                i += 1
                # add count only if count greater than 1
                # if count if 11, add two char "1" and "1"
                if count > 1:
                    chars[i:i+len(str(count))] = [d for d in str(count)]
                    # move i to the new char
                    i += len(str(count))
                chars [i] = chars[j]
                # reset count
                count = 1
            # reach end of list and count greater than 1
            elif j==len(chars)-1 and count>=1:
                # make space for count
                i += 1
                # additional offset of 1 taking the current iterate into consideration
                # add count char
                chars[i:i+len(str(count))] = [d for d in str(count+1)]
                # move slow index of i, as there is no subsequent char, no need make addiotnal space, hence offset by -1
                i += len(str(count+1)) -1
            else:
                count += 1
        # indicate number of elements in the final list
        return i+1

# 2) cleaner version without using slow/fast pointers
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        def cntCntgns(chars, c): #count contignous char in chars
            i = 0
            for char in chars:
                if char == c:
                    i += 1
                else:
                    return i
            else:
                return i

        i = 0
        while i < len(chars):
            c = chars[i]
            cntc = cntCntgns(chars[i:], c)
            if cntc != 1:
                chars[i + 1:i + cntc] = str(cntc)
                i += 2
                continue
            else:
                i += 1
                continue

# 3) anchor and write are similar to slow and fast pointers
class Solution(object):
    def compress(self, chars):
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write
