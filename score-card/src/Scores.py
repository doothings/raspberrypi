# Python script to display the latest scores
# Arun Kumar, Varun Gupta 
# 01.06.2014


######################## Libraries ##############################
from __future__ import print_function, division, absolute_import, unicode_literals
from RPLCD import *
import httplib
import json



####################### Constatnts #############################

teams = ["England", "India", "Sri Lanka", "West Indies"]
rows = ["timeRow" : 0 , "team1Row" : 1 , "team2Row" : 2 , "playerRow" : 3]


###################### functions ##############################

def initLCD():
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

def getTeamName(names):
	


def getTeamScores(scores):

###############################################################################


initLCD()

#Get list of matches
matches = getMatchList()

#Get the Match ID
matchIds = getFavsIds(matches, teams)

#get the score for all matches
scores = getMatchScore(matchIds)  # all scores

# Display Scores

for score in scores:
	team_names  = getTeamName(score['si'])
	team_scores = getTeamScores(score['si'])












#favs = getFavsIds(matches,teams)


#score = getMatchScore(str(favs[0]))
#l = eval(score)
#text = l[0]['si']
#index = text.find(" v ")


display.cursor_pos = (1,0)
display.write_string(text[:index])
display.cursor_pos = (2,0)
display.write_string(text[index+3:])
print(text)

#display.write_string(text)

