class Solution{
    public:
    
    //Function to rotate an array by d elements in counter-clockwise direction. 
    int g_c_d(int a,int b){
        if(b == 0){
            return a;
        }
        else{
            return g_c_d(b,a%b);
        }
    }
    void rotateArr(int arr[], int d, int n){
        // code here
        d = d%n;
        int gcd1 = g_c_d(n,d);
        for(int i=0;i<gcd1;i++){
            int j = i;
            int temp = arr[i];
            while (1){
                int k = j+d;
                if (k>=n){
                    k = k-n;
                }
                if (k == i){
                    break;
                }
                arr[j] = arr[k];
                j = k;
            }
            arr[j] = temp;
        }
    }
};
