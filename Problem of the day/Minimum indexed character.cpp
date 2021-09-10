class Solution
{
  public:
    //Function to find the minimum indexed character.
    int minIndexChar(string str, string patt)
    {
        // Your code here
        unordered_set<char> set;
        for(int i = 0;i<patt.length();i++){
            set.insert(patt[i]);
        }
        for(int j=0;j<str.length();j++){
            if(set.find(str[j])!= set.end()){
                return j;
            }
        }
        return -1;
    }
};
