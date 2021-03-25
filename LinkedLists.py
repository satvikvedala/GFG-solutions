#Reverse a Linked List in groups of given size
   def reverse(self,head, k):
        curr = head
        prev = None
        nex = None
        count = 0
        while curr!=None and count<k:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            count+=1
        if nex!=None:
            resthead = self.reverse(curr,k)
            head.next = resthead
        return prev
