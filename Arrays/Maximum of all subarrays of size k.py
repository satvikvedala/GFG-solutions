 #Using Deque  
        from collections import deque
        lis = []
        q = deque()
        for i in range(k):
            while q and arr[i]>=arr[q[-1]]:
                q.pop()
            q.append(i)
        for i in range(k,n):
            lis.append(arr[q[0]])
            while q and q[0]<=i-k:
                q.popleft()
            while q and arr[i]>arr[q[-1]]:
                q.pop()
            q.append(i)
        lis.append(arr[q[0]])
        return lis
