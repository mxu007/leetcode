# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:

# Input: "hello"
# Output: "holle"
# Example 2:

# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".

# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

# 1) convert input string to list and construct an index list to store index for vowel char
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # list of vowels
        vowels = ['a','e','i','o','u','A','E','I','O','U']

        # list to store index of char in string that is vowel
        indices = []
        for i in range(len(s)):
            if s[i] in vowels:
                indices.append(i)
        # convert string to list as string is immutable
        s = list(str(s))
        # get length of indices list
        length = len(indices)
        # swap
        for j in range(length//2):
            temp = s[indices[j]]
            s[indices[j]] = s[indices[length-1-j]]
            s[indices[length-1-j]] = temp
            print(temp, s[indices[j]], s[indices[length-1-j]])

        return ("".join(s))

# 2) use re
import re
class Solution(object):
    def reverseVowels(self, s):
        # (?i) is an inline flag corresponding to re.IGNORECASE. In other words (?i)[aeiou] is equivalent to [aeiouAEIOU].
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

# 3) use two pointers
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        L = list(s)
        i = 0
        j = len(L) - 1
        while i < j:
            while i < j and L[i] not in vowels:
                i += 1
            while j > i and L[j] not in vowels:
                j -= 1
            L[i], L[j] = L[j], L[i]
            i += 1
            j -= 1
        return ''.join(L)
