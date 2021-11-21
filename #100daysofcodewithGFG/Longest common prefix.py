class Solution:
    def longestCommonPrefix(self, str1, str2):
        # code here
        ln = 0
        temp = ''
        pattern = ''
        for i in range(len(str1)):
            temp += str1[i]
            if (temp in str2) and (len(temp)>ln):
                ln = len(temp)
                pattern = temp
        i = 0
        j = len(pattern)-1
        while j<len(str1) and j>=0:
            temp = str1[i:j+1]
            if temp == pattern:
                return [i,j]
            i+=1
            j+=1
        return[-1,-1]
