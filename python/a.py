import requests
def getseason(mon):
    winter = ['dec','jan','feb']
    spring = ['mar', 'apr', 'may']
    summer = ['jun', 'jul', 'aug']
    fall   = ['sep', 'oct', 'nov']

    if mon.lower() in winter:
        season = 'winter'
        return season
    elif mon.lower() in spring:
        season = 'spring'
        return season
    elif mon.lower() in summer:
        season = 'summer'
        return season
    elif mon.lower() in fall:
        season = 'fall'
        return season


month=raw_input("Enter the season:\n")
month_count=len(month)
print month_count
if(month_count == 3):
    season=getseason(month)
    print("The season is " + season)
else:
        print "Month not found"
