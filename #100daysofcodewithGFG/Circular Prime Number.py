class Solution:
    def isCircularPrime(self, n):
        # Code here
        if n == 1:
            return 0
        import math
        def func(n):
            if n<20:
                count = 0
            else:
                count = 1
            for i in range(1,20):
                if n%i == 0:
                    count+=1
            if count == 2:
                return True
            return False
        m = len(str(n))
        for i in range(m):
            if func(int(n)) == False:
                return 0
            temp = str(n)
            first = temp[0]
            second = temp[1:]
            n = second+first
        return 1
