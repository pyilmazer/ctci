import stack
class QueueS:
    def __init__(self,stack1=None,stack2=None):
        self.stack1=stack1
        self.stack2=stack2

    def add(self,item):
        if not self.stack1 or not self.stack2:
            self.stack1=stack.myStack()
            self.stack2=stack.myStack()

        while not self.stack2.isEmpty():
            self.stack1.pushNode(self.stack2.pop())

        self.stack1.push(item)

        while not self.stack1.isEmpty():
            self.stack2.pushNode(self.stack1.pop())

    def remove(self):
        return self.stack2.pop()

    def peek(self):
        return self.stack2.peek()

    def getSize(self):
        node=self.stack2.top
        count=0
        while node:
            node=node.next
            count+=1
        return count

    def __str__(self):
        strP=""
        node=self.stack2.top
        while node:
            strP += str(node.value) + " "
            node=node.next
        return strP


class QueueS2:
    def __init__(self,stackNewest=None,stackOldest=None):
        self.stackNewest=stackNewest
        self.stackOldest=stackOldest

    def add(self,item):
        if not self.stackNewest or not self.stackOldest:
            self.stackNewest=stack.myStack()
            self.stackOldest=stack.myStack()

        self.stackNewest.push(item)

    def peek(self):
        self.shiftElements()
        return self.stackOldest.peek()

    def remove(self):
        self.shiftElements()
        return self.stackOldest.pop()

    def shiftElements(self):
        if self.stackOldest.isEmpty():
            while(not self.stackNewest.isEmpty()):
                self.stackOldest.pushNode(self.stackNewest.pop())


    def __str__(self):
        strP="\nOldest:"
        node=self.stackOldest.top
        while node:
            strP += str(node.value) + " "
            node=node.next

        strP += "\nNewest:"
        node = self.stackNewest.top
        while node:
            strP += str(node.value) + " "
            node = node.next
        return strP


if __name__ == "__main__":
    queueS = QueueS2()
    queueS.add(1)
    queueS.add(2)
    queueS.add(3)
    queueS.add(4)

    print(queueS)

    print("Removed",queueS.remove().value)
    print("Removed",queueS.remove().value)
    queueS.add(13)
    queueS.add(14)

    print(queueS)

    print("Removed",queueS.remove().value)
    print("Removed",queueS.remove().value)

    print(queueS)


    print("Removed",queueS.remove().value)
    print("Removed",queueS.remove().value)

    print(queueS)




