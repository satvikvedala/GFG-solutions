class Solution:
    def sort012(self,arr,n):
        # code here
        count_0 =0
        count_1 = 0
        count_2 = 0
        for i in range(n):
            if arr[i] == 0:
                count_0+=1
            elif arr[i] == 1:
                count_1+=1
            else:
                count_2+=1
        i = 0
        count = 0
        while i<count+count_0:
            arr[i] = 0
            i+=1
        count+=count_0
        while i<count+count_1:
            arr[i] = 1
            i+=1
        count+=count_1
        while i<count+count_2:
            arr[i] = 2
            i+=1
