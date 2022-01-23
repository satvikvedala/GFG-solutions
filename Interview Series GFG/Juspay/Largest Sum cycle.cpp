class Solution
{
  public:
  long long largestSumCycle(int N, vector<int> Edge)
  {
    // code here
    int max_sum = -1;
    for(int i=0;i<N;i++){
        int node = i;
        int sum = 0;
        unordered_set<int> visited;
        while(node>=0 && node<N && visited.count(node) == 0 && i!=Edge[node]){
            visited.insert(node);
            sum+=node;
            node = Edge[node];
        }
        if (node>=0 && node<N && i == Edge[node]){
            max_sum = max(max_sum,sum);
        }
    }
    return max_sum;
  }
};
