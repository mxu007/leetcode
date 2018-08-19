# In a string S of lowercase letters, these letters form consecutive groups of the same character.

# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

# The final answer should be in lexicographic order.



# Example 1:

# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
# Example 2:

# Input: "abc"
# Output: []
# Explanation: We have "a","b" and "c" but no large group.
# Example 3:

# Input: "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]


# Note:  1 <= S.length <= 1000

# https://leetcode.com/problems/positions-of-large-groups/description/

# 1) use regex
class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        # contents of group1
        # \1{2,} matches the same text as most recently matched by the 1st capturing group
        return [[r.start(), r.end() - 1] for r in re.finditer(r'(\w)\1{2,}', S)]


# 2) shorter version using only one set of index i and j
class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        # init index and get length of the list
        i, j, N = 0, 0, len(S)
        res = []

        while j < N:
            # increment j as long as S[j] equals S[i]
            while j < N and S[j] == S[i]: j += 1
            # end while loop means now S[j] AND S[i] are different, check if group has 3 or more char
            if j - i >= 3: res.append((i, j - 1))
            # move the index i to equal j
            i = j
        return res

# 3) more complex appraoch
class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        # init counter, result, previous value and start & end index
        counter = 1
        result = []
        prev = S[0]
        start, end = 0, 0

        # iterate from second element to end of list
        for i in range(1, len(S)):
            # if current equals to previous, update counter and end index
            if S[i] == prev:
                counter += 1
                end += 1
            # if not equal, check if counter is greater or equal to three
            else:
                if counter >= 3:
                    result.append([start,end])
                counter = 1
                start, end = i, i
            # reach end of list
            if i == len(S)-1:
                if counter >= 3:
                    result.append([start,end])
                break
            prev = S[i]
        return(result)

