class Solution:
    def maxLength(self, S):
        # code here
        open = 0
        close = 0
        maxLen = 0
        for item in S:
            if item == '(':
                open+=1
            elif item == ')':
                close+=1
            if open == close:
                maxLen = max(maxLen,open+close)
            elif close>open:
                open = close = 0
        open = 0
        close = 0
        for item in S[::-1]:
            if item == '(':
                open+=1
            if item == ')':
                close+=1
            if open == close:
                maxLen = max(maxLen,open+close)
            elif open>close:
                open = close = 0
        return maxLen
