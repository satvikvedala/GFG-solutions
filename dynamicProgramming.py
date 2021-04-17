#Jump Game I (leetcode)
    def canJump(self, nums: List[int]) -> bool:
        maxrange = 0
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        for i in range(len(nums)-1):
            if nums[i]!=0:
                maxrange = max(maxrange,i+nums[i])
                if maxrange >= len(nums)-1:
                    return True
            else:
                if maxrange<=nums[i]+i:
                    break
                else:
                    continue
        return False

#Unique BST's (Recursive Approach) Time limit High
    def numTrees(self,N):
        # code here
        if N == 0:
            return 1
        su = 0
        for i in range(N):
            su+=self.numTrees(i)*self.numTrees(N-i-1)
        return su%1000000007
#Unique BST's(DP approach)
    def numTrees(self,N):
        # code here
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1,n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return (dp[n]%1000000007)
