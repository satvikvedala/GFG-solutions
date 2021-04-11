#Square root of a number(iterative)
    def floorSqrt(self, x): 
    #Your code here
        ans = 0
        if x == 0 or x == 1:
            return x
            
        for i in range(1,x):
            if i*i == x:
                return i
            if i*i<x:
                ans = i
            if i*i>x:
                break
        return ans
 #recursive square root approach
    def mySqrt(self, x: int) -> int:
        def func(l,r,x):
            if l<=r:
                mid = (l+r)//2
                if mid*mid <= x and (mid+1)*(mid+1) > x:
                    return mid
                if mid*mid>x:
                    return func(l,mid,x)
                if mid*mid<x:
                    return func(mid+1,r,x)
            return l
        
        l = 0
        r = x
        return func(l,r,x)
