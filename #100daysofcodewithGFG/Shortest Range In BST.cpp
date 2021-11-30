class Solution{
    
    public:
    pair<int, int> shortestRange(Node *root) {
        // Your code goes here
        queue<Node*>q;
        q.push(root);
        vector<vector<int>>v;
        while(!q.empty()){
            int l = q.size();
            vector<int> temp;
            while(l--){
                Node* x = q.front();
                q.pop();
                if(x->left){
                    q.push(x->left);
                }
                if(x->right){
                    q.push(x->right);
                }
                temp.push_back(x->data);
            }
            v.push_back(temp);
            
        }
        priority_queue<vector<int>,vector<vector<int>>,greater<vector<int>>>pq;
        int minirange = INT_MAX;
        int maxi = INT_MIN;
        for(int i=0;i<v.size();i++){
            pq.push({v[i][0],i,0});
            maxi = max(maxi,v[i][0]);
        }
        int left = 100000;
        int right = 0;
        while(true){
            auto x = pq.top();
            pq.pop();
            int num = x[0];
            int lis = x[1];
            int idx = x[2];
            if(maxi-num < minirange){
                minirange = maxi-num;
                left = num;
                right = maxi;
            }
            if(idx+1 == v[lis].size()){
                break;
            }
            pq.push({v[lis][idx+1],lis,idx+1});
            maxi = max(maxi,v[lis][idx+1]);
            
        }
        pair<int,int>ans;
        ans.first = left;
        ans.second = right;
        return ans;
        
    }
};
