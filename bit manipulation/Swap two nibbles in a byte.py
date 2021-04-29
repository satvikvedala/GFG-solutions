class Solution:
    def swapNibbles (self, N):
        # code here 
        num1 = N>>4
        temp = N&0xF
        num2 = temp<<4
        return num1|num2
