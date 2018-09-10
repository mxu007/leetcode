# Write a program to find the node at which the intersection of two singly linked lists begins.


# For example, the following two linked lists:

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.


# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

# https://leetcode.com/problems/intersection-of-two-linked-lists/description/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1) nested loop structure, O(mn) time complexity, exceeds time limit
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        headB_copy = headB
        while headA:
            headB = headB_copy
            while headB:
                if headB == headA:
                    return headB
                headB = headB.next
            headA = headA.next

        return None

# 2) using difference of node counts, O(m+n) time complexity, O(1) space
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        headA_copy, headB_copy = headA, headB
        length_A, length_B = 0, 0

        while headA:
            length_A += 1
            headA = headA.next

        while headB:
            length_B += 1
            headB = headB.next

        headA, headB = headA_copy, headB_copy

        for i in range (abs(length_A-length_B)):
            if length_A >= length_B:
                headA = headA.next
            else:
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next
        return None

# 3) use dictionary to store all the addresses, can use built-in dictionary or collections.defaultdict
import collections
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodesA = collections.defaultdict()
        while headA:
            nodesA[headA] = True
            headA = headA.next

        while headB:
            if headB in nodesA:
                return headB
            headB = headB.next

        return None

# 4) two pointers, swtich heads at end of linked list, so both traverse the same distances to reach a common node
# O(m+n) time complexity and O(1) space
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None: return None

        headA_copy, headB_copy = headA, headB

        while headA is not headB:
            headA = headB_copy if headA is None else headA.next
            headB = headA_copy if headB is None else headB.next

        return headA

# 5) further simplification of 4)
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        headA_copy, headB_copy = headA, headB;
        while headA != headB:
            headA = headA.next if headA else headB_copy;
            headB = headB.next if headB else headA_copy;
        return headA;

