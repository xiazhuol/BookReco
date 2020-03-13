artists ={}

c=0
with open('user1.txt', 'r') as r:
	for line in r:
		print(c)
		c=c+1
		l = line.split("\t")

		a_id = l[1]
		if a_id in artists:
			artists[a_id][0]+=1
			artists[a_id][1].append(line)
		else:
			temp = [1]
			rating_temp = []
			rating_temp.append(line)
			temp.append(rating_temp)
			artists[a_id]  = temp

	
with open('user2.txt', 'w') as w:
	for x in artists:
		if artists[x][0] >= 1750:
			for y in artists[x][1]:
				w.write(y)

