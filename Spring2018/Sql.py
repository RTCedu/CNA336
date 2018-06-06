# This script creates a SQLite db and does a basic query for it. Some initial code for accessing RateMyProfessor.
# Zachary Rubin, zrubin@rtc.edu
# CNA 336 Spring 2018
import sqlite3
import time
import os
import urllib.request
import json
sqlite_file = "foo.db"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS Ratings(ID INT PRIMARY KEY AUTOINCREMENT, "
          "Prof_Name TEXT, Overall_Quality FLOAT, Level_Difficulty FLOAT, Date DATE)")
#c.execute("INSERT INTO Ratings(Prof_Name, Overall_Quality, Level_Difficulty, Date) "
#                "VALUES(?, ?, ?, ?)", ("McCormick", 5.0, 4.0, '2016-05-19'))
# 2016-05-19
counter = 0

query = "https://data.seattle.gov/api/views/cf52-s8er/rows.json?accessType=DOWNLOAD"
jsonpage = 0
try:
    contents = urllib.request.urlopen(query)
    response = contents.read()
    jsonpage = json.loads(response)

except:
    pass
    time.sleep(1)

#print(jsonpage)
data = json.dumps(jsonpage['data'])

for x in data:
    print(x)
#conn.commit()


conn.close()

