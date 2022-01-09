def rotate(matrix): 
    #code here
    for i in range(len(matrix)):
        for j in range(i,len(matrix[0])):
            if (i!=j):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
    i = 0
    j = len(matrix)-1
    while(i<=j):
        for k in range(len(matrix[0])):
            temp = matrix[i][k]
            matrix[i][k] = matrix[j][k]
            matrix[j][k] = temp
        i+=1
        j-=1
    return matrix
