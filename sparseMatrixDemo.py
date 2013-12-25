#!/bin/pyhton
### BY: GARY CHEUNG AND DEV SETHI


import sys
import re
from sparseMatrixMath import*

def parseNonZeroEntries(input):
    """ takes in string of matrix element input and outputs tuple """
    match = re.findall(r'[0-9]+', input)
    return match

   
def createSparseMatrix(entry,rows,cols):
      """ Takes In User Entry and Number of Rows and Outputs a Sparse Matrix """
     ## CREATE A EMPTY MATRIX DEFINED BY SIZE OF USER##
      sparseMatrix = createEmptyMatrix(rows,cols)
     
      ### LOOPING THROUGH THE EMPTY MATRIX AND APPENDING THE USER INPUT VALUES TO IT
      for i in range(len(entry)):
          sparseMatrix[int(entry[i][0])][int(entry[i][1])] = int(entry[i][2])
      return sparseMatrix
      
def matrixConstruct(cols):
    """ Creates a 0-filled square matrix of cols size, prompts user to populate element-by-element and returns the populated matrix """
 
    #Initiate variables
    rows = cols
    values = ""
    entry = []
    flag = 0    #Stays 0 if first value entered is q, avoids returning an undefined matrix
    while (values != "q"): #User finishes input by entering 'q'
        values = raw_input("Enter values in form '(row,column)-value' or enter 'q' if complete: ")
        
        if (values != "q"):
            flag = 1
            values = parseNonZeroEntries(values)
            if (len(values) != 3):  #Error Check
                print "Length Error"
                continue

            if((int(values[0]) > (int(rows)-1)) or (int(values[1]) > (int(rows)-1) )): #Error check
                print "Row size too large"
                continue 

            entry.append(values)
            
            sparseMatrix = createSparseMatrix(entry,rows,cols)
            print "Current matrix: "
            matrixDisplay(sparseMatrix)
    if (flag == 0):
        sparseMatrix = createEmptyMatrix(rows,cols) #Creates all 0 matrix if no values are entered before user quits
    return sparseMatrix

def matrixDisplay(matrix):
    """ Displays the matrix passed to the function, returns nothing """
    for i in range(0,len(matrix)):
        print matrix[i]
    return None

def rowPrompt():
    
    rows  = raw_input("Enter number of rows: ")
    
    while (rows.isdigit() == False):
        print "Value Is Not A Digit"
        rows  = raw_input("Enter number of rows: ")
    
    return int(rows)
        
        
def main():
    repeat = True
    while repeat:
        try:
            rows  =  rowPrompt()
    
            #Ask user to produce a sparse matrix, returned to main as dense matrix
            dense = matrixConstruct(rows)
    
            #Produce CSR based on dense matrix
            values = denseToValues(dense)
            columns = denseToColumns(dense)
    
    
            lenRow = nonZeroInRow(dense,columns)
            rowIndex = denseToRowIndex(dense, values, columns,lenRow)

            #Display original matrix
            print "\nOriginal Matrix: "
            matrixDisplay(dense)
            print "\nReconstructed Matrix: "
    
            #Reconstruct matrix from CSR and display
            reconstructedMatrix = sparseToDense(values, columns, rowIndex,rows)
            matrixDisplay(reconstructedMatrix)

            #Check for equality betweeen original and reconstructed matrix
            if (dense == reconstructedMatrix):
                print "\nReconstructed matrix is equal to original matrix\n"
            else:
                print "\nReconstructed matrix is not equal to original matrix\n"

            #Ask user for column vector to multiply against matrix    
            colVector = readColumnVector(rows)
            print ""
            matrixDisplay(dense)
            print "mulitplied by"
            matrixDisplay(colVector)
            print "equals"
    
            #Perofrm multiplication of matrix and column vector
            matrixProduct = columnMultiplication(dense, colVector)
    
            #Display product
            matrixDisplay(matrixProduct)

            #Option to restart
            repeat_Input = raw_input("\nRepeat (y/n)?: ")
            if (repeat_Input == 'y' or repeat_Input == "Y"):
                repeat = True
            elif (repeat_Input == 'n' or repeat_Input == 'N'):
                repeat = False
                exit
            else:
                print "Invalid response"
        except KeyboardInterrupt:
                print "Exiting Program"
                sys.exit(0)
       
if __name__ == "__main__":
    main()


    
