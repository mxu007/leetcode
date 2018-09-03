# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

# https://leetcode.com/problems/remove-linked-list-elements/description/

# 1) itearte thru the linked list, O(N) time complexity
class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        head_copy = head
        last = None
        # iterate the linked list
        while(head):
            # move head as long as head.val equal val
            while(head.val == val):
                # before the last element of linked list
                if head.next is not None:
                    head.val = head.next.val
                    head.next = head.next.next
                # handle last element of linked list equal to val
                else:
                    # find the last node with val not equal val
                    if last is not None:
                        last.next = None
                    # all elements in the list have value of val, assign head_copy to None and will return
                    else:
                        head_copy = None
                    break
            last = head
            head = head.next

        return head_copy


# 2) cleaner itearative approach, handling begining and subsequent nodes differently
# head stores begining of valid node
class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head is not None and head.val == val:
            head = head.next
        current = head
        while current is not None:
            if current.next is not None and current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head

# 3) smart approach by creating additional node left to the original head, easier for later part of the handling
class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return []

        o_head = ListNode(None)
        o_head.next = head
        head = o_head

        while o_head and o_head.next:
            if o_head.next.val == val:
                o_head.next = o_head.next.next
            else:
                o_head = o_head.next

        return head.next

# 4) recursive approach, elegant solution
class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if (head == None): return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
