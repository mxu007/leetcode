# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# https://leetcode.com/problems/longest-common-prefix/description/

# 1) use all function on iterable, O(N^2) time complexity
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_pre = ""
        if len(strs) == 0: return longest_pre
        elif len(strs) == 1: return strs[0]

        shortest_str = min(strs, key=len)

        for i in range(len(shortest_str)):
            if all([x.startswith(shortest_str[:i+1]) for x in strs]):
                longest_pre = shortest_str[:i+1]
            else:
                break

        return longest_pre

# 2) small variant of 1)
class Solution:
    def longestCommonPrefix(self, strs):
        longest_pre = ""
        if not strs: return longest_pre
        shortest_str = min(strs, key=len)
        for i in range(len(shortest_str)):
            if all([x.startswith(shortest_str[:i+1]) for x in strs]):
                longest_pre = shortest_str[:i+1]
            else:
                break
        return longest_pre

# 3) variant of 1)
 def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

# 4) use zip, set and length of set, if length of set greater than 1, return
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            #print(i,letter_group,set(letter_group))
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

# 5) zip, set, and len of set
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]; rtype: str
        """
        sz, ret = zip(*strs), ""
        # looping corrected based on @StefanPochmann's comment below
        for c in sz:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret


# 6) use min max on list of strings
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]; rtype: str
        """
        if not strs:
            return ""
        min_s = min(strs)
        max_s = max(strs)
        print(min_s, max_s)
        if not min_s:
            return ""
        for (i,v) in enumerate(min_s):
            if max_s[i] != min_s[i]:
                return max_s[:i]
        return min_s[:]

# 7) horizontal scanning, O(S) time complexity where S is the number of all characters in all strings
# outer loop for each individual words, inner loop for each individual chars
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]; rtype: str
        """
        if not strs: return ""
        longest_pre = strs[0]
        for i in range(1,len(strs)):
            while(strs[i].find(longest_pre)!=0):
                longest_pre = longest_pre[:-1]
                if len(longest_pre) == 0: return ""
        return longest_pre


# 8) vertical scanning, O(S) time complexity where S is the number of all characters in all strings
# outer loop for each individual char, inner loop for each individual words, better optimized vs 7) to deal case where we have very short word at the end of list
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]; rtype: str
        """
        if not strs: return ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1,len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        return strs[0]


# 9) divide and conquer with recursive call, O(S) time complexity where S is the number of all characters, O(mlog(n)) space complexity, n is number of elements in input list, m is the number of characters in each word. there will be log(n) recursive calls, each requires m space
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]; rtype: str
        """
        def commonPrefix(left,right):
            min_len = min(len(left), len(right))
            for i in range(min_len):
                if left[i] != right[i]:
                    return left[:i]
            return left[:min_len]

        def find_longestCommonPrefix(strs, left_index, right_index):
            if left_index == right_index:
                return strs[left_index]

            # recursive call
            else:
                mid_index = (left_index + right_index)//2
                lcpLeft = find_longestCommonPrefix(strs,left_index, mid_index)
                lcpRight = find_longestCommonPrefix(strs,mid_index+1,right_index)
                return commonPrefix(lcpLeft,lcpRight)

        if not strs: return ""
        return find_longestCommonPrefix(strs, 0, len(strs)-1)
