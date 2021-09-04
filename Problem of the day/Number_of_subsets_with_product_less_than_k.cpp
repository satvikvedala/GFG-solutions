class Solution {
  public:
    void func(int arr[], int N, int K, int prod,int *count,int i){
        if(i == N){
            if(prod<=K){
                *count = *count+1;
            }
            return;
        }
        else if(i>N||prod>K){
            return;
        }
        func(arr,N,K,prod*arr[i],count,i+1);
        func(arr,N,K,prod,count,i+1);
    }
    int numOfSubsets(int arr[], int N, int K) {
        // code here
        int prod = 1;
        int count = 0;
        func(arr,N,K,prod,&count,0);
        return count-1;
    }
};
