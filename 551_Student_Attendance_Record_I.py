# You are given a string representing an attendance record for a student. The record only contains the following three characters:
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

# You need to return whether the student could be rewarded according to his attendance record.

# Example 1:
# Input: "PPALLP"
# Output: True
# Example 2:
# Input: "PPALLL"
# Output: False

# https://leetcode.com/problems/student-attendance-record-i/description/

# 1) using regex
import re
class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Regex
        # "(L){3,}" consecutive L for 3 or more times in the string
        # (A).*\1  A two times anywhere in the string
        return False if bool(re.search(r"(L){3,}",s)) or bool(re.search(r"(A).*\1",s)) else True


# 2) using dictionary and list iteration
class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # init the dictionary, 'A' record number of absence, 'L': record number of three consecutive late
        attendance = {'A':0, 'L':0}
        # iterate the input list
        for i in range(0,len(s)):
            # handle case for Absence and late only
            if s[i] == 'A':
                attendance[s[i]] = attendance.get(s[i]) + 1
            # capture any three consecutive late
            elif s[i] == 'L' and i >=2:
                if s[i]==s[i-1]==s[i-2]:
                    attendance[s[i]] = attendance.get(s[i]) + 1

        return False if (attendance['A'] > 1 or attendance['L'] >=1) else True
