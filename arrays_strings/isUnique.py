## with additional data structure
import math


def isUnique(myInput):  #with hashmap
    myDict = {}
    for i in myInput:
        if (i in myDict and myDict[i] == 1):
            return False
        else:
            myDict[i] = 1
    return True


def isUnique2(myInput):   #without hashmap
    for i in range(len(myInput)):
        for j in range(i + 1, len(myInput)):
            if myInput[i] == myInput[j]:
                return False
    return True




if __name__ == '__main__':
     myInput = input()
     myInput2 = input()

     if (isUnique(myInput)):
        print("Input1 is Unique")
     else:
        print('Input1 is Not Unique')

     if (isUnique2(myInput2)):
        print("Input2 is Unique")
     else:
        print('Input2 is Not Unique')
