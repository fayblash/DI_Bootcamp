# Instructions
# Hint: Look at the remote learning “Matrix” videos

# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, select only the alpha characters and connect them, then he replaces every group of symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix:
matrix=[
    "7ir",
    "Tsi",
    "h%x",
    "i&$",
    "sM*",
    "$a*",
    "*t%",
    "^&!",
    ]

def decode_matrix(matrix):
    code=""
    temp=""
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            # print(matrix[x][y])
            if matrix[x][y].isalpha():
                code+=matrix[x][y]
            else:
                if temp.isalpha()==False:
                    code+=" "
            temp=matrix[x][y]    
                             
    print(code)
                
decode_matrix(matrix)