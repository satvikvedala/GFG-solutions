class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        count1 = 0
        for item in a:
            count1+=ord(item)
        count2 = 0
        for item in b:
            count2+=ord(item)
        if count1 == count2:
            return True
        else:
            return False
