class mlops: 
    def __init__ (self, totalstudents): 
        self.totalstudents  = totalstudents
        
    def gettotalstudents(self): 
        return self.totalstudents
    
    def Addstudent(self): self.totalstudents = self.totalstudents + 1
    
    def removestudent(self): self.totalstudents = self.totalstudents - 1
    
    def getclassname(Self): return "MLOPS B"