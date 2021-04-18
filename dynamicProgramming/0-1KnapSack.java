    static int knapSack(int W, int wt[], int val[], int n) 
    { 
         // your code here 
         int dp[][] = new int[n+1][W+1];
         for(int i=0;i<n+1;i++){
             for(int j=0;j<W+1;j++){
                 dp[i][0] = 0;
             }
             
         }
         for(int i=1;i<n+1;i++){
             for(int j=1;j<W+1;j++){
                 dp[i][j] = dp[i-1][j];
                 if(wt[i-1]<=j){
                     dp[i][j] = Math.max(dp[i][j],val[i-1]+dp[i-1][j-wt[i-1]]);
                 }
             }
         }
         return dp[n][W];
    } 
}
