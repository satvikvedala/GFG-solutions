class Solution{
    public:
    int Maximize(int a[],int n)
    {
        // Complete the function
        sort(a,a+n);
        long long sum = 0;
        for(long long i=0;i<n;i++){
            sum+=(a[i]*i)%(1000000007);
        }
        return sum%(1000000007);
    }
};
