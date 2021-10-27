class Solution:

    def convert(self, Str, n):
        # code here
        if n == 1:
            return Str
        arr = ['']*n
        arr[0]+=Str[0]
        i = 1
        j = 1
        state = 'one'
        for k in range(1,len(Str)):
            if state == 'one':
                arr[i]+=Str[k]
                i+=1
                if i == n:
                    i = i-2
                    state = 'two'
            elif state == 'two' and j<len(Str):
                arr[i]+=Str[k]
                i-=1
                if i == -1:
                    i = i+2
                    state = 'one'
            j+=1
        ans = ''
        for item in arr:
            ans+=item
        return ans
