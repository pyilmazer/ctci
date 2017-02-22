## with additional data structure
import math

def isOneAway(str1, str2):
    if math.fabs(len(str1) - len(str2)) > 1:
        return False
    count = 0
    if len(str1) > len(str2):
        count = countEditsForInsertionDeletion(str1, str2)
    elif len(str2) > len(str1):
        count = countEditsForInsertionDeletion(str2, str1)
    else:
        count = countEditsForEdition(str1,str2)

    if count > 1:
        return False
    else:
        return True


def countEditsForInsertionDeletion(str1, str2):
    j = 0
    count = 0
    for i in str1:
        if j < len(str2) and i != str2[j]:
            count += 1
        else:
            j += 1
    return count

def countEditsForEdition(str1, str2):
    j = 0
    count = 0
    for i in str1:
        if i != str2[j]:
            count += 1
        j += 1
    return count


if __name__ == '__main__':

    if(isOneAway("ab","abg")):
        print('One Away')
    else:
        print('Not One Away')

    if (isOneAway("abcdf", "abg")):
        print('One Away')
    else:
        print('Not One Away')

    if (isOneAway("abcdf", "abgdf")):
        print('One Away')
    else:
        print('Not One Away')
