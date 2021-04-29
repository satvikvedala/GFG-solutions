class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		import math
		arr = []
	    for i in range(1,2**len(s)):
	        st = ''
	        for shift in range(31,-1,-1):
	            x = 1<<shift
	            if i&x == x:
	                st = st+s[shift]
	        arr.append(st[::-1])
	    return sorted(arr)
