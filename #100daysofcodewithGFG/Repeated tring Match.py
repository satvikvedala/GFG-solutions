class Solution:
    def repeatedStringMatch(self, A, B):
        # code here
        count = len(B)//len(A)
        temp1 = ''
        temp2 = ''
        temp3 = ''
        for i in range(count):
            temp1+=A
        if B in temp1:
            return count
        for i in range(count+1):
            temp2+=A
        if B in temp2:
            return count+1
        for i in range(count+2):
            temp3+=A
        if B in temp3:
            return count+2
        return -1
