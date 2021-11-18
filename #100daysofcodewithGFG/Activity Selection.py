class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        
        # code here
        dic = []
        for i in range(n):
            dic.append((start[i],end[i]))
        dic = sorted(dic,key=lambda x: x[1])
        count = 1
        one = dic[0][0]
        two = dic[0][1]
        for i in range(1,n):
            try:
                temp0 = dic[i][0]
                temp1 = dic[i][1]
                if two<temp0:
                    count+=1
                    one = temp0
                    two = temp1
            except:
                print(i,n)
        return count
