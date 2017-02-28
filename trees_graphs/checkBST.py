import sys
import math
import treeLib

          
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

def checkBST(tree):

   if tree.left:
       if tree.id >= tree.left.id:
           leftAction,maxId,minId=checkBST(tree.left)
       else:
           return False
   else:
       return True

   if tree.right:
       if tree.id < tree.right.id:
           rightAction,maxId,minId=checkBST(tree.right)
       else:
           return False
   else:
       return True
 
   return leftAction and rightAction 
   

def checkBSTFunc(tree):
   if checkBST(tree):
       print "BST"
   else:
       print "Not BST"

def checkBSTWithInorder(tree):
   global lastVal
   if tree:
       if not checkBSTWithInorder(tree.left):
          return False
       if lastVal and lastVal >= tree.id:
          return False
       lastVal=tree.id
       if not checkBSTWithInorder(tree.right):
           return False
       return True
   else:
       return True

def printList(myList):
   for i in myList:
       for j in i :
           sys.stdout.write(str(j.id) + " ")
       print ""
   print ""   


def printA(list1):
   for i in list1:
       sys.stdout.write(str(i.id) + " ")
   print ""
if __name__ == '__main__':

   bt=treeLib.BinaryTree()
   bt.createBinaryTree(10)   
   
   print "inorder traversal"
   print bt.inOrder(bt.node)

   print "preorder traversal"
   bt.preOrder(bt.node)

 
   bt2=treeLib.BinaryTree()
   bt2.createBinaryTree2([10,8,6,7,9,4,3,18,15,20])
   print "inorder traversal"
   print bt2.inOrder(bt2.node)

   print "preorder traversal"
   bt2.preOrder(bt2.node)


   bt3=treeLib.BinaryTree()
   bt3.createBinaryTree2([20,10,5,3,15,30,25,40])
   print "inorder traversal"
   print bt3.inOrder(bt3.node)

   print "preorder traversal"
   bt3.preOrder(bt3.node)


   bt4=treeLib.BinaryTree()
   bt4.createBinaryTree2([20,10,5])
   print "inorder traversal"
   print bt4.inOrder(bt4.node)

   print "preorder traversal"
   bt4.preOrder(bt4.node)

   print ""
   node=treeLib.BinaryNode(20)
   node.left=treeLib.BinaryNode(10)
   node.right=treeLib.BinaryNode(30)
   node.left.left=treeLib.BinaryNode(5)
   node.left.right=treeLib.BinaryNode(25)
   node.left.left.left=treeLib.BinaryNode(3)
   node.right.right=treeLib.BinaryNode(40)
   node.right.left=treeLib.BinaryNode(26)

   #checkBSTFunc(bt.node)
   #checkBSTFunc(bt2.node)
   #checkBSTFunc(bt3.node)
   #checkBSTFunc(bt4.node)
   #checkBSTFunc(node)


   lastVal=None
   if checkBSTWithInorder(node):
      print "BST"
   else:
      print "Not BST"
