class Solution
{
    public:
        vector <int> search(string pat, string txt)
        {
            //code hee.
            vector<int> res;
            for (int i=0;i<(txt.size()-pat.size()+1);i++){
                if(txt.substr(i,pat.length()) == pat){
                    res.push_back(i+1);
                }
            }
            if (res.empty()){
                res.push_back(-1);
            }
            return res;
        }
     
};
