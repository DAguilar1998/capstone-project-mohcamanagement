from ScheduledDate import *

class User:
	def __init__(self, user, cursor, startDict, endDict):
		self.userWeight = 0
		self.totalHours = 0
		self.hoursLeft = 0
		self.startDict = startDict
		self.endDict = endDict
		self.name = user[0]
		self.pin = user[1]
		self.userSchedule = {"Monday" : list(), 
							"Tuesday" : list(), 
							"Wednesday" : list(),
							"Thursday" : list(),
							"Friday" : list(),
							"Saturday" : list(),
							"Sunday" : list()}


		cursor.execute('SELECT Day, ShiftName FROM availability WHERE Pin = %s', (self.pin,))

		data = cursor.fetchall()

		for i in range(len(data)):
			if data[i][1] == None: self.userSchedule.get(data[i][0]).append("None")
			else: self.userSchedule.get(data[i][0]).append(data[i][1])

		print(self.userSchedule)

	def setUserWeight(self, weight):
		self.userWeight = weight

	def userScheduleAdd(self, element):
		self.userSchedule.append(element)

	def calculateTotalHoursRequested(self):
		for i in range(len(self.userSchedule)):
			for j in range(len(list(self.userSchedule.values())[i])):
				shift = list(self.userSchedule.values())[i][j]
				startTime = self.startDict.get(shift)
				endTime = self.endDict.get(shift)

				print(startTime)
				print(endTime)

	def calculateUserWeight(self):
		print("Implement function to calculate weight")

		

		calculatedWeight = 0
		self.setUserWEgith(calculatedWeight)