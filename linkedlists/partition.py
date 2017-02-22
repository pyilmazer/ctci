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


   def partition(self,partition):
       node=self.head
       nodeHead=nodeTail=node
       while node:
           nodeT=node.next
           if node.value < partition:
               if node!=nodeHead:                  
                   node.next=nodeHead
                   nodeHead=node
           else:
               if node!=nodeTail:
                   nodeTail.next=node
                   node.next=None
                   nodeTail=nodeTail.next
           node=nodeT
       nodeTail.next=None
       self.head=nodeHead

   
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
   
   print "List:"
   list1.createList(value)
   list1.printList()
   
   print "Partitioned:"
   value=random.randint(0,10)
   print "Partitioned wrt:",value
   list1.partition(value)
   list1.printList()

