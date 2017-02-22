import stack

def sortStack(unsorted):
   sorted=stack.myStack()
   if not unsorted or unsorted.isEmpty():
       return sorted
   while not unsorted.isEmpty():
       currNode=unsorted.pop()
       if sorted.isEmpty() or currNode.value <= sorted.peek():
           sorted.pushNode(currNode)
       else:
           count=0
           while not sorted.isEmpty() and sorted.peek() < currNode.value:
               unsorted.pushNode(sorted.pop())
               count+=1
           sorted.pushNode(currNode)
           for i in range(count):
               sorted.pushNode(unsorted.pop())

   return sorted


if __name__ == "__main__":
   mystack=stack.myStack()
   mystack.push(4)
   mystack.push(7)
   mystack.push(1)
   mystack.push(2)
   mystack.push(6)
   mystack.push(10)
   mystack.push(3)


   mysorted=sortStack(mystack)

   mystr=""
   while not mysorted.isEmpty():
       mystr+=str(mysorted.pop().value) + " "
  
   print(mystr)

              
