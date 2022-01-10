class Solution
{
    public static int func(Node head){
        int carry = 0;
        if (head.next == null){
            int sum = head.data+1;
            if (sum>=10){
                head.data = sum%10;
                return 1;
            }
            else{
                head.data = sum;
                return 0;
            }
        }
        else{
            carry = func(head.next);
            int sum = head.data+carry;
            if (sum>=10){
                head.data = sum%10;
                return 1;
            }
            else{
                head.data = sum;
                return 0;
            }
        }
    }
    public static Node addOne(Node head) 
    { 
        //code here.
        int carry = func(head);
        if(carry == 1){
            Node n = new Node(carry);
            n.next = head;
            head = n;
        }
        return head;
    }
}
