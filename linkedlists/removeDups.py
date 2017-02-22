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

   def removeDup(self):
       dict = self.findDup()
       node=self.head
       while node and node.next:
           if dict[node.next.value] > 1:
               dict[node.next.value]-=1
               delNode = node.next
               node.next = node.next.next
               delNode.next = None
           else:
               node = node.next


   def findDup(self):
       dict={}
       node=self.head
       while node:
           if node.value in dict:
               dict[node.value] += 1
           else:
               dict[node.value] = 1
           node=node.next
       return dict

   def removeDupNoHashMap(self):
       node=self.head
       node2=node
       while node:
           while node2.next:
               if node2.next.value == node.value:
                   nodeT=node2.next
                   node2.next=node2.next.next
                   nodeT.next=None
               else:
                   node2=node2.next
           node=node.next
           node2=node

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
   print "List1, Original:"
   list2 = list1.createList(value)
   list1.printList()

   print "List1, Removed Dups"
   list1.removeDup()
   #list.removeDupNoHashMap()
   list1.printList()

   print "List2, Original:"
   list3 = list1.createList(value)
   list1.printList()

   print "List2, Removed Dups No HashMap"
   list1.removeDupNoHashMap()
   list1.printList()

