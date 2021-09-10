bool func(vector<int> adj[],vector<bool> visited,vector<bool> recStack, int i){
        visited[i] = true;
        recStack[i] = true;
        
        for(auto x:adj[i]){
            if(visited[x] == false){
                if(func(adj,visited,recStack,x)){
                    return true;
                }
            }
            else if(recStack[x]){
                return true;
            }
        }
        recStack[i] = false;
        return false;
    }
	bool isPossible(int N, vector<pair<int, int> >& prerequisites) {
	    // Code here
	    vector<int> adj[N];
	    for (auto x:prerequisites){
	        adj[x.second].push_back(x.first);
	    }
	    vector<bool> visited(N,false);
	    vector<bool> recStack(N,false);
	    
	    for(int i = 0;i<N;i++){
	        if(visited[i] == false){
	            if(func(adj,visited,recStack,i)){
	                return false;
	            }
	        }
	    }
	    return true;
	    
	}
};
