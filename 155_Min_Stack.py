# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

# https://leetcode.com/problems/min-stack/description/

# 1) use a list and separate variable to store min
# https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
# the trick is 2x - minEle and minEle - y
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.minEle = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.items) == 0:
            self.items.append(x)
            self.minEle = x
        else:
            if x < self.minEle:
                self.items.append(2*x-self.minEle)
                self.minEle = x
            else: self.items.append(x)


    def pop(self):
        """
        :rtype: void
        """
        if self.items[-1] >= self.minEle:
            return_val = self.items[-1]
        else:
            return_val = self.minEle
            self.minEle = 2*self.minEle - self.items[-1]
        self.items = self.items[:-1]
        return return_val

    def top(self):
        """
        :rtype: int
        """
        if self.items[-1] >= self.minEle:
            return self.items[-1]
        else:
            return self.minEle


    def getMin(self):
        """
        :rtype: int
        """
        return self.minEle



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



# 2) use tuple to store current data and current min
class MinStack:

    def __init__(self):
        self.q = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin));

    # @return nothing
    def pop(self):
        self.q.pop()


    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]


    # @return an integer
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]


# 3) stack and min
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack= []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.stack: self.stack.append((x,x))
        else:
           self.stack.append((x,min(x,self.stack[-1][1])))

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack: self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack: return self.stack[-1][0]
        else: return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack: return self.stack[-1][1]
        else: return None
