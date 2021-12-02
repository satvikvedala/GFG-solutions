class Solution{
public:

	// Function to find maximum product subarray
	long long maxProduct(vector<int> arr, int n) {
	    // code here
	    if(n == 1){
	        return arr[0];
	    }
	    long long mi = 1;
	    long long ma = 1;
	    long long res = INT_MIN;
	    for(int i=0;i<n;i++){
	        if(arr[i]>0){
	            ma = ma*arr[i];
	            mi = mi*arr[i];
	        }
	        else if (arr[i] == 0){
	            ma = 1;
	            mi = 1;
	        }
	        else{
	            long temp = ma*arr[i];
	            ma = max((long long)1, mi*(long long)arr[i]);
	            mi = temp;
	        }
	        res = max(res,ma);
	    }
	    return res;
	    
	}
};
