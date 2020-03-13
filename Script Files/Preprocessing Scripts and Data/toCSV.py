new_users={}
count_user = 1

new_artists={}
count_artist = 1
k = 0


with open('finalUserData.csv', 'w') as w:
	with open('user4.txt', 'r') as r:
		for line in r:
			l = line.split("\t")
			u_id = l[0]
			a_id = l[1]
			rating = l[2]
			if u_id in new_users:
				pass
			else:
				new_users[u_id] = count_user
				count_user = count_user+1
			
			if a_id in new_artists:
				pass
			else:
				new_artists[a_id] = count_artist
				count_artist = count_artist+1
	print(len(new_users))
	print(len(new_artists))		
	with open('user4.txt', 'r') as r:
		for line in r:	
			l = line.split("\t")
			u_id = new_users[l[0]]
			a_id = new_artists[l[1]]
			rating = l[2]		
			toWrite = str(u_id)+","+str(a_id)+","+str(rating)
			w.write(toWrite)
			

with open('our_users.txt', 'w') as w:
	with open('our_artists.txt', 'w') as l:
		for x in new_users:
			w.write(str(x)+"\t" + str(new_users[x]) + "\n")
			
		for x in new_artists:
			l.write(str(x)+"\t" + str(new_artists[x])+ "\n")
			
	

   
