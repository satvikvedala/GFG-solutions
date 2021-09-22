class Solution{

    public:
    int repeatedStringMatch(string A, string B) 
    {
        // Your code goes here
        string temp;
        for(int i = 1;i<100;i++){
            temp+=A;
            if(temp.find(B)!= string::npos){
                return i;
            }
        }
        return -1;
    }
  
};
