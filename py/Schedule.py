class Schedule:
    def __init__(self, users):
        self.users = users

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

        if daysAvailable <= 2:
            print("todo")

    #Determine if all users have a shift or if all days are set
    def stillAvailable(self):
        return True #Should not always return True

    def createSchedule(self):
        while self.stillAvailable():
            #Iterate through all users
            for i in self.users:
                self.judgeUserRequest(user)