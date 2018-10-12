# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

# American keyboard

# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

# https://leetcode.com/problems/keyboard-row/

# 1）use the first letter of the word to decide which row
# o(NM) time where N is no.of words, M is maximum length of a word
# implementation based on list
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        # Define list of three possible list
        top_row =['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o','p']
        middle_row = ['a','s','d','f','g','h','j','k','l']
        bottom_row = ['z','x','c','v','b','n','m']
        rows = [top_row, middle_row, bottom_row]

        # Initiate the empty output words list
        output_words = []

        for word in words:
            flag = False
            # Find the
            if word[0].lower() in rows[0]:
                row_num = 0
            elif word[0].lower() in rows[1]:
                row_num = 1
            else:
                row_num = 2

            # Iterate through each letter in word
            for letter in word:
                if letter.lower() not in rows[row_num]:
                    flag = False
                    break
                else:
                    flag = True

            # Append to output list if flag is true
            if flag:
                output_words.append(word)

        return output_words

# 2) simplification of 1)
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        top_row = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o','p']
        middle_row = ['a','s','d','f','g','h','j','k','l']
        bottom_row = ['z','x','c','v','b','n','m']

        return [word for word in words if all(letter.lower() in top_row for letter in word) or all(letter.lower() in middle_row for letter in word) or all(letter.lower() in bottom_row for letter in word)]


# 3) one-liner solution based on 2)
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return [word for word in words if all(letter.lower() in ['q','w','e','r','t','y','u','i','o','p'] for letter in word) or all(letter.lower() in ['a','s','d','f','g','h','j','k','l'] for letter in word) or all(letter.lower() in ['z','x','c','v','b','n','m'] for letter in word)]


# 4) similar approach but using set, O(MN) time complexity
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        top_row, middle_row, bottom_row = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        result = []
        for word in words:
            word_set = set(word.lower())
            if word_set.issubset(top_row) or word_set.issubset(middle_row) or word_set.issubset(bottom_row):
                result.append(word)
        return result

# 5) one-liner based on set operations
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return [word for row in [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')] for word in words if set(word.lower()) <= row]

# 6) use regex
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # ?i means case-insensitive
        # * indicates zero or more times
        # | indicates or
        return list(filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words))

# 7) use set and performs and operations between sets
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a=set('qwertyuiop')
        b=set('asdfghjkl')
        c=set('zxcvbnm')
        ans=[]
        for word in words:
            t=set(word.lower())
            if a&t==t:
                ans.append(word)
            if b&t==t:
                ans.append(word)
            if c&t==t:
                ans.append(word)
        return ans

# 8) use dictionary
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        h = {c:i for i in range(3) for c in keyboard[i]}
        result = []
        for word in words:
            flag = None
            for c in word:
                x = c.lower()
                if flag is None:
                    flag = h[x]
                elif flag != h[x]:
                    flag = False
                    break
            if flag is not False:
                result.append(word)
        return result

# 9) another variant of using set and <= operations
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set("qwertyuiopQWERTYUIOP")
        row2 = set("asdfghjklASDFGHJKL")
        row3 = set("zxcvbnmZXCVBNM")

        return [word for word in words if set(word)<=row1 or
                                          set(word)<=row2 or
                                          set(word)<=row3]

# 10) uaw sum and map operations, maps word.count to each row of the keyboard
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = "qwertyuiopQWERTYUIOP"
        row2 = "asdfghjklASDFGHJKL"
        row3 = "zxcvbnmZXCVBNM"
        output = []
        for word in words:
            if (sum(map(word.count, row1)) == len(word) or sum(map(word.count, row2)) == len(word)
                or sum(map(word.count, row3)) == len(word)):
                output.append(word)
        return output

# 11) use set diff operations "-", if any word has letters from two rows, then any not will not pick the word
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return [w for w in words if any(not set(w.lower()) - row for row in (set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")))]
