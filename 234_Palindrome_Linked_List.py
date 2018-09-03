# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# https://leetcode.com/problems/palindrome-linked-list/description/

# 1) O(N) time and O(N) space
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        result = []
        while(head):
            result.append(head.val)
            head = head.next
        #print(result)
        return result == result[::-1]

# 2) Recursive approach
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def recur_isPalindrome(right):
            if right == None: return True
            isp = recur_isPalindrome(right.next)
            if isp == False:
                return False
            isp_l = (right.val == self.left.val)
            self.left = self.left.next
            return isp_l

        self.left = head
        result = recur_isPalindrome(head)
        return result
