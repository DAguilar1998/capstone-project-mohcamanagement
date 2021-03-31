import mysql.connector
from User import *

def main():
	overseer = mysql.connector.connect(
		host="localhost",
		user="root",
		password="",
		database="overseer")


	cur = overseer.cursor()
	
	date = ScheduledDate(cur)

	cur.execute("SELECT * FROM users")


	userList = list()

	userData = cur.fetchone()
	while userData != None:
		if userData[2] == 0:
			userList.append(User(userData, cur, date.getStartTimeDictionary(), date.getEndTimeDictionary()))
		userData = cur.fetchone()



	userList[0].calculateTotalHoursRequested()



	overseer.close()


if __name__ == "__main__":
	main()