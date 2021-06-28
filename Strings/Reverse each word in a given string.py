class Solution:
    def reverseWords(self, s):
        # code here
        sarr = s.split(".")
        for i in range(len(sarr)):
            temp = sarr[i]
            temp = temp[::-1]
            sarr[i] = temp
        st=''
        for item in sarr:
            st+=item
            st+='.'
        return st[:len(st)-1]
