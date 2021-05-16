    def relativeSort (self,A1, N, A2, M):
        # Your Code Here
        visited = [False]*N
        res = []
        for i in range(M):
            for j in range(N):
                if (A1[j] == A2[i]) and visited[j] == False:
                    res.append(A1[j])
                    visited[j] = True
        rem = []
        for j in range(N):
            if visited[j] == False:
                rem.append(A1[j])
        rem = sorted(rem)
        for item in rem:
            res.append(item)
        return res
