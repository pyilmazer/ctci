#################### isPermutationPalindrome

def isPermutationPalindrome(input):
    myDict = {}
    for i in input:
        if i in myDict:
            myDict[i] += 1
        else:
            myDict[i] = 1

    count = 0
    for i in myDict.keys():
        count += myDict[i]

    ##### This case is actually not needed.
    ## We will check oddNumber of characters in else case.
    if count % 2 == 0:
        for i in myDict.keys():
            if myDict[i] % 2 == 1:
                return False
        return True
    else:
        countOdd = 0
        for i in myDict.keys():
            if myDict[i] % 2 == 1:
                if countOdd == 1:
                    return False
                countOdd += 1
        return True



if __name__ == '__main__':

    if isPermutationPalindrome(""):
        print('Polindrome')
    else:
        print('Not Polindrome')

    if isPermutationPalindrome("tactcao"):
        print('Polindrome')
    else:
        print('Not Polindrome')