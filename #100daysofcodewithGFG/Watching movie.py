class Solution:
    def solve(self, N, K, heights): 
        #code here
        stack = [N-1]
        count = 0
        nextgreater = [float("inf")]*N
        for i in range(N-2,-1,-1):
            while stack and heights[i]>heights[stack[-1]]:
                stack.pop()
            if len(stack)>0:
                nextgreater[i] = stack[-1]     
            stack.append(i)
        for i in range(N):
            if (nextgreater[i] - i)>K:
                count+=1
        return count
