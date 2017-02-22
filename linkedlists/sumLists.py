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


   def sumLists(self,list1,list2):
       nodeH1=list1
       nodeH2=list2
       str1=str2=""
       while nodeH1:
           str1+=str(nodeH1.value)
           nodeH1=nodeH1.next

       while nodeH2:
           str2+=str(nodeH2.value)
           nodeH2=nodeH2.next

       print str1,str2
       print int(str1)+int(str2)
           
   
   def printList(self):
       node = self.head
       p=""
       while node:
           p += str(node.value) + " "
           node=node.next
       print(p)

if __name__ == '__main__':
   list = List()
   
   value=random.randint(0,5)
   print value
   list1 = list.createList(value)

   list.printList()

   list2 = list.createList(value)

   list.printList()

   list.sumLists(list1,list2)
