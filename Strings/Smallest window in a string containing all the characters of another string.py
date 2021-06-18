class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        def isValid(string):
            for item in p:
                if string.count(item)<p.count(item):
                    return 0
            return 1
        ans = ''
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                string = s[i:j]
                k = isValid(string)
                if k == 1:
                    if len(ans) == 0 or len(string)<len(ans):
                        ans = string
        if len(ans) == 0:
            return '-1'
        return ans
