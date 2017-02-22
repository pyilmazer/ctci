class Node:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next


class myStack:
    def __init__(self,top=None):
        self.top=top

    def push(self,item=0):
        node=Node(item)
        node.next=self.top
        self.top=node

    def pushNode(self,node):
        node.next = self.top
        self.top = node

    def pop(self):
        node = self.top
        if self.top:
            self.top=self.top.next
            node.next=None
        return node

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

    def __str__(self):
        strT=""
        node=self.top
        while node:
            strT+=str(node.value) + " "
            node=node.next
        return strT

if __name__ == '__main__':
    ms = myStack()
    if ms.isEmpty():
        print("empty")


    ms.push(5)
    ms.push(6)
    ms.push(1)

    print(ms)
    print(ms.peek())

    node = ms.pop()
    print("Popped:",node.value)
    node = ms.pop()
    print("Popped:",node.value)


    print(ms)

    ms.push(7)

    node = ms.pop()
    print("Popped:", node.value)
    node = ms.pop()
    print("Popped:", node.value)
    node = ms.pop()
    print("Popped:", node.value) if node else print(None)
