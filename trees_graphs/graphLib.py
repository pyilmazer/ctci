import sys
import random
from Queue import Queue

class Node:
   def __init__(self,id=-1,visited=False,children=[]):
       self.id=id
       self.visited=visited
       if not children:
           self.children=[]
       else:
           self.children=children

   def __str__(self):
       return str(self.id)


class Graph:
   def __init__(self,vertexIdList=None,edgeList=None):
       self.vertexIdList=vertexIdList
       self.edgeList=edgeList
       self.vertexList=[]

   def __str__(self):
       myStr=""
       for i in self.vertexList:
           myStr+= "Node id: " + str(i.id) +"\n"
           for j in i.children:
               myStr+="Children id: " + str(j.id) + "\n"
       myStr+= "-------------\n"
       return myStr 
       
  
   def addNode(self,nodeId,edgeList):
       index,node=self.getVertex(nodeId)
       if not node:
           print "Add new node!"
           self.vertexIdList.append(nodeId) 
           self.vertexList.append(Node(nodeId))
           indexFrom=len(self.vertexList)-1
       else:
           print "There is a node with same id!"
           indexFrom=index
      
       for i in edgeList:
           index,node=self.getVertex(i)
           if not node:
               self.vertexList.append(Node(i))
               self.vertexList[indexFrom].children.append(len(self.vertexList)-1)
           else:
               self.vertexList[indexFrom].children.append(node)
           self.edgeList.append((nodeId,i))    



   def createDirectedGraph(self):
       if not self.vertexIdList:
           return 

       for i in self.vertexIdList:
           self.vertexList.append(Node(i))
                
       for j in self.edgeList:
           index,vertex=self.getVertex(j[0])
           if vertex:
               index2,vertexTo=self.getVertex(j[1])
               self.vertexList[index].children.append(vertexTo)
              
           

   def getVertex(self,vid):
       for i in range(len(self.vertexList)):
           if self.vertexList[i].id == vid:
               return i,self.vertexList[i]
       return -1,None

       
   def depthFirstTraversal(self,root):
       if not root.children:
           sys.stdout.write(str(root.id) + " ")
           return
       else:
           index,node=self.getVertex(root.id)
           self.vertexList[index].visited=True
           sys.stdout.write(str(node.id) + " ")
           for i in root.children:
               index,node=self.getVertex(i.id)
               if not node.visited:
                   self.vertexList[index].visited=True
                   self.depthFirstTraversal(node)

  
   def breadthFirstTraversal(self,root):
       index,node=self.getVertex(root.id)
       if node:     
           queue=Queue()
           self.vertexList[index].visited=True
           queue.put(node)
           while not queue.empty():
               node=queue.get()
               sys.stdout.write(str(node.id) + " ")
               for i in node.children:
                   index,childNode=self.getVertex(i.id)
                   if not childNode.visited:
                       queue.put(childNode)    
                       self.vertexList[index].visited=True

 
   def setVisitedFalse(self):
       for i in self.vertexList:
           i.visited=False

