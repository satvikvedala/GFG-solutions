class Solution:
	def removeDups(self, S):
		# code here
		hash1 = [0]*26
		s = ''
		for item in S:
		    if hash1[ord(item)-97] == 0:
		        s+=item
		        hash1[ord(item)-97] += 1
		return s
