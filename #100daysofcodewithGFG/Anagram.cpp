class Solution
{
    public:
    //Function is to check whether two strings are anagram of each other or not.
    bool isAnagram(string a, string b){
        
        // Your code here
        int count1 = 0;
        int count2 = 0;
        for(int i=0;i<a.length();i++){
            count1+=int(a[i]);
        }
        for(int j=0;j<b.length();j++){
            count2+=int(b[j]);
        }
        if(count1 == count2){
            return true;
        }
        return false;
        
    }

};
