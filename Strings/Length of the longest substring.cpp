class Solution{
    public:
    int longestUniqueSubsttr(string S){
        //code
        int n = S.size();
        int i = 0;
        int j = 1;
        
        vector<int> cnt(256,0);
        cnt[S[0]]++;
        
        int res = 1;
        while (j<n){
            if (cnt[S[j]] == 0){
                res = max(res,j-i+1);
                cnt[S[j]] = 1;
                j++;
            }
            else{
                cnt[S[i]]--;
                i++;
            }
        }
        return res;
        
    }
};
