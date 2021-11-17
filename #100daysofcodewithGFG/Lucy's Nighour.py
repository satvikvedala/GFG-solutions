class Solution:
    def Kclosest(self, arr, n, x, k):
        # Your code goes here
        dic = {}
        temp = x
        for i in range(n):
            dic[arr[i]] = abs(temp - arr[i])
        dic = sorted(dic.items(),key = lambda x: (x[1],x[0]))
        ans = []
        for item in dic:
            ans.append(item[0])
        return sorted(ans[:k])
