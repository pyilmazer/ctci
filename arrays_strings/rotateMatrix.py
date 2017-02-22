import numpy

def createMatrix(size):
    return [[] for i in range(size)]

def rotateToLeft(matrix):
    matrixT=createMatrix(len(matrix))
    for row in matrix:
        for column in range(len(row)-1,-1,-1):
           matrixT[len(row)-column-1].append(row[column])
    return matrixT      


def rotateToRight(matrix):
    matrixT=createMatrix(len(matrix))
    for i in range(len(matrix)-1,-1,-1):
        row=matrix[i]
        for column in range(len(row)):
           matrixT[column].append(row[column])
    return matrixT

       
def pprint(mylist):
    res=""
    for i in range(len(mylist)):
       for j in range(len(mylist[i])):
           res += str(mylist[i][j]) + " "
       res += '\n'
    print res

def rowsToColumns(matrix):
  columns = [[row[col] for row in matrix] for col in range(len(matrix[1]))]
  return columns

if __name__ == '__main__':
   list1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
   
   pprint(list1)
   list2=rotateToLeft(list1)
   pprint(list2)

   list3=rotateToRight(list1)
   pprint(list3)

   list4=rowsToColumns(list1)
   pprint(list4)
