Class day:
    def __self__(self, shifts=(0,0,0)):
        self.shifts=shifts
    
    def getShift():
        return self.shifts
        
    def setShift(sNum):
        if(sNum==1):
            shifts[0]=1
        elif(sNum==2):
            shifts[1]=1
        elif(sNum==3):
            shifts[2]=1
        else:
            print("error")
    def rmvShift(sNum):
        if(sNum==1):
            shifts[0]=0
        elif(sNum==2):
            shifts[1]=0
        elif(sNum==3):
            shifts[2]=0
        else:
            print("error")