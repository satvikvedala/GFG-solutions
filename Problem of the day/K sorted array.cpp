class Solution {
  public:
  int binary_search(int arr[],int n,int item){
      int l = 0;
      int r = n-1;
      while(l<=n){
          int mid = l+(r-l)/2;
          if(arr[mid] == item){
              return mid;
          }
          else if(arr[mid]<item){
              l = mid+1;
          }
          else{
              r = mid-1;
          }
      }
  }
    string isKSortedArray(int arr[], int n, int k)
    {
        //code here.
        int aux[n];
        for(int i=0;i<n;i++){
            aux[i] = arr[i];
        }
        sort(aux,aux+n);
        for(int i=0;i<n;i++){
            int index = binary_search(aux,n,arr[i]);
            if (abs(i-index)>k){
                return "No";
            }
        }
        return "Yes";
    }
};
