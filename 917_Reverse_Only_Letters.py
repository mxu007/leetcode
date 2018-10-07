# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

# Example 1:

# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"


# Note:

# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122
# S doesn't contain \ or "

# https://leetcode.com/problems/reverse-only-letters/

# 1) extract letters from S and reverse, convert S into list and update char index by index
# O(N) time where N is no.of characters of the input string S
# O(N) space due to the additional list to store reversed letter string
# two-passes
import string
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """

        reversed_letters = [s for s in S if s in string.ascii_letters][::-1]
        i, S = 0, list(S)
        for j in range(len(S)):
            if S[j] in string.ascii_letters:
                S[j] = reversed_letters[i]
                i += 1
        return "".join(S)

# 2) single-passes approach, two pointers i and j control the left and right index
# O(N) time complexity, O(1) space (temp)
# can also use isalpha() function to check if a character is letters
import string
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        i, j = 0, len(S)-1
        S = list(S)
        while i < j:
            if S[i] in string.ascii_letters:
                while(S[j] not in string.ascii_letters):
                    j -= 1
                S[j], S[i] = S[i], S[j]
                i, j = i+1, j-1
            else:
                i += 1
        return "".join(S)

# 3) regex using replace() to replace letters into "{}" then use format to do multiple substitution
import string
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """

        return re.sub(r'[A-Za-z]', "{}", S).format(*[c for c in S[::-1] if c.isalpha()])
