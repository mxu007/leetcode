# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?

# https://leetcode.com/problems/linked-list-cycle/description/

# 1) use set to store address of visited node
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()

        while(head):
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False

# 2) use two points (fast and slow), Floyd's cycle finding algorithm
# https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow_p = head
        fast_p = head
        while(slow_p and fast_p and fast_p.next):
            # move pointer first then check if equals
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True

        return False
