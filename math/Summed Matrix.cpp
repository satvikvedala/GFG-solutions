class Solution {
  public:
    long long sumMatrix(long long n, long long q) {
        // code here
        if(q<=n*2){
        long long high = n+1;
        long long highFreq = n;
        long long distance = abs(q-high);
        return highFreq-distance;
        }
        return 0;
        
    }
};
