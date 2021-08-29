class Solution {
  public:
  void func(Node *root,unordered_map<int,pair<int,int>> li,int y,int x){
      if (root == NULL){
          return;
      }
      if (li.find(x) == li.end()){
          li[x] = make_pair(root->data,y);
      }
      else{
          pair<int, int> p = li[x];
          if(y>=p.second){
              p.second = y;
              p.first = root->data;
          }
      }
      func(root->left,li,y+1,x-1);
      func(root->right,li,y+1,x+1);
      
  }
    vector <int> bottomView(Node *root) {
        // Your Code Here
        unordered_map<int,pair<int,int>> li;
        int y = 0;
        int x = 0;
        func(root,li,y,x);
        vector<int>v;
        map < int, pair < int, int > > ::iterator it;
        for (it = li.begin(); it != li.end(); ++it)
        {
        pair < int, int > p = it -> second;
        v.push_back(p.first);
        }
        return v;
        
    }
};
