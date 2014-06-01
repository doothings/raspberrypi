# Python script to display the latest scores
# Arun Kumar, Varun Gupta 
# 01.06.2014


######################## Libraries ##############################
from __future__ import print_function, division, absolute_import, unicode_literals
from RPLCD import *
import httplib
import time
import re


####################### Constatnts #############################

teams = ["England", "India", "Sri Lanka", "West Indies", "Punjab T", "Chennai T"]
rows = {"time" : 0 , "team1" : 1 , "team2" : 2 , "player" : 3}


###################### functions ##############################

display = None

def initLCD():
	global display
	display =CharLCD()
	display.clear()
	display.cursor_mode = CursorMode.blink


def getMatchList():
	Con =  httplib.HTTPConnection('cricscore-api.appspot.com')
	Con.request("GET", "/csa")
	Response = Con.getresponse()
	return eval(Response.read()) ## Disputed

 
def getFavsIds(matchesList,favTeams) :
	favs = []
	for match in matchesList :
		if match['t1'] in favTeams or match['t2'] in favTeams :
			favs.append(match['id'])
	print(favs)
	return favs

def getMatchScore(matchId):
	Con =  httplib.HTTPConnection('cricscore-api.appspot.com')
	Con.request("GET", "/csa?id="+"+".join(map(str,matchId)))
	Response = Con.getresponse()
	return eval(Response.read())  ## Disputed

def getTeamNameandScores(status):
	#print(status)
	#Result = re.search("([a-zA-Z\ ]+)([0-9]+\/[0-9]+)[\ \*]*v([a-zA-Z\ ]+)([0-9]+\/[0-9]+)",status)
	#names = [Result.group(1), Result.group(2), Result.group(3), Result.group(4)]
	names = status.split(" v ");
	return names


###############################################################################


initLCD()

#Get list of matches
matches = getMatchList()

print(matches)
#Get the Match ID
matchIds = getFavsIds(matches, teams)

print(matchIds)

#get the status for all matches
statuses = getMatchScore(matchIds)  # all scores

# Display Scores

for status in statuses:
	
	s = getTeamNameandScores(status['si'])
	#display
	#display.clear()
	
	display.cursor_pos = (rows["team1"],0)
	display.write_string(s[0])
	#display.cursor_pos = (rows["team1"], 14)
	#display.write_string(s[1])

	display.cursor_pos = (rows["team2"],0)
	display.write_string(s[1])
	#display.cursor_pos = (rows["team2"], 14)
	#display.write_string(s[3])

	#time.sleep(60/ len(statuses))
	print("hello")


display.cursor_pos = (rows["time"],0)
Current_Time =time.strftime("%d %b %y")
display.write_string(Current_Time)


display.cursor_pos = (rows["time"],11)
Current_Time = time.strftime(" %H:%M:%S")
display.write_string(Current_Time)

	













#favs = getFavsIds(matches,teams)


#score = getMatchScore(str(favs[0]))
#l = eval(score)
#text = l[0]['si']
#index = text.find(" v ")


#display.cursor_pos = (1,0)
#display.write_string(text[:index])
#display.cursor_pos = (2,0)
#display.write_string(text[index+3:])
#print(text)

#display.write_string(text)

