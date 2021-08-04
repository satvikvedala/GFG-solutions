class Solution{
    public:
    string findSubString(string str)
    {
        // Your code goes here
        int se = 0;
        bool set[256] = {false};
        for (int j=0;j<str.length();j++){
            if (set[str[j]] == false){
                set[str[j]] = true;
                se+=1;
            }
        }
        int arr[256] = {0};
        int start = 0;
        int count = 0;
        int minLen = 256;
        int start_index = -1;
        for(int i=0;i<str.length();i++){
            arr[str[i]]+=1;
            if (arr[str[i]] == 1){
                count+=1;
            }
            if (count == se){
                while (arr[str[start]]>1){
                    if (arr[str[start]]>1)
                        arr[str[start]]-=1;
                    start+=1;
                }
                int l = i-start+1;
                if(l<minLen){
                    minLen = l;
                    start_index = start;
                }
            }
        }
        return str.substr(start_index,minLen);
