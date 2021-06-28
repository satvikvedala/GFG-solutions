class Solution:
	def idToShortURL(self,n):
		# code here
		dic = {}
		k = 0
		for i in range(26):
		    dic[i] = chr(97+i)
		k+=i+1
		for i in range(26):
		    dic[k+i] = chr(65+i)
		k+=i+1
		for i in range(10):
		    dic[k+i] = str(i)
		st = ''
		while(n>=62):
		    rem = n%62
		    st = st+dic[rem]
		    n = n//62
		st = st+dic[n]
		st = st[::-1]
		return st
