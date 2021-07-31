class Solution:
    def wordBoggle(self,board,dictionary):
        # return list of words(str) found in the board
        def func(board,dictionary,word,visited,i,j,k):
            if k == len(word):
                return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or visited[i][j] == True:
                return False
            elif board[i][j] == word[k]:
                visited[i][j] = True
                a1 = func(board,dictionary,word,visited,i-1,j-1,k+1)
                a2 = func(board,dictionary,word,visited,i-1,j,k+1)
                a3 = func(board,dictionary,word,visited,i-1,j+1,k+1)
                a4 = func(board,dictionary,word,visited,i,j-1,k+1)
                a5 = func(board,dictionary,word,visited,i,j+1,k+1)
                a6 = func(board,dictionary,word,visited,i+1,j-1,k+1)
                a7 = func(board,dictionary,word,visited,i+1,j,k+1)
                a8 = func(board,dictionary,word,visited,i+1,j+1,k+1)
                visited[i][j] = False
                return a1 or a2 or a3 or a4 or a5 or a6 or a7 or a8
            return False
        res = []
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        for word in dictionary:
            flag = 0
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if func(board,dictionary,word,visited,i,j,0):
                        res.append(word)
                        flag = 1
                        break
                if flag == 1:
                    break
        return sorted(res)
