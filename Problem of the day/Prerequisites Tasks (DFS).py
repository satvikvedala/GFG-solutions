class Solution:
    def isPossible(self,N,prerequisites):
        #code here
        def func(dd,visited,recStack,i):
            
            visited[i] = True
            recStack[i] = True
            for item in dd[i]:
                if visited[item] == False:
                    if func(dd,visited,recStack,item) == True:
                        return True
                else:
                    if recStack[item] == True:
                        return True
            recStack[i] = False
            return False
                    
        from collections import defaultdict
        dd = defaultdict(list)
        for item in prerequisites:
            x = item[1]
            y = item[0]
            dd[x].append(y)
        visited = [False]*N
        recStack = [False]*N
        for i in range(N):
            if visited[i] == False:
                if(func(dd,visited,recStack,i)):
                    return False
        return True
