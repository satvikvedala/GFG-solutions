class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		def func(s,arr,st,n,i):
		    if n == 0:
		        arr.append(st[::-1])
		        return 
		    func(s,arr,st,n-1,i-1)
		    func(s,arr,st+s[i],n-1,i-1)
		arr = []
		st = ''
		func(s,arr,st,len(s),len(s)-1)
		return sorted(arr[1:])
