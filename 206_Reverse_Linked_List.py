# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

# https://leetcode.com/problems/reverse-linked-list/description/

# 1) Iteartive Approach
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # the linked list to be returned
        reverse_head = None

        # curr is the intermediate variable to retrieve from original linked list
        # and update the new one
        while(head):
            # get the head of old linked list
            curr = head
            # udpate head
            head = head.next
            # update curr.next
            curr.next = reverse_head
            # update reverse head
            reverse_head = curr

        return reverse_head

# 1) Recursive Approach
class Solution(object):
    def reverseList(self, head, prev=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # reach end of original linked list
        if not head:
            return prev

        # curr becomes the new head, moving in the original direction
        # head constructs in the reverse direction, become prev in the function call and eventually get returned
        curr, head.next = head.next, prev
        return self.reverseList(curr, head)
