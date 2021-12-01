class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
		from collections import deque
		dq = deque()
		time = 1
		tt = 0
		one_count = 0
		for i in range(len(grid)):
		    for j in range(len(grid[0])):
		        if grid[i][j] == 1:
		            one_count+=1
		        if grid[i][j] == 2:
		            dq.append((time,i,j))
	    while(len(dq) and one_count>0):
	        temp = dq.popleft()
	        tt = temp[0]
	        i = temp[1]
	        j = temp[2]
	        if (i+1)<len(grid):
		        if grid[i+1][j]==1:
		            grid[i+1][j] = 2
		            dq.append((tt+1,i+1,j))
		            one_count-=1
		      if (i-1)>=0:
		        if grid[i-1][j]==1:
		            grid[i-1][j] = 2
		            dq.append((tt+1,i-1,j))
		            one_count-=1
		      if (j+1)<len(grid[0]):
		        if grid[i][j+1]==1:
		            grid[i][j+1] = 2
		            dq.append((tt+1,i,j+1))
		            one_count-=1
		      if (j-1)>=0:
		        if grid[i][j-1]==1:
		            grid[i][j-1] = 2
		            dq.append((tt+1,i,j-1))
		            one_count-=1
        if one_count == 0:
            return tt
        return -1
