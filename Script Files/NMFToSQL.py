import mysql.connector
from mysql.connector import errorcode

uname = "kolisett"
pwd = "A46610134"
hname = "mysql-user.cse.msu.edu"


try:
	cnx = mysql.connector.connect(user=uname, password=pwd, host=hname,database=uname)
	cursor = cnx.cursor()

	with open('NMFFinal.txt', 'r') as f:
		for line in f:
			l = line.split(',')
			name = l[0]
			u_id = l[1]
			a_1 = l[2]
			a_2 = l[3]
			a_3 = l[4]
			cursor.execute("""INSERT INTO ArtistRecommendation VALUES (%s,%s,%s,%s,%s)""",(name,u_id,a_1,a_2,a_3))
		
	cursor.close()
	cnx.commit()
	cnx.close()


except mysql.connector.Error as e:
	print(e.msg)



	
