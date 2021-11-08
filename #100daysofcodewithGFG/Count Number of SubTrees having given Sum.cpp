int cnt;
int func(Node* root,int X){
    if (root == NULL){
        return 0;
    }
    int left = func(root->left,X);
    int right = func(root->right,X);
    
    if(left+right+root->data == X){
        cnt++;
    }
    return left+right+root->data;
}
int countSubtreesWithSumX(Node* root, int X)
{
	// Code here
    cnt = 0;
	int ans = func(root,X);
	return cnt;
}
