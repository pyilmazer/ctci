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

   def kthElementFromLast(self,k):
       node=self.head
       node2=node
       count=0
       #if k<size of the list, return first element
       while node and node2.next:
           if count<k-1:
               node2=node2.next
               count+=1
           else:
               node2=node2.next
               node=node.next
       return node    

   def removeMiddle(self):
       node=self.head
       node2=node
       count=0
       while node2.next:
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
               nodeTail.next=node
               node.next=None
               nodeTail=nodeTail.next
           node=nodeT
       nodeTail.next=None
       self.head=nodeHead

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
   list1 = List()
   value=random.randint(0,10)
   print value
   list1.createList(value)
   print "List:"
   list1.printList()

   value=random.randint(0,value)
   print "k:",value
   node3=list1.kthElementFromLast(value)
   print node3.value if node3 else None

