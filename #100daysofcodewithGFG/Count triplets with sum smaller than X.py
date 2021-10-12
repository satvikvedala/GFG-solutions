class Solution:
    def countTriplets(self, arr, n, sumo):
        #code here
        def func(arr,temp,i):
            x = 0
            y = i-1
            result = 0
            while (x<y):
                if (arr[x]+arr[y])<temp:
                    result+=y-x
                    x+=1
                else:
                    y-=1
            return result
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                if arr[j]<arr[i]:
                    arr[i],arr[j] = arr[j],arr[i]
        i = n-1
        while(i>0):
            temp = sumo - arr[i]
            count+=func(arr,temp,i)
            i-=1
        return count
