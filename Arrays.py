  #Missing number in array
  def MissingNumber(array,n):
    # code here
    return (n*(n+1)//2) - sum(array)
  #MergeSort  
  def merge(self,arr, l, m, r): 
        # code here
        n1 = m-l+1
        n2 = r-m
        
        L = [0]*n1
        R = [0]*n2
        
        for i in range(n1):
            L[i] = arr[l+i]
        for i in range(n2):
            R[i] = arr[m+1+i]
        
        i = 0
        j = 0
        k = l
        while i<n1 and j<n2:
            if L[i]<=R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i<n1:
            arr[k] = L[i]
            i+=1
            k+=1
        while j<n2:
            arr[k] = R[j]
            j+=1
            k+=1
    def mergeSort(self,arr, l, r):
        #code here
        if l<r:
            mid = (l+r)//2
            
            self.mergeSort(arr,l,mid)
            self.mergeSort(arr,mid+1,r)
            self.merge(arr,l,mid,r)

            
#Stock Buy and Sell
	def stockBuySell(self, A, n):
		#code here
		i = 0
		res = []
		while i<n-1:
		    while i<n-1 and A[i+1]<=A[i]:
		        i+=1
		    if i==n-1:
		        break
		    buy = i
		    i = i+1
		    while i<n and A[i]>=A[i-1]:
		        i+=1
		    sell = i-1
		    res.append((buy,sell))
		return res
#Minimum Swaps to Sort
	def minSwaps(self, nums):
		#Code here
		arr = nums.copy()
		nums = sorted(nums)
		temp = [-1]*(max(nums)+1)
		for i in range(len(arr)):
		    temp[arr[i]] = i
		count = 0
		for i in range(len(arr)):
		    if arr[i]!=nums[i]:
		        x = temp[arr[i]]
		        y = temp[nums[i]]
		        arr[x],arr[y] = arr[y],arr[x]
		        temp[arr[y]] = y
		        temp[arr[x]] = x
		        count+=1
		return count

	
#Count Inversions using MERGE SORT
    def inversionCount(self, arr, n):
        # Your Code Here
        def func(arr,n,l,mid,r):
            m = mid-l+1
            n = r-mid
            count = 0
            L = [0]*m
            R = [0]*n
            for i in range(m):
                L[i] = arr[l+i]
            for j in range(n):
                R[j] = arr[mid+1+j]
            
            i = 0
            j = 0
            k = l
            while i<m and j<n:
                if L[i]<=R[j]:
                    arr[k] = L[i]
                    i+=1
                else:
                    arr[k] = R[j]
                    print(mid,i,l)
                    count += (mid-i+1-l)
                    print(count)
                    j+=1
                k+=1
            while i<m:
                arr[k] = L[i]
                k+=1
                i+=1
            while j<n:
                arr[k] = R[j]
                k+=1
                j+=1
            return count
        def merge(arr,n,l,r):
            count = 0
            if l<r:
                mid = (l+(r-1))//2
                count+=merge(arr,n,l,mid)
                count+=merge(arr,n,mid+1,r)
                count+=func(arr,n,l,mid,r)
            return count
        return merge(arr,n,0,n-1)

#Search in a row-column sorted Matrix
    def search(self,matrix, n, m, x): 
    	# code here 
    	i = 0
    	while i<n:
    	    if matrix[i][-1]>=x and matrix[i][0]<=x:
    	        if x in matrix[i]:
    	            return True
    	    i+=1
    	return False
