reblogged_leest=[]
liked_leest=[]
fp = open("notes.txt")
for line in fp.readlines():
    if line.find(" reblogged this from ")!=-1:
        username=line.split()[0]
        reblogged_leest.append(username)
    if line.find(" liked this")!=-1:
        username=line.split()[0]
        liked_leest.append(username)


for leest in reblogged_leest, liked_leest:
    if leest == reblogged_leest:
        print("REBLOGGGED ----- ")
    else:
        print("LIKED ----- ")
    for name in leest:
        print(name)
    print()


