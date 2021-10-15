class Solution {
  public:
  void func(vector<int> &arr,set<vector<int>> &s,int l, int r){
      if(l == r){
          s.insert(arr);
          return;
      }
      else{
          for(int i=l;i<r;i++){
              swap(arr[l],arr[i]);
              func(arr,s,l+1,r);
              swap(arr[l],arr[i]);
          }
      }
  }
    vector<vector<int>> uniquePerms(vector<int> arr ,int n) {
        // code here
        sort(arr.begin(),arr.end());
        set<vector<int>>s;
        vector<vector<int>>res;
        func(arr,s,0,n);
        for(auto x:s){
            res.push_back(x);
        }
        return res;
        
        
    }
};
