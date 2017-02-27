import sys
#sys.path.insert(0,path)

import graphLib 


def isThereRoute(graph,node1,node2):

   graph.setVisitedFalse()
   
   nodeList=[]
   indexFrom,nodeFrom=graph.getVertex(node1.id)
   indexTo,nodeTo=graph.getVertex(node2.id)
   if not nodeFrom or not nodeTo:
       print "there is no such nodes"
   nodeFrom.visited=True
   nodeList.append(nodeFrom)
   while nodeList:
       node=nodeList.pop(0)
       print "popped:",node
       if node == nodeTo:
           return True
       for i in node.children:
           index,nodeC=graph.getVertex(i.id)
           if not nodeC.visited:
               nodeC.visited=True
               nodeList.append(nodeC)
   return False
           
           


if __name__ == '__main__':

   vertexIdList=[1,2,3,4,5,6,7,8,9]
   edgeList=[(1,2),(1,3),(2,3),(3,4),(2,5),(2,6),(6,7),(4,7),(7,8),(9,1),(8,4),(8,5)]
   myG=graphLib.Graph(vertexIdList,edgeList)
   myG.createDirectedGraph()

   print myG
  
   if isThereRoute(myG,myG.vertexList[7],myG.vertexList[4]):
       print "yes there is"
   else:
       print "node there is not"
 
