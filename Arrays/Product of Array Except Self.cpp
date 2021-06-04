class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        int left[n],right[n];
        
        left[0] = nums[0];
        right[n-1] = nums[n-1];
        
        for(int i=1;i<n;i++){
            left[i] = left[i-1]*nums[i];
        }
        
        for(int j=n-2;j>-1;j--){
            right[j] = right[j+1]*nums[j];
        }
        
        for(int k=0;k<n;k++){
            if (k == 0){
                nums[k] = right[k+1];
            }
            else if(k == n-1){
                nums[k] = left[k-1];
            }
            else{
                nums[k] = left[k-1]*right[k+1];
            }
        }
        return nums;
    }
};
