class Solution
{
  public:
  int maxWeightCell(int N, vector<int> Edge)
  {
      // code here
      int n = Edge.size();
      vector<int> v(n,0);
      for(int i=0;i<N;i++){
          if (Edge[i]!=-1){
              v[Edge[i]]+=i;
          }
      }
      int max_weight = 0;
      int cell_number = 0;
      for(int i=0;i<N;i++){
          if (v[i]>=max_weight){
              max_weight = max(max_weight,v[i]);
              cell_number = max(cell_number,i);
          }
          
      }
      return cell_number;
  }
};
