# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.



# Example 1:

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.


# Note:

# The number of nodes in the given list will be between 1 and 100.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from math import ceil

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # save a copy of head
        head_copy = head

        # init length of the linked list
        length = 1

        # iterate the linked list
        while (head.next != None):
            length += 1
            head = head.next

        # compute mid point for odd and even number of elements
        mid = ceil(length/2) if length%2!=0 else int(length/2+1)
        #print(mid)

        # move to the mid position
        for i in range(1,mid):
            head_copy = head_copy.next

        # return the linked list
        return (head_copy)


