        def func(N,arr,index,curr_sum,rem_sum):
            if (curr_sum>rem_sum) or (index>=N):
                return False
            if curr_sum == rem_sum:
                return True
            return func(N,arr,index+1,curr_sum + arr[index],rem_sum) or func(N,arr,index+1,curr_sum,rem_sum) 
        rem_sum = sum(arr)
        if rem_sum%2!=0:
            return False
        return func(N,arr,0,0,rem_sum//2)
