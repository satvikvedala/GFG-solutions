string isSubset(int a1[], int a2[], int n, int m) {
    unordered_set<int>s;
    for(int i=0;i<n;i++){
        s.insert(a1[i]);
    }
    for(int j=0;j<m;j++){
        if(s.find(a2[j]) == s.end()){
            return "No";
        }
    }
    return "Yes";
    
}
