import re
import random
from collections import defaultdict

#open a text file containing tumblr notes
fp = open("notes.txt")

#lists that contain the usernames of people who have liked, reblogged and said
reblogged_leest=[]
liked_leest=[]
said_leest=[]

#for every line in a file search if it contains a note with reblogged/liked/said
for line in fp.readlines():
    if re.search(" reblogged this from | liked this| said: ",line) != None:
        #split into a string containing the person's username as well as if it was reblogged/liked/said
        tumblr_note=re.split("(?<=[a-zA-Z0-9_])\ (reblogged this from|liked this|said: )", line)
        #add it into the relevant list
        if tumblr_note[1] == "reblogged this from":
            reblogged_leest.append(tumblr_note[0])
        elif tumblr_note[1] == "liked this":
            liked_leest.append(tumblr_note[0])
        elif tumblr_note[1] == "said: ":
            said_leest.append(tumblr_note[0])

#add weighting to a tumblr user based for random number generation         
LIKED_WEIGHTING=0.5
REBLOGGED_WEIGHTING=1.0
SAID_WEIGHTING=0.5

#dictionary of usernames and weighting
username_dict=defaultdict(int)
#add weighting to the username depending on wether they said, liked or reblogged
for leest in said_leest, liked_leest, reblogged_leest:
    for username in leest:
        if leest == said_leest:
            username_dict[username] += SAID_WEIGHTING
        if leest == liked_leest:
            username_dict[username] += LIKED_WEIGHTING
        if leest == reblogged_leest:
            username_dict[username] += REBLOGGED_WEIGHTING

#select a user
username= random.choices(list(username_dict.keys()), list(username_dict.values()), k=1)
#print the winrar
print(username)
#print the dictionary of usernames for troubleshooting purposes
print(username_dict)