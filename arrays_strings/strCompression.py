
def compress(mystr):
    if len(mystr) <= 1:
        print(mystr)
    count=1
    finalStr=""
    for i in range(1,len(mystr)):
        if mystr[i] == mystr[i-1]:
            count+=1
        else:
            finalStr += mystr[i-1] + str(count);
            count = 1
    finalStr += mystr[i]+str(count);

    if len(finalStr) >= len(mystr):
        print(mystr)
    else:
        print(finalStr)



if __name__ == '__main__':

    compress("aabbbcdddd")
    compress("aaccedd")
    compress("aa")
    compress("aabbccccccdeeddd")

