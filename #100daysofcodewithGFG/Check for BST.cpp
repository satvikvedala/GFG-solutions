class Solution
{
    public:
    //Function to check whether a Binary Tree is BST or not.
    void func(Node* root,vector<int> &arr){
        if (root){
            func(root->left,arr);
            arr.push_back(root->data);
            func(root->right,arr);
        }
    }
    bool isBST(Node* root) 
    {
        // Your code here
        vector<int> arr;
        func(root,arr);
        for(int i=1;i<arr.size();i++){
            if(arr[i]<=arr[i-1]){
                return false;
            }
        }
        return true;
    }
};
