class Solution:
    
    #Function to find the minimum indexed character.
    def minIndexChar(self,str, pat): 
        #code here
        se = set(pat)
        for i in range(len(str)):
            if str[i] in se:
                return i
        return -1
