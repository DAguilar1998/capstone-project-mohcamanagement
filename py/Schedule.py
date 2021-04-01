from Week import *
class Schedule:
    def __init__(self, users, scheduleInfo):
        self.users = users
        self.finalizedWeek = Week(scheduleInfo)

    def sortUserArray(self, userArray):
        userArray.sort(key=cmp_to_key(compareByWeight), reverse=True)
	
    def compareByWeight(self, a, b):
        if (a.getUserWeight() < b.getUserWeight()):
            return -1
        if (a.getUserWeight() > b.getUserWeight()):
            return 1
        return 0

    #Prints the schedule
    def printSchedule(self):
        print("Todo")

    #Assigns a user to a shift
    def assignUserToShift(self):
        print("Todo")

    #In case of backtrack purposes
    def removeUserFromShift(self):
        print("Todo")

    #Judges a user's request to work that day
    def judgeUserRequest(self, user):
        daysAvailable = user.calculateDaysWorking()
        
        if daysAvailable != 0:
            userAvailability = user.getUserAvailability()



    #Determine if all users have a shift or if all days are set
    def stillAvailable(self):
        return True #Should not always return True

    def createSchedule(self):
        while self.stillAvailable():
            #Iterate through all users
            for i in self.users:
                self.judgeUserRequest(user)