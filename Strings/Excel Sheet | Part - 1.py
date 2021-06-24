class Solution:
    def ExcelColumn(self, N):
        #return required string
        #code here
        dic = {}
        for i in range(1,27):
            dic[i] = chr(64+i)
        dic[0] = 'Z'
        st = ''
        while N>0:
            rem = N%26
            st+=dic[rem]
            if rem == 0:
                N = (N//26)-1
            else:
                N = N//26
        return st[::-1]
