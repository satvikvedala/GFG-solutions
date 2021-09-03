class Solution {
public:
    void MakeZeros(vector<vector<int> >& matrix) {
        // Code here
        int n = matrix.size();
        int m = matrix[0].size();
        vector<vector<int>> grid = matrix;
        for(int i = 0;i<n;i++){
            for(int j = 0;j<m;j++){
                if(matrix[i][j] == 0){
                    int su = 0;
                    if(i>0){
                        su+=matrix[i-1][j];
                        grid[i-1][j] = 0;
                    }
                    if(j>0){
                        su+=matrix[i][j-1];
                        grid[i][j-1] = 0;
                    }
                    if(i<n-1){
                        su+=matrix[i+1][j];
                        grid[i+1][j] = 0;
                    }
                    if(j<m-1){
                        su+=matrix[i][j+1];
                        grid[i][j+1] = 0;
                    }
                    grid[i][j] = su;
                }
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                    matrix[i][j] = grid[i][j];
            }
        }
    }
};
