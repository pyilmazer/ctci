import random


class Node:
   def __init__(self,value=None,next=None):
       self.value = value
       self.next = next

   def __str__(self):
       return str(self.value)

class List:
   def __init__(self,head=None,curr=None):
       self.head=head
       self.curr=curr

   def createList(self,num):
       self.head=None
       if num > 0:
           curr=Node(8)
           self.head=curr
       else:
           return self.head

       for i in range(1,num):
           value = random.randint(5,9)
           nodeT = Node(value)
           curr.next = nodeT
           curr = nodeT
       return self.head

   def isCycleExist(self,list1):
       nodeFast=nodeSlow=list1
       if not nodeFast or not nodeFast.next:
          return False
       while nodeFast and nodeFast.next:
          nodeSlow=nodeSlow.next
          nodeFast=nodeFast.next.next
          if nodeSlow == nodeFast:
               return True
       return False

   def cyclePoint(self,list1):
       nodeFast=nodeSlow=list1
       if not nodeFast or not nodeFast.next:
          return None
       while nodeFast and nodeFast.next:
          nodeSlow=nodeSlow.next
          nodeFast=nodeFast.next.next
          if nodeSlow == nodeFast:
               break
       if not nodeFast.next:
          return None

       nodeSlow=list1
       while nodeSlow!=nodeFast:
           nodeSlow=nodeSlow.next
           nodeFast=nodeFast.next
       return nodeSlow

   def printList(self,myList):
       node = myList
       p=""
       while node:
           p += str(node.value) + " "
           node=node.next
       print(p)
   

if __name__ == '__main__':
   list = List()
   
   value=random.randint(1,5)
   print value
   
   list1 = list.createList(value)
   list.printList(list1)



   a = Node(1)
   a.next=Node(2)
   a.next.next=Node(3)
   a.next.next.next=Node(4)
   a.next.next.next.next=Node(5)
   a.next.next.next.next.next=a.next.next
   #a.next.next.next.next.next=Node(1)


   if list.isCycleExist(a):
        print "exist"
   else:
        print "not exist"
   print list.cyclePoint(a)
