import random
import math


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

   def getLength(self,list1):
       node=list1
       count=1
       while node.next:
            count+=1
            node=node.next
       return count,node

   def goToNode(self,list1,count):
       node=list1
       for i in range(count):
           if node:
               node=node.next
       return node
 
   def detectIntersection(self,listB,listS,sizeDiff):
       node=listB
       node2=listS
       
       nodeT=self.goToNode(node,sizeDiff)
       
       while nodeT.next and node2.next:
           if nodeT.next == node2.next:
               break
           nodeT=nodeT.next
           node2=node2.next
       
       while nodeT.next:
           nodeTemp=Node(nodeT.next.value)
           node2.next=nodeTemp
           node2=node2.next
           nodeT=nodeT.next
       
       node2.next=None       

       return listB,listS
               
       

   def isThereIntersection(self,list1,list2):
       if not list1 or not list2:
           print "No intersection"
           return None,None 
       count1,nodeL1=self.getLength(list1)
       count2,nodeL2=self.getLength(list2)
       if nodeL1 == nodeL2:
           print "There is an intersection,find it!"
           sizeDiff=count1-count2
           if sizeDiff < 0:
               return self.detectIntersection(list2,list1,-sizeDiff)
           elif sizeDiff > 0:
               return self.detectIntersection(list1,list2,sizeDiff)
           else:
               return self.detectIntersection(list1,list2,0)
       else:
           print "No intersection"
           return list1,list2

   def printList(self,myList):
       node = myList
       p=""
       while node:
           p += str(node.value) + " "
           node=node.next
       print(p)
   
if __name__ == '__main__':
   list = List()
   
   #list.isPalindrome()

   a = Node(1)
   a.next=Node(2)
   a.next.next=Node(3)
   a.next.next.next=Node(4)
   a.next.next.next.next=Node(5)
   a.next.next.next.next.next=Node(6)


   b = Node(7)
   b.next=Node(8)
   #b.next.next=a.next.next.next
   b.next.next=Node(10)
   b.next.next.next=Node(11)
  # b.next.next.next.next=a.next
   b.next.next.next.next=None

   list.printList(a)
   list.printList(b)
   print "--------------"

   ret1,ret2=list.isThereIntersection(a,b)
   list.printList(ret1)
   list.printList(ret2)

   ret3,ret4=list.isThereIntersection(None,None)
   print ret3
