
def countSpace(charArr, length):
    count = 0
    for i in range(length):
        if charArr[i] == ' ':
            count += 1
    return count


def urlify(charArr, length):
    spaceCount = countSpace(charArr, length)
    newEnd = length + spaceCount * 2
    for i in range(length - 1, -1, -1):
        if charArr[i] == ' ':
            charArr[newEnd - 3] = '%'
            charArr[newEnd - 2] = '2'
            charArr[newEnd - 1] = '0'
            newEnd -= 3
        else:
            charArr[newEnd - 1] = charArr[i]
            newEnd -= 1
    print(charArr)



if __name__ == '__main__':

     urlify(['M','r',' ','J','o','h','n',' ','S','m','i','t','h','','','',''],13)
     urlify(['M','r',' ','h','a',' ',' ','J','o','h','n',' ','S','m','i','t','h','','','','','','','',''],17)
     urlify([],0)
     urlify(['b',' ','a',' ', ' '],3)
     urlify([' ',' ','a',' ', ' ',' ',' '],3)

