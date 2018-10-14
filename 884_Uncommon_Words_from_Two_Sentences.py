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

# 1) O(N) time to build the counter dictionary
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
        return list(key for key, val in word_count.items() if val == 1)

# 2) use collections.Counter() and set operations, O(N)
from collections import Counter
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """

        cnt_A = Counter(A.split())
        cnt_B = Counter(B.split())
        return [item for item in list(set(A.split()) ^ set(B.split())) if cnt_A[item] <= 1 and cnt_B[item] <= 1]


# 3) one-liner of 2), but less efficient due to recomputation of Counter dictionary
from collections import Counter
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        return [item for item in list(set(A.split()) ^ set(B.split())) if Counter(A.split())[item] <= 1 and Counter(B.split())[item] <= 1]

# 4) concatenate string A and B then find word that occur only once
from collections import Counter
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        count = Counter((A + " " + B).split())
        return [word for word in count if count[word]==1]

# 5) one-liner of 4)
from collections import Counter
class Solution:
    def uncommonFromSentences(self, A, B):
        return [word for word, count in Counter((A + " " + B).split()).items() if count == 1]


# 6) use two counters and find occurence of only once and not in another counter
from collections import Counter
class Solution:
    def uncommonFromSentences(self, A, B):
        ca, cb = Counter(A.split(" ")), collections.Counter(B.split(" "))
        return [w for w in ca if w not in cb and ca[w] == 1] + [w for w in cb if w not in ca and cb[w] == 1]

# 7) variant of 5
from collections import Counter
class Solution:
    def uncommonFromSentences(self, A, B):
        return [word for word, count in Counter(A.split() + B.split()).items() if count == 1]

# 8) use lambda function
from collections import Counter
class Solution:
    def uncommonFromSentences(self, A, B):
        return (lambda x: [word for word in x if x[word] == 1])(Counter((A + ' ' + B).split()))

