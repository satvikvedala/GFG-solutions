class Solution{
    
    public:
    int maxCandy(int height[], int n) 
    { 
        // Your code goes here
        int i = 0;
        int j = n-1;
        int maxarea = 0;
        while (i<j){
            maxarea = max(maxarea,(j-i-1)*(min(height[i],height[j])));
            if (height[i]<height[j]){
                i++;
            }
            else{
                j--;
            }
        }
        return maxarea;
    }   
};
