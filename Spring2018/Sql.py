# This script creates a SQLite db and does a basic query for it. Some initial code for accessing RateMyProfessor.
# Zachary Rubin, zrubin@rtc.edu
# CNA 336 Spring 2018
import sqlite3
import time
sqlite_file = "foo.db"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS Ratings(ID INT PRIMARY KEY AUTOINCREMENT, "
          "Prof_Name TEXT, Overall_Quality FLOAT, Level_Difficulty FLOAT, Date DATE)")
#c.execute("INSERT INTO Ratings(Prof_Name, Overall_Quality, Level_Difficulty, Date) "
#                "VALUES(?, ?, ?, ?)", ("McCormick", 5.0, 4.0, '2016-05-19'))
# 2016-05-19
counter = 0

#for i in range(1, 210):
#
#    query = "http://www.ratemyprofessors.com/filter/professor/?department=&institution=California+State+University%2C+Northridge&page=" + str(
#        i) + "&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=163"
#
#    try:
#        page = requests.get(query)
#        jsonpage = json.loads(page.content)
#        professorlist = jsonpage['professors']

#        if len(professorlist) > 0:
#            for prof in professorlist:
#                if db.find_one({"tid": int(prof['tid'])}) is None:
#                    db.insert(prof)
#        print
#        "page " + str(i) + " " + '\xF0\x9F\x98\x8F'
#    except:
#        pass

#    time.sleep(1)

c.execute("SELECT * FROM Ratings")
rows = c.fetchall()
for row in rows:
    print(row)
#conn.commit()


conn.close()

