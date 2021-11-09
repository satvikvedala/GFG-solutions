class Solution{
    
    public:
    int func(int x){
        int su = 0;
        while(x>0){
            int rem = x%10;
            su+=rem;
            x = x/10;
        }
        return su;
    }
    int RulingPair(vector<int> arr, int n) 
    { 
    	// Your code goes here
    	unordered_map<int,int> map;
    	int ans = -1;
    	for(int i=0;i<n;i++){
    	    int sum = func(arr[i]);
    	    if (map.find(sum) == map.end()){
    	        map[sum] = arr[i];
    	        continue;
    	    }
    	    int temp = map[sum]+arr[i];
    	    ans = max(ans,temp);
    	    map[sum] = max(map[sum],arr[i]);
    	}
    	return ans;
    }   
};
