#Implement Atoi    
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