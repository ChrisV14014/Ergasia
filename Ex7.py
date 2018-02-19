from datetime import *
datenow=datetime.today()
yearnow=datenow.year
daynow=datenow.day
weekdaynow=datenow.weekday()
print (datenow)
counter=0
for i in range(1,11):
    year=yearnow + i
    for j in range (1,13):
        day=date(year,j,daynow)
        day=day.weekday()
        if day==weekdaynow :
            counter+=1
print (counter)


