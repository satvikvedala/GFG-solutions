class Solution
{
    int timer = 0;
	public:
    //Function to return a list of lists of integers denoting the members 
    //of strongly connected components in the given graph.
    void dfs(int u,vector<int> adj[],vector<vector<int>>&ans,vector<int>&low,vector<int>&disc,
    stack<int>&s,vector<bool>&Instack){
        disc[u] = low[u] = timer;
        Instack[u] = true;
        s.push(u);
        timer++;
        for(auto v: adj[u]){
            if (disc[v] == -1){
                dfs(v,adj,ans,low,disc,s,Instack);
                low[u] = min(low[u],low[v]);
            }
            else if (Instack[v] == true){
                low[u] = min(low[u],disc[v]);
            }
            
        }
        if(disc[u] == low[u]){
            vector<int>temp;
            while(!s.empty() && s.top()!=u){
                temp.push_back(s.top());
                Instack[s.top()] = false;
                s.pop();
            }
            if(!s.empty()){
            temp.push_back(s.top());
            Instack[s.top()] = false;
            s.pop();
            sort(temp.begin(),temp.end());
            ans.push_back(temp);
            }
        }
    }
    vector<vector<int>> tarjans(int V, vector<int> adj[])
    {
        //code here
        vector<int> low(V,-1);
        vector<int> disc(V,-1);
        vector<bool> Instack(V,false);
        stack<int>s;
        vector<vector<int>>ans;
        for(int i=0;i<V;i++){
            if(disc[i] == -1){
                dfs(i,adj,ans,low,disc,s,Instack);
            }
        }
        sort(ans.begin(),ans.end());
        return ans;
