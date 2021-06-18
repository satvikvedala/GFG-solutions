tc = int(input())
for _ in range(tc):
    string = input()
    copy = string.lower()
    ans = ''
    map1 = {}
    for i in range(len(copy)):
        if copy[i] not in map1:
            map1[copy[i]] = 1
            ans=ans+string[i]
        else:
            map1[copy[i]]+=1
            if map1[copy[i]]%2!=0:
                ans = ans+string[i]
    print(ans)
