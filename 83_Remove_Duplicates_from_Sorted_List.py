# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:

# Input: 1->1->2
# Output: 1->2
# Example 2:

# Input: 1->1->2->3->3
# Output: 1->2->3

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# 1)
# notice the input is a sorted linked list, hence does not reqiure list or dictionary to store past occurence
# also for linked list, the pointer is from current node to the next node, one directional, hence cannot change the link from previous node to current node. can only change from current node to next node

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        head_copy = head

        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return head_copy

# 2) The list is unnecessary as the input linked list is sorted
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        head_copy = head
        item =[]

        while head.next:
            if head.val not in item:
                item.append(head.val)

            if head.next.val in item:
                head.next = head.next.next
            else:
                head = head.next

        return head_copy
