#Kadanes Algo
class Solution {
  public:
    int func(int arr[],int n){
        int cs = 0;
        int max = INT_MIN;
        
        for (int i = 0;i<n;i++){
            cs = cs+arr[i];
            if(cs>max){
                max = cs;
            }
            if(cs<0){
                cs = 0;
            }
        }
        return max;
    }
#
    int maximumSumRectangle(int R, int C, vector<vector<int>> M) {
        // code here
        int temp[R];
        int ma=INT_MIN;
        for(int i=0;i<C;i++){
            memset(temp,0,sizeof(temp));
            for(int j=i;j<C;j++){
                int sum = 0;
                for(int k=0;k<R;k++){
                    temp[k] += M[k][j];
                }
                sum = func(temp,R);
                if (sum>ma)
                    ma = sum;
            }
        }
        return ma;
        
    }
};
