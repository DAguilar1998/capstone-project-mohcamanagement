from ScheduledDate import *
from datetime import datetime
from Week import *

class User:
	def __init__(self, user, cursor, scheduleInfo):
		self.userWeight = 0
		self.totalHours = 0
		self.hoursLeft = 20	
		self.startDict = scheduleInfo.getStartTimeDictionary()
		self.endDict = scheduleInfo.getEndTimeDictionary()
		self.name = user[0]
		self.pin = user[1]

		self.week = Week(scheduleInfo)

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

		self.calculateUserWeight()

	def setUserWeight(self, weight):
		self.userWeight = weight

	def userScheduleAdd(self, element):
		self.userSchedule.append(element)


	def calculateDaysWorking(self):
		daysAmount = 0
		for i in list(self.userSchedule.values()):
			if len(i) > 0: daysAmount += 1
		return daysAmount


	def calculateTotalHoursRequested(self):
		for i in range(len(self.userSchedule)):
			for j in range(len(list(self.userSchedule.values())[i])):
				shift = list(self.userSchedule.values())[i][j]
				startTime = self.startDict.get(shift)
				endTime = self.endDict.get(shift)
				# startTime+=":00"
				# endTime+=":00"
				# FMT='%H:%M:%S'
				# self.totalHours += String(datetime.strptime(endTime,FMT) - datetime.strptime(startTime,FMT))
				startHours,startMinutes = startTime.split(':', 1)
				#Start hour: 6:30
				#Splits into 6 & 30
				endHours, endMinutes = endTime.split(':', 1)

				self.totalHours += int(endHours)-int(startHours)
				tMinutes = int(endMinutes)-int(startMinutes)
				if(tMinutes<0):
				    self.totalHours-=0.5
				if(tMinutes>0):
				    self.totalHours+=0.5

				# (totalHours)
				#print(endTime)
		print("Total hours: " + str(self.totalHours))

	def calculateUserWeight(self):
		self.calculateTotalHoursRequested()
		self.setUserWeight(self.totalHours - self.hoursLeft)
		print("Amount of days working: " + str(self.calculateDaysWorking()))
		print(self.userWeight)

	def getUserWeight(self):
		return self.userWeight

	def getName(self):
		return self.name