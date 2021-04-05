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
#Flattening a Linked List(Long approach)
def flatten(root):
    #Your code here
    res = []
    curr = root
    while curr:
        res.append(curr.data)
        if curr.bottom:
            temp = curr.bottom
            while temp:
                res.append(temp.data)
                temp = temp.bottom
        curr = curr.next
    res = sorted(res)
    tan = Node(res[0])
    head = tan
    for y in range(1,len(res)):
        tan.bottom = Node(res[y])
        tan = tan.bottom
    return head
