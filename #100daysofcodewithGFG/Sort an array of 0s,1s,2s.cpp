class Solution
{
    public:
    void sort012(int a[], int n)
    {
        // coode here 
        int count_0 = 0;
        int count_1 = 0;
        int count_2 = 0;
        
        for(int i=0;i<n;i++){
            if (a[i] == 0){
                count_0++;
            }
            else if(a[i] == 1){
                count_1++;
            }
            else{
                count_2++;
            }
        }
        int i = 0;
        int count = 0;
        while (i<count+count_0){
            a[i] = 0;
            i++;
        }
        count+=count_0;
        while(i<count+count_1){
            a[i] = 1;
            i++;
        }
        count+=count_1;
        while(i<count+count_2){
            a[i] = 2;
            i++;
        }
    }
    
};
