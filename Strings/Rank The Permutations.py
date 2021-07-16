class Solution:
	def findRank(self, S):
		#Code here
		def updatecount(item):
		    for i in range(ord(item),257):
		        count[i]-=1
		def func(item):
		    return 1 if item<=1 else item*(func(item-1))
		count = [0]*(257)
		visited = [False]*(257)
		for item in S:
		    count[ord(item)] += 1
		for i in range(1,257):
		    count[i] += count[i-1]
		l = len(S)
		fact = func(l)
		rank = 1
		for i in range(l):
		    if visited[ord(S[i])] == False:
		        fact = fact//(l)
		        l = l-1
		        rank+=count[ord(S[i])-1]*fact
		        visited[ord(S[i])] = True
		        updatecount(S[i])
		    else:
		        return 0
		return rank%1000003
