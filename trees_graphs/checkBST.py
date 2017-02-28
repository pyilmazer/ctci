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

def checkBST(tree,min=None,max=None):

   if not tree:
       return True

   if (min and tree.id < min) or (max and tree.id > max):
       return False

   return checkBST(tree.left,min,tree.id) and checkBST(tree.right,tree.id,max)


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


def checkBSTFunc(tree,mystr):
   print("Check BST "+mystr)
   if checkBST(tree):
       print("\tBST")
   else:
       print("\tNot BST")


def checkBSTWithInorderFunc(tree,mystr):
   print("Check BST With Inorder "+mystr)
   if checkBSTWithInorder(tree):
       print("\tBST")
   else:
       print("\tNot BST")


if __name__ == '__main__':

   bt=treeLib.BinaryTree()
   bt.createBinaryTree(10)   

   node=treeLib.BinaryNode(20)
   node.left=treeLib.BinaryNode(10)
   node.right=treeLib.BinaryNode(30)
   node.left.left=treeLib.BinaryNode(5)
   node.left.right=treeLib.BinaryNode(25)
   node.left.left.left=treeLib.BinaryNode(3)
   node.right.right=treeLib.BinaryNode(40)
   node.right.left=treeLib.BinaryNode(26)

   node2 = treeLib.BinaryNode(10)
   node2.left = treeLib.BinaryNode(5)
   node2.right = treeLib.BinaryNode(15)
   node2.left.left = treeLib.BinaryNode(4)
   node2.left.right = treeLib.BinaryNode(6)

   node3 = treeLib.BinaryNode(6)
   node3.left = treeLib.BinaryNode(5)
   node3.right = treeLib.BinaryNode(7)
   node3.left.left = treeLib.BinaryNode(4)
   node3.left.left.left = treeLib.BinaryNode(3)
   node3.left.left.left.right = treeLib.BinaryNode(9)


   checkBSTFunc(node,"node1")
   lastVal=None
   checkBSTWithInorderFunc(node,"node1")
   checkBSTFunc(node2,"node2")
   lastVal=None
   checkBSTWithInorderFunc(node2,"node2")
   checkBSTFunc(node3,"node3")
   lastVal=None
   checkBSTWithInorderFunc(node3,"node3")
