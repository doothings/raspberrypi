# Python script to display the latest scores
# Arun Kumar	@ArunMKumar
# Varun Gupta	varun90gupta@gmail.com
# Anish Tambe 	@atdaemon
# 01.06.2014


######################## Libraries ##############################
from __future__ import print_function, division, absolute_import, unicode_literals
from RPLCD import *
import httplib
import time
import re


####################### Constatnts #############################

teams = ["England", "India", "Sri Lanka", "West Indies", "Punjab T", "Chennai T", "Yorkshire", "Hampshire", "Surrey", "Sussex" ]
rows = {"time" : 0 , "team1" : 1 , "team2" : 2 , "player" : 3}
colm = {"teamname": 0 ,"score": 12, "time": 11}
namelen = 7
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
	return favs

def getMatchScore(matchId):
	Con =  httplib.HTTPConnection('cricscore-api.appspot.com')
	Con.request("GET", "/csa?id="+"+".join(map(str,matchId)))
	Response = Con.getresponse()
	return eval(Response.read())  ## Disputed

def getTeamNameandScores(status):
	Result = re.search("([a-zA-Z\ ]+).*([0-9]+\/[0-9]+)*[\ \*]*v([a-zA-Z\ ]+).*([0-9]+\/[0-9]+)*",status)
	names = [Result.group(1), Result.group(2), Result.group(3), Result.group(4)]
	return names

def displaytime():
	global display
	display.cursor_pos = (0,0)
	Current_Time =time.strftime("%d %b %y")
	display.write_string(Current_Time)
	display.cursor_pos = (rows['time'], colm['time'])
	Current_Time = time.strftime(" %H:%M:%S")
	display.write_string(Current_Time)


###############################################################################


initLCD()

#Get list of matches
matches = getMatchList()


#Get the Match ID
matchIds = getFavsIds(matches, teams)


#get the status for all matches
statuses = getMatchScore(matchIds)  # all scores
print(statuses)
# Display Scores

for status in statuses:
	
	nameAndScore = getTeamNameandScores(status['si'])

	display.clear()
	displaytime()

	if nameAndScore[0]:
		display.cursor_pos = (rows["team1"],colm['teamname'])
		display.write_string(nameAndScore[0].strip()[:namelen])

	if nameAndScore[1]:
                display.cursor_pos = (rows["team1"],colm['score'])
                display.write_string(nameAndScore[1].strip())

 	if nameAndScore[2]:
                display.cursor_pos = (rows["team2"],colm['teamname'])
                display.write_string(nameAndScore[2].strip()[:namelen])


 	if nameAndScore[3]:
                display.cursor_pos = (rows["team2"],colm['score'])
                display.write_string(nameAndScore[3].strip())
	
	time.sleep(60/len(matchIds))		# sleep accordingly
