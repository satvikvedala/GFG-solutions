#to iteratively determine what would be each bit of the final result from left to right. And it narrows down the candidate group iteration by iteration. 
#e.g. assume input are a,b,c,d,...z, 26 integers in total. In first iteration, if you found that a, d, e, h, u differs on the MSB(most significant bit), 
#so you are sure your final result's MSB is set. Now in second iteration, you try to see if among a, d, e, h, u there are at least two numbers make the 2nd MSB differs, 
#if yes, then definitely, the 2nd MSB will be set in the final result. And maybe at this point the candidate group shinks from a,d,e,h,u to a, e, h. Implicitly, 
#every iteration, you are narrowing down the candidate group, but you don't need to track how the group is shrinking, you only care about the final result.

class Solution:
    def max_xor(self, arr, n):
        #code here
        mask = 0
        ma = 0
        for i in range(31,-1,-1):
            mask = mask|(1<<i)
            se = set()
            for item in arr:
                se.add(item&mask)
            print(se)
            temp = ma|(1<<i)
            print(temp)
            for item in se:
                if item^temp in se:
                    ma = temp
                    print(ma)
                    break
        return ma
