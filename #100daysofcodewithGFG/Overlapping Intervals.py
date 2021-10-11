class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
		Intervals = sorted(Intervals,key = lambda x:x[0])
        arr = []
        temp = Intervals[0]
        for i in range(1,len(Intervals)):
            if temp[1]>=Intervals[i][0]:
                temp[0] = min(temp[0],Intervals[i][0])
                temp[1] = max(temp[1],Intervals[i][1])
            else:
                arr.append(temp)
                temp = Intervals[i]
        arr.append(temp)
        return arr
