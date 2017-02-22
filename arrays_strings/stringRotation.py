import numpy

def isSubstring(str1,str2):
   for i in range(len(str1)):
       if len(str2)+i <= len(str1):
           if str1[i:len(str2)+i] == str2:
               return True

def isRotated(str1,str2):
   if len(str1) == len(str2) and len(str1)>0:
       for i in range(1,len(str2)):
           if isSubstring(str1,str2[0:i]) and isSubstring(str1,str2[i:len(str2)]):
               return True
   return False 


def isRotated2(str1,str2): 
   str3=str1 + str2
   if isSubstring(str3,str2):
       return True
   else:
       return False
       
       
def pprint(mylist):
    res=""
    for i in range(len(mylist)):
       for j in range(len(mylist[i])):
           res += str(mylist[i][j]) + " "
       res += '\n'
    print res


if __name__ == '__main__':
   
   if isRotated("waterbottle","erbottlewat"):
       print "Rotated"
   else:
       print "Not Rotated"    

   if isRotated2("waterbottle","erbottlewat"):
       print "Rotated"
   else:
       print "Not Rotated"    
