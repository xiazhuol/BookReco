real_artist_names = {}
artist_conversions = {}
with open('artist_names_metadata.txt', 'r') as f:
	for line in f:
		artist_id = line[0:7]
		artist_name = line[8:]
	 	artist_name = artist_name.replace(' ', '-')
		artist_name=artist_name.strip()
		real_artist_names[artist_id] = artist_name

with open('our_artists.txt', 'r') as f:
	for line in f:
		l = line.split()
		big_id = l[0]
		small_id=l[1]
		artist_conversions[small_id] = big_id

with open('artist_conversions.csv', 'w') as w:
	with open('finalUserData.csv') as f:
			for line in f:
				l = line.split(',')
				u_id = l[0]
				og_a_id = l[1]
				rating = l[2]
				rating = rating.strip()
				a_id = artist_conversions[og_a_id]
				artistName = real_artist_names[a_id]
				toWrite = str(og_a_id)+","+str(artistName) + "\n"
				w.write(toWrite)
