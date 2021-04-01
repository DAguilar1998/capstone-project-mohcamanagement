from Day import *
class Week:
    def __init__(self, scheduleInfo):
        self.currentWeek = [Day(scheduleInfo)] * 7
        
    def getDay(self, day):
        return self.currentWeek[day]
          