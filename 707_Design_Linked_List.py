# Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement these functions in your linked list class:

# get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
# Example:

# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3
# Note:

# All values will be in the range of [1, 1000].
# The number of operations will be in the range of [1, 1000].
# Please do not use the built-in LinkedList library.

# https://leetcode.com/problems/design-linked-list/description/

# 1) add additional class "ListNode"

# class for node
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # init the head
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        head = self.head
        # move to the target index node
        for i in range(index):
            if head:
                head = head.next
            # exhaust the node directly break the loop
            else:
                break
        # return target node value if it is not None, otherwise returns -1
        return head.val if head else -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        # if head is None, directly set this new node to be head
        if not self.head:
            self.head = ListNode(val=val, next=None)
        # otherwise use temp to store original head, set new node to be head, and link new head to old head
        else:
            temp = self.head
            self.head = ListNode(val=val, next=temp)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        # if head is None, addAtTail is same as addAtHead
        if not self.head:
            self.head = ListNode(val=val, next=None)

        else:
            head = self.head
            # move pointer to the last element of linked list
            while head.next:
                head = head.next
            head.next = ListNode(val=val, next=None)


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        # if index is zero, same as addAtHead
        if index == 0: return self.addAtHead(val)

        head = self.head
        # only move pointer if head is not None
        if head:
            # move to the index-1 node
            for i in range(index-1):
                if head.next:
                    head = head.next
                else:
                    return
            # create temp and link to the original node at index
            temp = ListNode(val=val, next=head.next)
            # link node index-1 to this new node at index
            head.next = temp


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        head = self.head
        # move pointer if head is not None
        if head:
            if index == 0:
                self.head = self.head.next
            # move to the index-1 node
            else:
                for i in range(index-1):
                    if head.next:
                        head = head.next
                    else:
                        return
                # delete only if head.next is not None
                if head.next:
                    head.next = head.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
