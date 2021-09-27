class Solution{
    public:
    /* Should return data of middle node. If linked list is empty, then  -1*/
    int getMiddle(Node *head)
    {
        // Your code here
        auto slow = head;
        auto fast = head;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
    return slow->data;
    }
};
