class Solution
{
    public:
    //Function to find length of shortest common supersequence of two strings.
    int shortestCommonSupersequence(char* X, char* Y, int m, int n)
    {
        //code here
        int dp[m+1][n+1];
        int i,j;
        for(i=0;i<m+1;i++){
            dp[i][0] = i;
        }
        for(j=0;j<n+1;j++){
            dp[0][j] = j;
        }
        
        for(i=1;i<m+1;i++){
            for(j = 1;j<n+1;j++){
                dp[i][j] = 0;
                if(X[i-1] == Y[j-1]){
                    dp[i][j] = 1+dp[i-1][j-1];
                }
                else{
                    dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        return dp[m][n];
    }
};
