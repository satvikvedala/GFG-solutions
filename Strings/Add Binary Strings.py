class Solution:
	def addBinary(self, A, B):
		# code here
		a = int(A,2)
		b = int(B,2)
		a = a+b
		return bin(a)[2:]
