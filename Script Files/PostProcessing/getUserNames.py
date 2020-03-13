names=[]
with open("Names.txt", "r") as r:
	for line in r:
		l = line.split()
		name = l[0].strip()
		names.append(name)

with open("NMFFinal.txt", "w") as w:
	count =0
	with open("NMF.txt", "r") as r:
		for line in r:
			 n=names[count]
			 count=count+1
			 main = n + ","+line
			 w.write(main)
