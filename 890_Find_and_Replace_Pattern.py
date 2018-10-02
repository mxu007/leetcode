# You have a list of words and a pattern, and you want to know which words in words matches the pattern.

# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

# (Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

# Return a list of the words in words that match the given pattern.

# You may return the answer in any order.


# Example 1:

# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
# since a and b map to the same letter.


# Note:

# 1 <= words.length <= 50
# 1 <= pattern.length = words[i].length <= 20

# https://leetcode.com/problems/find-and-replace-pattern/

# 1) the char-char mapping is unique one-to-one between word and patterns, so use two dictionaries
# O(MN) time where M is no.of words and N is maximum char length for word in words
# O(N) space for the two dictionary
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result = []
        for word in words:
            if len(word) == len(pattern):
                word_to_pattern_dict = {}
                pattern_to_word_dict = {}
                flag = True
                for i, char in enumerate(pattern):
                    if char not in pattern_to_word_dict and word[i] not in word_to_pattern_dict:
                        pattern_to_word_dict[char] = word[i]
                        word_to_pattern_dict[word[i]] = char
                    elif char in pattern_to_word_dict and pattern_to_word_dict[char] == word[i]:
                        continue
                    else:
                        flag = False
                        break
                if flag: result.append(word)
        return result

# 2) just use single dicitonary with word-to-pattern matching
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result = []
        for word in words:
            if len(word) == len(pattern):
                word_to_pattern_dict = {}
                flag = True
                for i, char in enumerate(pattern):
                    if word[i] not in word_to_pattern_dict and char not in word_to_pattern_dict.values():
                        word_to_pattern_dict[word[i]] = char
                    elif word[i] in word_to_pattern_dict and word_to_pattern_dict[word[i]] == char:
                        continue
                    else:
                        flag = False
                        break
                if flag: result.append(word)
        return result

# 3) just use single dictionary with pattern-to-word matching
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result = []
        for word in words:
            if len(word) == len(pattern):
                pattern_to_word_dict = {}
                flag = True
                for i, char in enumerate(pattern):
                    if char not in pattern_to_word_dict and word[i] not in pattern_to_word_dict.values():
                        pattern_to_word_dict[char] = word[i]
                    elif char in pattern_to_word_dict and pattern_to_word_dict[char] == word[i]:
                        continue
                    else:
                        flag = False
                        break
                if flag: result.append(word)
        return result

# 4) normalize string to standard pattern, e.g. "deq" --> "abc" by using dict.get() with default set to len(dict()), very smart move
# at time of return, offset by 97 which is the ascii value of letter `a`
# requires construction of addtional function "found"
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def gen_pattern(word):
            count_dict = {}
            for char in word: count_dict[char] = count_dict.get(char, len(count_dict))
            # print("".join(chr(count_dict[char]+97) for char in word))
            # e.g. "deq" --> "abc"
            return "".join(chr(count_dict[char]+97) for char in word)
        return  [word for word in words if gen_pattern(word) == gen_pattern(pattern)]


# 5) similar to approach 4, normalize the pattern into numbers
# requires sorting, less ideal
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result = []
        pattern_dict = {}
        for i, val in enumerate(pattern):
            pattern_dict[val] = pattern_dict.get(val, []) + [i]

        # print(sorted(pattern_dict.values()))
        # "abb" --> [[0], [1, 2]]

        for word in words:
            word_dict = {}
            for i, val in enumerate(word):
                word_dict[val] = word_dict.get(val, []) + [i]

            if sorted(word_dict.values()) == sorted(pattern_dict.values()):
                result.append(word)
        return result

# 6) concise double dictionary
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(w):
            m1, m2 = {}, {}
            return all((m1.setdefault(i, j), m2.setdefault(j, i)) == (j, i) for i, j in zip(w, pattern))
        return list(filter(match, words))

# 7) check the length of set and length of set when characters are zipped together
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def is_iso(a):
            return len(a) == len(pattern) and len(set(a)) == len(set(pattern)) == len(set(zip(a, pattern)))
        return list(filter(is_iso, words))
