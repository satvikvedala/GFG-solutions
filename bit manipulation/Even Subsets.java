
  #DP APPROACH
  class Solution
{
    public int countSumSubsets(int[] arr, int N)
    {
        // Code here
        int sum = 0;
        int count = 0;
        for(int i=0;i<N;i++){
            sum = sum+arr[i];
        }
        int dp[][] = new int[sum+1][N+1];
        for(int i=0;i<sum+1;i++){
            dp[i][0] = 0;
        }
        for(int j=0;j<N+1;j++){
            dp[0][j] = 1;
        }
        for(int i = 1;i<sum+1;i++){
            for(int j = 1;j<N+1;j++){
                dp[i][j] = dp[i][j-1];
                if(i>=arr[j-1]){
                    dp[i][j] = dp[i][j]+dp[i-arr[j-1]][j-1];
                }
                if (i%2 == 0){
                    count+=dp[i][N];
                }
            }
        }
        return count;
    }
}


//ShortApproach
class Geeks{
    
    static int countSumSubsets(int arr[],int n)
    {
        
        //Your code here
        int even = 0;
        int odd = 0;
        int x = 0;
        int y = 0;
        for(int i = 0;i<n;i++){
            if(arr[i]%2 ==0) even++;
            else odd++;
        }
        if (even!=0) {x = (int)Math.pow(2,even)-1;}
        if(odd!=0) {y = (int)Math.pow(2,odd-1)-1;}
        return x+y+x*y;
    }
}
