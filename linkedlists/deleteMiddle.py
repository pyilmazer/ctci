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
       if num > 0 :
           curr=Node(1)
           self.head=curr
       else:
           return self.head

       for i in range(1,num):
           value = random.randint(0,9)
           nodeT = Node(value)
           curr.next = nodeT
           curr = nodeT

       return self.head

   def removeMiddle(self):
       node=self.head
       node2=node
       count=0
       while node2 and node2.next:
           count+=1
           if count>2 and count%2 == 0:
               node=node.next
           node2=node2.next
   
       if count>=2:
           nodeT=node.next
           node.next=node.next.next
           nodeT.next=None
   
   def removeGivenMiddle(self,node):
       if node is None or node.next is None:
          return False
       node2=node.next
       node.value=node2.value
       node.next=node2.next
       node2.next=None
       return True   
   
   def printList(self):
       node = self.head
       p=""
       while node:
           p += str(node.value) + " "
           node=node.next
       print(p)

if __name__ == '__main__':

   list1 = List()
   value=random.randint(0,10)
   print value
   
   print("List1:")
   list1.createList(value)
   list1.printList()
   
   print "remove middle"
   list1.removeMiddle()
   list1.printList()

   #print "remove given middle"
   #list.removeGivenMiddle()
   #list.printList()
   
