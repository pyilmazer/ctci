class Node:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next

class myStackP:
    def __init__(self,top=None,bottom=None):
        self.top=top
        self.bottom=bottom

    def push(self,item=0):
        node=Node(item)
        node.next=self.top
        self.top=node

        if not self.top.next:
            self.bottom=self.top

    def pushNode(self,node):
        node.next=self.top
        self.top=node
        if self.top.next is None:
            self.bottom=self.top

    def pop(self):
        node = self.top
        if self.top:
            self.top=self.top.next
            node.next=None
        return node

    def popFromBottom(self):
        node=self.top
        if node==self.bottom:
            self.top=self.bottom=None
            return node
        while node.next.next:
            node=node.next
        bottomNode=node.next
        self.bottom=node
        self.bottom.next=None
        return bottomNode

    def peek(self):
        if self.top:
            return self.top.value
        else:
            return None

    def isEmpty(self):
        if not self.top:
            return True
        else:
            return False

class stackPlates:
    def __init__(self,stackList=[],threshold=3):
        self.stackList=stackList
        self.threshold=threshold

    def push(self,item):
        if not self.stackList or self.isListFull():
            myStack=myStackP()
            myStack.push(item)
            self.stackList.append(myStack)
        else:
            myStack=self.stackList[self.getListSize()-1]
            myStack.push(item)

    def pop(self):
        if self.getListSize() == 0:
            return None
        else:
            myStack=self.stackList[self.getListSize()-1]
            node=myStack.pop()
            if myStack.isEmpty():
                self.stackList.pop()
            return node

    def peek(self):
        if self.getListSize() == 0:
            return None
        else:
            myStack=self.stackList[self.getListSize()-1]
            node=myStack.peek()
            return node.value

    def popAt(self,index):
        if index>=self.getListSize():
            return None
        stackT=self.stackList[index]
        node=stackT.pop()
        if index < self.getListSize()-1:
            self.shift(index)
        return node

    def shift(self,index):
        for i in range(index+1,self.getListSize()):
            stackT=self.stackList[i-1]
            stackN=self.stackList[i]
            while not self.isStackFull(stackT):
                poppedNode=stackN.popFromBottom()
                if not poppedNode:
                    break
                stackT.pushNode(poppedNode)
        if self.stackList[self.getListSize()-1].isEmpty():
            self.stackList.pop()

    def isListFull(self):
        for i in self.stackList:
            if not self.isStackFull(i):
                return False
        return True

    def isStackFull(self,stackT):
        count=self.getLengthOfStack(stackT)
        if count == self.threshold:
            return True
        return False

    def getLengthOfStack(self,stackT):
        count = 0
        node=stackT.top
        while node:
            count += 1
            node = node.next
        return count

    def getListSize(self):
        return len(self.stackList)

    def __str__(self):
        strT=""
        for i in self.stackList:
            strT+="\n---List---\n"
            node=i.top
            while node:
                strT+=" "+str(node.value)
                node=node.next
        return strT



if __name__ == "__main__":
    stackP=stackPlates()
    stackP.push(10)
    stackP.push(2)
    stackP.push(5)
    stackP.push(9)
    stackP.push(1)
    stackP.push(3)
    stackP.push(0)
    print(stackP)
    stackP.pop()
    print(stackP)
    stackP.pop()
    print(stackP)
    stackP.pop()
    print(stackP)
    stackP.pop()
    stackP.push(13)
    stackP.push(20)
    print(stackP)

    node=stackP.popAt(0)
    print(stackP)

    node = stackP.popAt(0)
    print(stackP)

    node = stackP.popAt(0)
    print(stackP)

    stackP.push(89)
    stackP.push(90)
    stackP.push(91)
    stackP.push(92)

    node = stackP.popAt(1)
    print(stackP)









