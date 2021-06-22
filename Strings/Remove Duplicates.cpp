class Solution{
public:	
		
	string removeDups(string S) 
	{
	    // Your code goes here
	    int arr[26] = {0};
	    string s;
	    for(int i=0;i<S.size();i++){
	        if(arr[S[i] - 'a'] == 0){
	            s+=S[i];
	            arr[S[i] - 'a']+=1;
	        }
	    }
	    return s;
	}
};
