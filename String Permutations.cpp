class Solution{
    public:
    //Complete this function
    void func(string S,vector<string> &res,int l,int r){
        if(l == r){
            res.push_back(S);
            return;
        }
        else{
            for(int i=l;i<r;i++){
                swap(S[l],S[i]);
                func(S,res,l+1,r);
                swap(S[l],S[i]);
            }
        }
    }
    vector<string> permutation(string S)
    {
        //Your code here
        int n = S.size();
        vector<string> res;
        func(S,res,0,n);
        sort(res.begin(),res.end());
        return res;
    }
};
