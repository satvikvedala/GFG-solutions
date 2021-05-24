class Solution{
    public:
    // arr: input array
    // n: size of array
    //Function to find the sum of contiguous subarray with maximum sum.
    int maxSubarraySum(int arr[], int n){
        
        // Your code here
        int end = INT_MIN;
        int curr = 0;
        for(int i = 0;i<n;i++){
            curr = curr+arr[i];
            if (curr>end){
                end = curr;
            }
            if (curr<0){
                curr = 0;
            }
            
            
        }
        return end;
        
    }
};
