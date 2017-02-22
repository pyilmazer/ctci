import stack
import sys

class nodeWithMin(stack.Node):
   ### in python 2.0 sys.maxint in python 3.0 sys.maxsize
   def __init__(self,value=0,minValue=sys.maxsize):
       stack.Node.__init__(self,value)
       self.minValue=minValue


class myStackWithMin(stack.myStack):
   def __init__(self,top=None):
       stack.myStack.__init__(self,top)

   def getPeakMin(self):
       if self.top:
           return self.top.minValue
       else:
           return sys.maxsize

   def push(self,item):
       node=nodeWithMin(item)
       node.minValue=self.getPeakMin() if node.value >= self.getPeakMin() else node.value
       node.next=self.top
       self.top=node

   def getMin(self):
       if self.top:
           return self.top.minValue
       else:
           return sys.maxsize


class myStackWithMin2(stack.myStack):
   def __init__(self, top=None, minStack=None):
       self.minStack=minStack
       stack.myStack.__init__(self, top)

   def push(self,item):
       stack.myStack.push(self,item)
       if not self.minStack:
           self.minStack=stack.myStack()
           self.minStack.push(item)
       else:
           if item < self.minStack.peek():
               self.minStack.push(item)

   def pop(self):
       node=stack.myStack.pop(self)
       if node.value == self.minStack.peek():
           self.minStack.pop()

   def getMin(self):
       if self.minStack:
           return self.minStack.peek()
       else:
           return sys.maxsize




if __name__ == '__main__':
   #ms = myStackWithMin()
   ms = myStackWithMin2()

   ms.push(4)

   print("actual stack",ms)
   print("min stack",ms.minStack)
   print(ms.getMin())

   ms.push(5)

   print("actual stack", ms)
   print("min stack", ms.minStack)
   print(ms.getMin())

   ms.push(2)

   print("actual stack", ms)
   print("min stack", ms.minStack)
   print(ms.getMin())

   ms.push(1)

   print("actual stack", ms)
   print("min stack", ms.minStack)
   print(ms.getMin())

   ms.pop()

   print("actual stack", ms)
   print("min stack", ms.minStack)
   print(ms.getMin())

   ms.pop()

   print("actual stack", ms)
   print("min stack", ms.minStack)
   print(ms.getMin())

   ms.pop()

   print("actual stack", ms)
   print("min stack", ms.minStack)
   print(ms.getMin())

   ms.pop()

   print("actual stack", ms)
   print("min stack", ms.minStack)
   print(ms.getMin())

