import sys
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



def listOfDepths(tree):
   listOfDepths=[]
   if not tree or not tree.node:
       return listOfDepths
  
   levelNodes=[] 
   levelNodes.append(tree.node)
   while levelNodes:
       listOfDepths.append(levelNodes)
       levelNodes2=[]
       for i in levelNodes:
           levelNodes2+= [i.left] if i.left else []
           levelNodes2+= [i.right] if i.right  else []
       levelNodes=levelNodes2

   return listOfDepths
       
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
   bt.createBinaryTree(7)   
 

   print "inorder traversal"
   print bt.inOrder(bt.node)

   print "preorder traversal"
   print bt.preOrder(bt.node)

   print "level by level print"
   listOfD=listOfDepths(bt)
   printList(listOfD)
 
