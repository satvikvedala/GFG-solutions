class Solution{
    public:
    double MedianOfArrays(vector<int>& array1, vector<int>& array2)
    {
        // Your code goes here
        int i = 0;
        int j = 0;
        vector<int> v;
        while (i<array1.size() && j<array2.size()){
            if(array1[i]<array2[j]){
                v.push_back(array1[i]);
                i++;
            }
            else{
                v.push_back(array2[j]);
                j++;
            }
        }
        while(i<array1.size()){
            v.push_back(array1[i]);
            i++;
        }
        while(j<array2.size()){
            v.push_back(array2[j]);
            j++;
        }
        if (v.size()%2 !=0){
            return (double)v[v.size()/2];
        }
        else{
            return (double)(v[v.size()/2]+v[v.size()/2-1])/2;
        }
    
    }
};
