# Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

# Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

# Examples:
# Input:
# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"

# Input:
# letters = ["c", "f", "j"]
# target = "c"
# Output: "f"

# Input:
# letters = ["c", "f", "j"]
# target = "d"
# Output: "f"

# Input:
# letters = ["c", "f", "j"]
# target = "g"
# Output: "j"

# Input:
# letters = ["c", "f", "j"]
# target = "j"
# Output: "c"

# Input:
# letters = ["c", "f", "j"]
# target = "k"
# Output: "c"

# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

# 1) use bisect
import bisect
class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        #  returns an insertion point which comes after (to the right of) any existing entries of item in list
        loc = bisect.bisect_right(letters, target)
        return letters[0] if loc == len(letters) else letters[loc]

# 2) O(N) sequantial search
class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # iterate the letters
        for letter in letters:
            # get ascii code
            if ord(letter) > ord(target):
                return letter
        return letters[0]

# 3) O(logN) binary search
class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # case for wrapping around
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        # specify left and right
        # iterate until left equals right, return that index and orginal letter at that index
        left, right = 0, len(letters)-1
        while left < right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return letters[left]
