reblogged_leest=[]
liked_leest=[]
said_leest=[]
fp = open("notes2.txt")
for line in fp.readlines():
    if line.find(" reblogged this from ")!=-1:
        username=line.split()[0]
        reblogged_leest.append(username)
    if line.find(" liked this")!=-1:
        username=line.split()[0]
        liked_leest.append(username)
    if line.find(" said: ")!=-1:
        username=line.split()[0]
        said_leest.append(username)

for leest in reblogged_leest, liked_leest, said_leest:
    if leest == reblogged_leest:
        print("REBLOGGGED ----- ")
    elif leest == liked_leest:
        print("LIKED ----- ")
    else:
        print("SAID ----- ")
    for name in leest:
        print(name)
    print()