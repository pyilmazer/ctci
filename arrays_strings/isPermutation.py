
def isPermutation(str1, str2):
    myDict = {}
    for i in str2:
        if i in myDict:
            myDict[i] += 1
        else:
            myDict[i] = 1
    for i in str1:
        if not i in myDict:
            return False
        else:
            if myDict[i] == 0:
                return False
            else:
                myDict[i] -= 1
    return True


if __name__ == '__main__':
     myInput = input()
     myInput2 = input()


     if (isPermutation(myInput,myInput2)):
        print("Permutation")
     else:
        print('Not Permutation')