class Solution:

    def findMaxGuests(self, Entry, Exit, N):
        # code here
        Entry = sorted(Entry)
        Exit = sorted(Exit)
        
        item = Entry[0]
        count = 1
        ma = 1
        
        i = 1
        j = 0
        
        while i<N and j<N:
            if Entry[i]<=Exit[j]:
                count+=1
                i+=1
            elif Entry[i]>Exit[j]:
                count-=1
                j+=1
            if count>ma:
                ma = count
                item = Entry[i-1]
        return [ma,item]
