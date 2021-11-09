class Solution:
    def RulingPair(self, arr, n): 
    	# Your code goes here
    	def func(item):
    	    su = 0
    	    while item>0:
    	        rem = item%10
    	        su+=rem
    	        item = item//10
    	    return su
    	       
    	from collections import defaultdict
    	dic = defaultdict(list)
    	for item in arr:
    	    ans = func(item)
    	    if len(dic[ans]) < 2:
    	        dic[ans].append(item)
    	    else:
    	        if item>dic[ans][0] and item>dic[ans][1]:
    	            second = max(dic[ans][0],dic[ans][1])
    	            dic[ans][0] = item
    	            dic[ans][1] = second
    	        elif item>dic[ans][0]:
    	            dic[ans][0] = item
    	        elif item>dic[ans][1]:
    	            dic[ans][1] = item
    	ma = -1
    	for k,v in dic.items():
    	    if len(v) == 2:
    	        one = v[0]
    	        two = v[1]
    	        ma = max(ma,one+two)
    	return ma
