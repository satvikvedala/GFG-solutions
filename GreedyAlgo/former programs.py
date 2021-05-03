#Max length chain
def maxChainLen(Parr, n):
    # Parr:  list of pair
    #code here
    li = []
    for item in Parr:
        temp = []
        temp.append(item.a)
        temp.append(item.b)
        li.append(temp)
    li = sorted(li,key = lambda x:x[1])
    count = 1
    temp = li[0][1]
    for i in range(1,len(li)):
        if li[i][0]>temp:
            count+=1
            temp = li[i][1]
    return count
  #Activity Selection
  def maximumActivities(n,start,end):
    '''
    :param n: number of activities
    :param start: start time of activities
    :param end: corresponding end time of activities
    :return: Integer, maximum number of activities
    '''
    # code here
    li = []
    for i in range(len(start)):
        li.append([start[i],end[i]])
    li = sorted(li,key = lambda x:x[1])
    count = 1
    temp = li[0][1]
    for i in range(1,len(li)):
        if li[i][0]>=temp:
            count+=1
            temp = li[i][1]
    return count
