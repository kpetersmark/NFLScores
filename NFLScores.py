# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 09:29:17 2018

@author: Kyle
"""

import requests
from bs4 import BeautifulSoup
import csv


#Open CSV file to start writing
File = open("NFL Scores 1966 thru 2017.csv", "w", newline='')     


# create list for scores
scores = []
headers = ["Year","Week", "GameID","Team Home Abbrev", "Team Home Name", " Team Home Score", "Team Away Abbrev", "Team Away Name", "Team Away Score"]
scores.append(headers)


for year in range(1966,2018):
    for week in range(1,18):


    
        #specify the URL
        URL = 'http://www.nfl.com/ajax/scorestrip?season={}&seasonType=REG&week={}'.format(year,week)
                    
        #Get url from requests
        request = requests.get(URL)
        content = request.content
            
        # parse the html using beautiful soap and store in variable `soup`
            
        soup = BeautifulSoup(content, "lxml")
            
        
            
        # Find all Scores
            
        Table = soup.find_all("g")
        
        for Game in Table:
            GameID = Game["eid"]
            TeamHomeAbbrev = Game["h"]
            TeamHomeName = Game["hnn"]
            TeamHomeScore = Game["hs"]
            TeamAwayAbbrev = Game["v"]
            TeamAwayName = Game["vnn"]
            TeamAwayScore = Game["vs"]
         
            LineScore = [year, week, GameID, TeamHomeAbbrev, TeamHomeName, TeamHomeScore, TeamAwayAbbrev, TeamAwayName, TeamAwayScore]
            scores.append(LineScore)
            
            print(year, week, GameID, TeamHomeAbbrev, TeamHomeName, TeamHomeScore, TeamAwayAbbrev, TeamAwayName, TeamAwayScore)
            
            
  #Write arrays to CSV file        
with File:
    writer = csv.writer(File)
    writer.writerows(scores)

            
            