from ScheduledDate import *
from datetime import datetime
from Week import *

class User:
	def __init__(self, user, cursor, scheduleInfo):
		self.userWeight = 0
		self.totalRequestedHours = 0
		self.maxHoursPerWeek = 168
		self.startDict = scheduleInfo.getStartTimeDictionary()
		self.endDict = scheduleInfo.getEndTimeDictionary()
		self.name = user[0]
		self.pin = user[1]
		self.hoursAssigned = 0

		self.week = Week(scheduleInfo)

		self.userAvailability = {"Monday" : list(), 
							"Tuesday" : list(), 
							"Wednesday" : list(),
							"Thursday" : list(),
							"Friday" : list(),
							"Saturday" : list(),
							"Sunday" : list()}


		cursor.execute('SELECT Day, ShiftName FROM availability WHERE Pin = %s', (self.pin,))

		data = cursor.fetchall()

		for i in range(len(data)):
			if data[i][1] == None: self.userAvailability.get(data[i][0]).append("None")
			else: self.userAvailability.get(data[i][0]).append(data[i][1])

		self.calculateUserWeight()

	def setUserWeight(self, weight):
		self.userWeight = weight

	def userAvailabilityAdd(self, element):
		self.userAvailability.append(element)


	def calculateDaysWorking(self):
		daysAmount = 0
		for i in list(self.userAvailability.values()):
			if len(i) > 0: daysAmount += 1
		return daysAmount

	def calculateTotalHoursRequested(self):
		for i in range(len(self.userAvailability)):
			for j in range(len(list(self.userAvailability.values())[i])):
				shift = list(self.userAvailability.values())[i][j]
				startTime = self.startDict.get(shift)
				endTime = self.endDict.get(shift)
				# startTime+=":00"
				# endTime+=":00"
				# FMT='%H:%M:%S'
				# self.totalRequestedHours += String(datetime.strptime(endTime,FMT) - datetime.strptime(startTime,FMT))
				startHours,startMinutes = startTime.split(':', 1)
				#Start hour: 6:30
				#Splits into 6 & 30
				endHours, endMinutes = endTime.split(':', 1)

				self.totalRequestedHours += int(endHours)-int(startHours)
				tMinutes = int(endMinutes)-int(startMinutes)
				if(tMinutes<0):
				    self.totalRequestedHours-=0.5
				if(tMinutes>0):
				    self.totalRequestedHours+=0.5

				# (totalHours)
				#print(endTime)
		print("Total hours: " + str(self.totalRequestedHours))

	def getShiftLength(self, shift):
		startTime = self.startDict.get(shift)
		endTime = self.endDict.get(shift)

		startHours,startMinutes = startTime.split(':', 1)
		endHours, endMinutes = endTime.split(':', 1)

		tHours = int(endHours)-int(startHours)
		tMinutes = int(endMinutes)-int(startMinutes)

		return tHours, tMinutes

	def assignHours(self, hours):
		self.hoursAssigned += hours

	def getHoursAssigned(self):
		return self.hoursAssigned

	def calculateUserWeight(self):
		self.calculateTotalHoursRequested()
		#Weight = (M - R + M/R)(1-(T/R))
		#Weight = (maxHoursPerWeekWeek - RequestedHours + (maxHoursPerWeek/Requested)) * (1 - (TotalHoursCurrentlyAssigned/Requested))
		weight = (self.maxHoursPerWeek - self.totalRequestedHours + (self.maxHoursPerWeek/max(self.totalRequestedHours,1))) * (1 - (self.hoursAssigned/max(self.totalRequestedHours,1)))

		self.setUserWeight(weight)
		
		print(self.userWeight)

	def getUserWeight(self):
		return self.userWeight

	def getName(self):
		return self.name

	def getUserAvailability(self):
		return list(self.userAvailability.values())