import mysql.connector
from User import *
from Schedule import *



def main():
	overseer = mysql.connector.connect(
		host="localhost",
		user="root",
		password="",
		database="overseer")


	cur = overseer.cursor(buffered=True)
	
	date = ScheduledDate(cur)

	cur.execute("SELECT * FROM users")


	userList = list()

	userRows = cur.fetchall()
	for userData in userRows:

		if userData[2] == 0:
			userList.append(User(userData, cur, date))
		userData = cur.fetchone()
	userList.sort(compareByWeight)

		if userData[2] == 0: userList.append(User(userData, cur, date))


	workSchedule = Schedule(userList)

	overseer.close()

    
def sortUserArray(userArray):
	userArray.sort(compareByWeight)
	
def compareByWeight(a, b):
    if (a.getUserWeight < b.getUserWeight):
        return -1
    if (a.getUserWeight > b.getUserWeight):
        return 1
    return 0
    

if __name__ == "__main__":
	main()