class Solution{
    //Function to find the leaders in the array.
    public:
    vector<int> leaders(int a[], int n){
        // Code here
        vector<int> stack;
        for(int i=0;i<n;i++){
            while(stack.size()>0 && stack.back()<a[i]){
                stack.pop_back();
            }
            stack.push_back(a[i]);
        }
        return stack;
        
    }
};
