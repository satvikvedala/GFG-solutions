class Solution{
public:
int func(int N,int k){
    if (N == 1) return 1;
    return (func(N-1,k)+k-1)%N+1;
}
    int find(int N){
        // code here
        int k = 2;
        return func(N,k);
    }
};
