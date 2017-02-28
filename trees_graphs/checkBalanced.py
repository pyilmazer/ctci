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

def checkBalanced(tree):
   if not tree:
       return -1
   heightL=checkBalanced(tree.left)
   heightR=checkBalanced(tree.right)
   #print tree,heightL,heightR
   if heightL == sys.maxint or heightR == sys.maxint:
       return sys.maxint
   if math.fabs(heightL-heightR) > 1:
       return sys.maxint
   return max(heightL,heightR)+1

def checkBalancedFunc(tree):
   height=checkBalanced(tree) 
   if height == sys.maxint:
       print "Not Balanced"
   else:
       print "Balanced, height:",height

       
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

   checkBalancedFunc(bt.node)
   checkBalancedFunc(bt2.node)
   checkBalancedFunc(bt3.node)
   checkBalancedFunc(bt4.node)
