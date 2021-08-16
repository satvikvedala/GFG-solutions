#involving dijkastra's
	def minimumCostPath(self, grid):
		#Code here
		import heapq
		row = len(grid)
		col = len(grid[0])
		dx = [-1,0,1,0]
		dy = [0,1,0,-1]
		dist = [[float("inf") for j in range(col)] for i in range(row)]
		visited = [[False for j in range(col)] for i in range(row)]
		dist[0][0] = grid[0][0]
		heap = [(dist[0][0],0,0)]
		while heap:
		    d,x,y = heapq.heappop(heap)
		    visited[x][y] = True
		    for i in range(4):
		        u = x+dx[i]
		        v = y+dy[i]
		        if u>=0 and v>=0 and u<row and v<col and visited[u][v] == False:
		            if dist[u][v]>d+grid[u][v]:
		                dist[u][v] = d+grid[u][v]
		                heapq.heappush(heap,(dist[u][v],u,v))
		return dist[-1][-1]
