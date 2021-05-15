class Solution:
    def divide(self, a, b):
        #code here
        Flag = -1 if ((a<0)^(b<0)) else 1
        a = abs(a)
        b = abs(b)
        temp = 0
        quotient = 0
        for i in range(31,-1,-1):
            if(temp+(b<<i)<=a):
                temp = temp+(b<<i)
                quotient|=(1<<i)
        return Flag*quotient
