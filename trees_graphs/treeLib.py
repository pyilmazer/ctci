import sys
import random

class Node:
   def __init__(self,id=-1,visited=False,children=[]):
       self.id=id
       self.visited=visited
       self.children=children

class BinaryNode:
   def __init__(self,id,visited=False,left=None,right=None):
       if not id:
           id = -1
       self.id=id
       self.visited=visited
       self.left=left
       self.right=right

   def __str__(self):
       return str(self.id)


class Tree:
   def __init__(self,node=None):
       self.node=node

class BinaryTree:
   def __init__(self,node=None):
       self.node=node

   def add(self,nodeId):
       print "added",nodeId
       self.addNode(self.node,nodeId)
  
   def addNode(self,nodePtr,nodeId):
       if not nodePtr:
           self.node = BinaryNode(nodeId)
       else:
           if nodeId<=nodePtr.id:
               if not nodePtr.left:
                   nodePtr.left=BinaryNode(nodeId)
               else:
                   self.addNode(nodePtr.left,nodeId)
           else:
               if not nodePtr.right:
                   nodePtr.right=BinaryNode(nodeId)
               else:
                   self.addNode(nodePtr.right,nodeId)
   


   def inOrder(self,nodePtr):
       if not nodePtr:
          return ""
          
       a=self.inOrder(nodePtr.left)
       b=str(nodePtr.id)
       c=self.inOrder(nodePtr.right)
       return a+" "+b+" "+c

   def inOrderP(self,nodePtr):
       if nodePtr:
           self.inOrderP(nodePtr.left)
           sys.stdout.write(str(nodePtr.id))
           sys.stdout.write(" ")
           self.inOrderP(nodePtr.right)


   def preOrder(self,nodePtr):
       if nodePtr:
           sys.stdout.write(str(nodePtr.id))
           sys.stdout.write(" ")
           self.preOrder(nodePtr.left)
           self.preOrder(nodePtr.right)


   def postOrder(self,nodePtr):
       if nodePtr:
           self.postOrder(nodePtr.left)
           self.postOrder(nodePtr.right)
           sys.stdout.write(str(nodePtr.id))
           sys.stdout.write(" ")


   def createBinaryTree(self,nodeCount):
       for i in range(nodeCount):
           value=random.randint(1,50)
           self.add(value)

   def createBinaryTree2(self,list1):
       for i in list1:
           self.add(i)
 
