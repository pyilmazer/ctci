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


def createMinBST(sortedList):
   if not sortedList:
       return None
   if len(sortedList) == 1:
       return BinaryNode(sortedList[0])

   indexMin=(len(sortedList)-1)/2
   node=BinaryNode(sortedList[indexMin])
   
   node.right=createMinBST(sortedList[:indexMin])
   node.left=createMinBST(sortedList[indexMin+1:])
   return node


def inOrder(nodePtr):
   if nodePtr:
       sys.stdout.write(str(nodePtr.id)+" ")
       inOrder(nodePtr.right)
       inOrder(nodePtr.left)

if __name__ == '__main__':

   #vertexIdList=[1,2,3,4,5,6,7,8,9,10]
   #vertexIdList=[1,2]
   #vertexIdList=[1]
   #vertexIdList=[]
   vertexIdList=[1,2,3]
   node=createMinBST(vertexIdList)

   inOrder(node)
 
