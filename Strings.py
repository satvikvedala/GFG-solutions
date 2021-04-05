#Implement Atoi   (a longer method)
  def atoi(self,string):
        # Code here
        try:
            res = 0
            if string[0] == '-':
                for i in range(1,len(string)):
                    res = res*10+int(string[i])
                return -1*res
            else:
                for i in range(len(string)):
                    res = res*10+int(string[i])
                return res
        except:
            return -1

#Implement Atoi   (a shorter method)
    def atoi(self,string):
        # Code here
        try:
            return int(string)
        except:
            return -1

#Multiply two strings
    def multiplyStrings(self,s1,s2):
        # code here
        # return the product string
        return int(s1)*int(s2)
      
      
#Validate an IP Address(not using REGEX)
  def isValid(s):
    #code here
    sarray = s.split('.')
    if len(sarray)<4 or len(sarray)>4:
        return False
    for item in sarray:
        if item == '':
            return False
        try:
            if int(item)>=0 and item[0] == '0' and len(item) != 1:
                return False
            if int(item)>255 or int(item)<0:
                return False
        except:
            return False
    return True
