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

# 2) Recursive approach, O(N) compexity
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

# 3） use fast and slow pointers to find mid pos
# from mid point, reverse the second half of the linked list
# e.g. 1>2>3>2>1, second half 3>2>1 reversed as 1>2>3
# compare from head (left-most) and node (right most)
# O(N) time complexity, O(1) space
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
