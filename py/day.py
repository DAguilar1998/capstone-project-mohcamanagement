class Day:
    def __init__(self, scheduleInfo):
        self.scheduleInfo = scheduleInfo
        self.shifts = [0] * self.scheduleInfo.getShiftAmount()
    
    def getShift(self):
        return self.shifts
        
    def setShift(self, shift):
        shiftIndex = self.scheduleInfo.shiftStringToIndex(shift)
        self.shifts[shiftIndex] = 1

    def removeShift(self, shift):
        shiftIndex = self.scheduleInfo.shiftStringToIndex(shift)
        self.shifts[shiftIndex] = 0
