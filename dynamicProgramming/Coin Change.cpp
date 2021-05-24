class Solution
{
  public:
    long long int count( int S[], int m, int n )
    {
       
        //code here.
        long long int table[n+1][m+1];
        for (int j =0;j<m+1;j++){
            table[0][j] = 1;
        }
        for(int i = 0;i<n+1;i++){
            table[i][0] = 0;
        }
        for (int i = 1;i<n+1;i++){
            for(int j=1;j<m+1;j++){
                table[i][j] = table[i][j-1];
                if(S[j-1]<=i){
                    table[i][j]+=table[i-S[j-1]][j];
                }
            }
        }
        return table[n][m];
    }
};
