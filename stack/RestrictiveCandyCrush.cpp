class Solution{
    public:
    string Reduced_String(int k,string s){
        // Your code goes here
        if(k == 1){
            return "";
        }
        string output = "";
        stack<pair<char,int>> stk;
        for(int i=0;i<s.length();i++){
            if(stk.size() == 0){
                stk.push(make_pair(s[i],1));
            }
            else if(stk.top().first != s[i]){
                stk.push(make_pair(s[i],1));
            }
            else{
                if(stk.top().second == k-1){
                    stk.pop();
                }
                else{
                    stk.top().second+=1;
                }
                
            }
        }
        while(!stk.empty()){
            while(stk.top().second>0){
                output+=stk.top().first;
                stk.top().second-=1;
            }
            stk.pop();
        }
        reverse(output.begin(),output.end());
        return output;
    }


};
