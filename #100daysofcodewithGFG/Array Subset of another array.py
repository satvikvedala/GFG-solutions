def isSubset( a1, a2, n, m):
    set1 = set()
    
    for item in a1:
        set1.add(item)
    for item in a2:
        if item not in set1:
            return 'No'
    return 'Yes'
