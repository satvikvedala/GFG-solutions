class Solution {
  public:
    int minCostClimbingStairs(vector<int>&cost ,int N) {
        //Write your code here
        vector<int>dp(N,0);
        dp[0] = cost[0];
        dp[1] = cost[1];
        int i;
        for(i=2;i<N;i++){
            dp[i] = cost[i]+min(dp[i-1],dp[i-2]);
        }
        return min(dp[i-1],dp[i-2]);
    }
};
