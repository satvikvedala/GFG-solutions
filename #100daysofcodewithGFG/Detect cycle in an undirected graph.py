	def isCycle(self, V, adj):
		#Code here
		def func(adj,u,p):
		    parent[u] = p
		    visited[u] = True
		    for item in adj[u]:
		        if (item != parent[u]) and (visited[item] == True):
		            return True
		        elif visited[item] == False:
		            if func(adj,item,u) == True:
		                return True
		    return False
		parent = [-1]*(V+1)
		visited = [False]*(V+1)
		for i in range(V):
		    if visited[i] == False:
		        if func(adj,i,-1) == True:
		            return True
		return False
