#IS SUDOKU VALID
    def isValid(self, mat):
        # code here
        def func(mat,x,row,col):
            rowset = set()
            for j in range(9):
                if mat[row][j] in rowset:
                    return False
                if mat[row][j]!=0:
                    rowset.add(mat[row][j])
            colset = set()
            for i in range(9):
                if mat[i][col] in colset:
                    return False
                if mat[i][col]!=0:
                    colset.add(mat[i][col])
            rowstart = row - row%3
            colstart = col - col%3
            subset = set()
            for i in range(0,3):
                for j in range(0,3):
                    if mat[i+rowstart][j+colstart] in subset:
                        return False
                    if mat[i+rowstart][j+colstart]!=0:
                        subset.add(mat[i+rowstart][j+colstart])
            return True
                
        for i in range(9):
            for j in range(9):
                if mat[i][j]!=0 and func(mat,mat[i][j],i,j) == False:
                    return 0
        return 1
