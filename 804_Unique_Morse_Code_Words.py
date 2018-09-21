# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

# For convenience, the full table for the 26 letters of the English alphabet is given below:

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

# Return the number of different transformations among all words we have.

# Example:
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation:
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."

# There are 2 different transformations, "--...-." and "--...--.".


# Note:

# The length of words will be at most 100.
# Each words[i] will have length in range [1, 12].
# words[i] will only consist of lowercase letters.

# https://leetcode.com/problems/unique-morse-code-words/description/

# 1) use dictionary to creat mapping between lowercase alphabet to morse code
# O(N) space where N is number of word in input list words
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        translation = {}
        morsecode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in range(26):
            translation[chr(97+i)] = morsecode[i]

        output=[""]*len(words)
        j = 0
        for word in words:
            for letter in word:
                output[j] += translation[letter]
            j+=1

        return len(list(set(output)))


# 2) cleaner version of 1)
from string import ascii_lowercase
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morsecode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        translation = dict(zip(ascii_lowercase,morsecode))
        output = ["".join(translation[letter] for letter in word) for word in words]
        return len(set(output))


# 3) one-liner
class Solution:
    def uniqueMorseRepresentations(self, words):
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len({"".join([codes[ord(l) - ord("a")] for l in word]) for word in words})
