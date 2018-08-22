# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# https://leetcode.com/problems/merge-two-sorted-lists/description/

# 1) more concise iterative appraoch
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        merge_head = ListNode(None)
        head = merge_head

        # iterate the linked list l1 and l2
        while(l1 and l2):
            if(l1.val <= l2.val):
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        # if any of l1 or l2 is finished iteration
        head.next = l1 or l2

        # pass the first element of merge_head, return from the second element
        return merge_head.next

# 2) iterative approach
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if either of the input linked list is empty
        if not l1:
            return l2
        elif not l2:
            return l1

        # set the first element of returned linked list
        if l1.val <= l2.val:
            merge_head = ListNode(l1.val)
            l1 = l1.next
        else:
            merge_head = ListNode(l2.val)
            l2 = l2.next
        head = merge_head

        # iterate the linked list l1 and l2
        while(l1 and l2):
            if(l1.val <= l2.val):
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next

            head.next = node
            head = head.next

        # if any of l1 or l2 is finished iteration
        if l1 is None and l2 is not None:
            head.next = l2
        elif l1 is not None and l2 is None:
            head.next = l1

        return merge_head

# 3) recursive appraoch, more abstract
# recursively
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2

