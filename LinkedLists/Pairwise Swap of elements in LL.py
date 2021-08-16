class Solution:    
    def pairWiseSwap(self, head):
        # code here
        prev = None
        first = head
        while first and first.next:
            second = first.next
            nxt = second.next
            if prev:
                prev.next = second
                second.next = first
                first.next = nxt
            else:
                second.next = first
                first.next = nxt
                head = second
            prev = first
            first = prev.next
        return head
