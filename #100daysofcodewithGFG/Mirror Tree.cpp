class Solution {
  public:
    // Function to convert a binary tree into its mirror tree.
    void func(Node* node){
        if (node == NULL){
            return;
        }
        swap(node->left,node->right);
        func(node->left);
        func(node->right);
    }
    void mirror(Node* node) {
        // code here
        func(node);
    }
};
