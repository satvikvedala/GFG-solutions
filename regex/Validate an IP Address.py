def isValid(s):
    #code here
    import re
    string1 = "^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}"+"([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
    
    if(re.match(string1,s)):
        return 1
    return 0
