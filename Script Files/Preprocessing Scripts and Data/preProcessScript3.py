users = {}
artists ={}
c=0
m=0
with open('user4.txt', 'r') as r:
	for line in r:
		print(c)
		c=c+1
		l = line.split("\t")
		u_id = l[0]
		a_id = l[1]
		if a_id in artists:
			artists[a_id]+=1
		else:
			artists[a_id]  = 1
	
		if u_id in users:
			users[u_id]+=1
		else:
			users[u_id]  = 1

print("users" + "   " + str(len(users)))
print("artists" + "   " + str(len(artists)))
with open('user5.txt', 'w') as w:
	with open('user4.txt', 'r') as r:
		for line in r:
			#print(m)
			m=m+1
			l = line.split("\t")
			u_id = l[0]
			a_id = l[1]
			if users[u_id]>400:
				if artists[a_id]>550:
					w.write(line)
