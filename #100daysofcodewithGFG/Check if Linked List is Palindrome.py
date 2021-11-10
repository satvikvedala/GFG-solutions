class Solution:
    def isPalindrome(self, head):
        #code here
        st = ''
        curr = head
        while curr:
            st+=str(curr.data)
            curr = curr.next
        l = 0
        r = len(st)-1
        while l<=r:
            if st[l]!=st[r]:
                return False
            l+=1
            r-=1
        return True
