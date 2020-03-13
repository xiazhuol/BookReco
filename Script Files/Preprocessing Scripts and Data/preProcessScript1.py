from collections import defaultdict
users = defaultdict(int)
artists = defaultdict(int)
user_keep = defaultdict(list)
artist_keep = defaultdict(list)

m=0
r1_set = open("artist_ratings.txt", "r")
for line in r1_set:
    print(m)
    m=m+1
    temp_list = line.strip().split('\t')
    if (len(temp_list)) == 3:
        users[temp_list[0]] += 1
        artists[temp_list[1]] += 1
        user_keep[temp_list[0]].append(line)
        artist_keep[temp_list[1]].append(line)

file1 = open("user1.txt", "w")
for key in users:
    if users[key] > 500:
        for x in user_keep[key]:
            file1.write(x)
file1.close()

file2 = open("artist1.txt", "w")
for key2 in artists:
    if artists[key2] > 1000:
        for y in artist_keep[key2]:
            file2.write(y)
file2.close()

