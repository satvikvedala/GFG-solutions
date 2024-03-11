class Solution{
public:
	
	int findMaximum(int arr[], int n) {
	    // code here
	    int low = 0;
	    int high = n-1;
	    return BinarySearch(arr,low,high);
	}
	int BinarySearch(int arr[],int low,int high){
	    if (high > low){
	    int mid = low+(high-low)/2;
	    if(arr[mid]>arr[mid+1]){
	        return BinarySearch(arr,low,mid);
	    }
	    if(arr[mid]<arr[mid+1]){
	        return BinarySearch(arr,mid+1,high);
	    }
	}
	return arr[high];
	}
};
