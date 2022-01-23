class Solution():
    def maxWeightCell(self, N, Edge):
        #your code goes here
        arr = [0]*N
        for i in range(N):
            if Edge[i]!=-1:
                arr[Edge[i]]+=i
        weight = 0
        number = 0
        for i in range(N):
            if arr[i]>=weight:
                weight = max(weight,arr[i])
                number = max(number,i)
        return number
