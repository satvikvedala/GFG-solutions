class Solution{
    
    public:
    vector<int> help_classmate(vector<int> arr, int n) 
    { 
        // Your code goes here
        vector<int> v(n,-1);
        stack<int> s;
        s.push(0);
        for(int i=1;i<n;i++){
            while (s.empty()!=true && arr[i]<arr[s.top()]){
            int temp = s.top();
            s.pop();
            v[temp] = arr[i];
        }
        s.push(i);
        }
       return v;
    } 
};
