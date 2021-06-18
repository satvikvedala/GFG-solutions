def findSpecificPattern(Dict, pattern):
    #Code here
    res = []
    pattern_count = 0
    pmap = {}
    for i in range(len(pattern)):
        if pattern[i] not in pmap:
            pmap[pattern[i]]=i
        pattern_count = pattern_count+10**pmap[pattern[i]]
    for item in Dict:
        count = 0
        imap = {}
        for i in range(len(item)):
            if item[i] not in imap:
                imap[item[i]] = i
            count = count+10**imap[item[i]]
        if count == pattern_count:
            res.append(item)
    return res
