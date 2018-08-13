# We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Return a list of all uncommon words.

# You may return the list in any order.



# Example 1:

# Input: A = "this apple is sweet", B = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:

# Input: A = "apple apple", B = "banana"
# Output: ["banana"]


# Note:

# 0 <= A.length <= 200
# 0 <= B.length <= 200
# A and B both contain only spaces and lowercase letters.

# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        # init dict to store word count
        word_count = {}

        # get two lists from string
        A = A.split(" ")
        B = B.split(" ")

        # update the count dictionary
        for word in A:
            word_count[word] = word_count.get(word,0) + 1

        for word in B:
            word_count[word] = word_count.get(word,0) + 1

        # return the key if it has only value 1, appears exxactly once in one of the sentences,
        # and does not appear in the other sentence
        return (list(key for key, val in word_count.items() if val == 1))

