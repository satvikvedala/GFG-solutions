class Solution:
	def minJumps(self, arr, n):
	    steps = arr[0]
	    reach = arr[0]
	    count = 1
	    for i in range(1,n):
	        if i>reach:
	            return -1
	        if i == n-1:
	            return count
	        reach = max(reach,arr[i]+i)
	        steps-=1
	        if steps == 0:
	            count+=1
	            steps = reach - i
	    return -1
