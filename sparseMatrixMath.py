#!/bin/pyhton
### BY: GARY CHEUNG AND DEV SETHI

def createEmptyMatrix(rows,cols):
    """ Create and returns empty matrix of size rows x cols """
    emptyMatrix = []    
    for i in range(int(rows)):
        newMatrix = []
        for j in range(int(cols)):
            newMatrix.append(0)
        emptyMatrix.append(newMatrix)
    return emptyMatrix
    
def denseToValues(dense):
    """ Receives matrix and returns values list """
    values = []
    for i in range(len(dense)):
        for j in range(len(dense)):
            if  (dense[i][j] != 0):
                values.append(dense[i][j])
    return values
    
    
def denseToColumns(dense):
    """ Receives matrix and returns columns list """
    columns = []
    for i in range(len(dense)):
        for j in range(len(dense)):
        
            if  (dense[i][j] != 0):
               columns.append(j)
               
    return columns
    
def nonZeroInRow(dense,columns):
    """ determines how many non zero values are in each row"""
    ##COLUNT OF HOW MANY NON ZERO VALUES ARE IN EACH ROW 
    ## THE POSITION IN THE ARRAY LEN COL CORRESPONDS TO THE ROW NUMBER
    output = []
    for i in range(len(dense)):
            length = 0
            for col in columns:
                  if col == i:
                      length = length + 1
            output.append(length)
    return output
    
def denseToRowIndex(dense,values,columns,lenRow):
    """ Receives matrix, values list and columns list and returns Row Index list """
    
    ##COLUNT OF HOW MANY NON ZERO VALUES ARE IN EACH ROW 
    ## THE POSITION IN THE ARRAY LEN COL CORRESPONDS TO THE ROW NUMBER

    
    rowIndex = []
    ### COLUMN INDEX
    i = 0
    ## ROW INDEX
    j = 0
    ### INDEX FOR VALUES 
    x = 0

    ## CURRENT TOTAL LENGTH OF ROWS TRAVERSER
    lenCount = 0

    while (i < len(dense)):
        while (j < len(dense)):
        
            if (dense[i][j] != 0):
                
                ##The Length Count Counts how many Non zero numbers have been iterated through
                ## When we go to a new row, the lenCount is updated to  the size of the new row 
            
               lenCount = lenCount + (lenRow[i])
                          
               ## TRAVERSING VALUES 
               while (x < len(values)):
                   if (values[x] == dense[i][j]):
                       ## APPREND THE LOCATION IN VALUES TO ROW INDEX 
                       rowIndex.append(x)
                   
                       ## UPDATE TO THE VALUES TRAVERSED IN THE NEXT ROW 
                       x = lenCount                  
                       break
                   x += 1
               #Set the Row Back to the First Row, 
               j = 0
               break          
            j += 1 
        
            ## NEEDED TO RESET J POSTION AND BREAK THIS ITERATION 
            if (j == len(dense[i])):
                j = 0
                break
        #GO TO THE NEXT ROW        
        i += 1  

    ## LAST Value is the number of non zero elemetns
    rowIndex.append(len(values))
    return rowIndex

def sparseToDense(values,columns,rowIndex,colLen):
    """ Reconstructs and returns a matrix from the values, columns and row index lists as well as the size of the square matrix """
      
  
    denseMatrix = createEmptyMatrix(colLen,colLen)

    ## I Stands For the Number of Columns or Rows in the Matrix (which is the same since its a square)
    for i in range(len(values)):
        ## Start at rowIndex[i] which is the position of the non-zero value in the values lists
        startPos = rowIndex[i]
    
        if ((i + 1 )== len(denseMatrix)):
            #if at the end of the columns, just set the end position to the end of values
            endPos = len(values)-1
        else:
            endPos = rowIndex[i+1]
       
        for y in range(startPos,endPos):
            val = int(values[y]) 
            column = int(columns[y])
            row = int(i)
            denseMatrix[row][column] = val
        
    return denseMatrix        

def readColumnVector(rows):
    """ Allows user to input elements of column vector from element 0 to the size of the corresponding square matrix. Returns this list """ 
    colVector = []
    for i in range(rows):
        value = raw_input("Enter a Value For Column Matrix Row-"+str(i)+" :")
        
        ## CHECK TO SEE IF USER INPUT IS DIGIT
        while (value.isdigit() == False):
            print "Value Is Not A Digit"
            value = raw_input("Enter a Value For Column Matrix Row-"+str(i)+" :")
        
        colVector.append(value)
    
    return colVector


def columnMultiplication(denseMatrix,columnVector):
    """ Multiplies specified matrix and column vector. """ 
    product = []
    for i in range(len(denseMatrix)):
        sum = 0
        for j in range(len(denseMatrix)):
            sum = sum + (int(columnVector[i])* denseMatrix[i][j])
        product.append(sum)
    return product



        
            
            
            
