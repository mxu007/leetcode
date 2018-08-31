# Implement the following operations of a stack using queues.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Example:

# MyStack stack = new MyStack();

# stack.push(1);
# stack.push(2);
# stack.top();   // returns 2
# stack.pop();   // returns 2
# stack.empty(); // returns false
# Notes:

# You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

# https://leetcode.com/problems/implement-stack-using-queues/description/

# https://www.geeksforgeeks.org/implement-stack-using-queue/
# 1) making pop operation costly
from queue import Queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = Queue()


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.items.put(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        q2 = Queue()
        while(self.items.qsize() >1):
            q2.put(self.items.get())
        result = self.items.get()
        self.items = q2
        return result


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        q2 = Queue()
        while(self.items.qsize() >1):
            q2.put(self.items.get())
        result = self.items.get()
        q2.put(result)
        self.items = q2
        return result


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.items.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# 2) # 1) making push operation costly
from queue import Queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = Queue()
        print("init")


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        q2 = Queue()
        q2.put(x)
        while(not self.items.empty()):
            q2.put(self.items.get())
        print("q2",q2.qsize())
        self.items = q2
        print("q1",self.items.qsize())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.items.get()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        result = self.items.get()
        q2 = Queue()
        q2.put(result)
        while(not self.items.empty()):
            print(self.items.qsize())
            q2.put(self.items.get())
        self.items = q2
        return result


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.items.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

