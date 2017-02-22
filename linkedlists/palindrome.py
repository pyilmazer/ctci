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


   def isPalindrome(self):
       node=self.head
       reversedList=None
       count=0
       while node:
           nodeT=Node(node.value)
           nodeT.next=reversedList
           reversedList=nodeT
           node=node.next
           count+=1

       self.printList(reversedList)
       if self.compare(count,reversedList):
           print "Palindrome"
       else:
           print "Not Palindrome"                      
       print reversedList

   def compare(self,halfsize,reversedList):
       node=self.head
       node2=reversedList
       for i in range(halfsize):
           if node and node2:
               if node.value != node2.value:
                   return False
           node=node.next
           ndoe2=node2.next
       return True

   def isPalindromeWithStack(self):
       nodeFast=nodeSlow=self.head
       stack=[]
       count=0

       if not nodeSlow:
          return "Not Palindrome"

       stack.append(nodeSlow.value)
       while nodeFast:
           if count%2 == 0 and count != 0:
               nodeSlow=nodeSlow.next
               stack.append(nodeSlow.value)
           count+=1
           nodeFast=nodeFast.next
       
       if count%2 == 1:
           stack.pop()
       nodeSlow=nodeSlow.next
       
       while stack and nodeSlow:
           if stack.pop() != nodeSlow.value:
               return "Not Palindrome"
           nodeSlow=nodeSlow.next
       return "Palindrome"        
           

   def printList(self,myList):
       node = myList
       p=""
       while node:
           p += str(node.value) + " "
           node=node.next
       print(p)
   
   def getLength(self,listA):
       count=0
       node=listA
       while node:
           count+=1
           node=node.next
       return count

if __name__ == '__main__':
   list = List()
   
   value=random.randint(1,5)
   print value
   
   list1 = list.createList(value)
   list.printList(list1)


   #list.isPalindrome()

   a = Node(1)
   a.next=Node(2)
   a.next.next=Node(3)
   a.next.next.next=Node(2)
   a.next.next.next.next=Node(1)
   #a.next.next.next.next.next=Node(1)


   list.head=a
   #list.isPalindrome()
   print list.isPalindromeWithStack()
