import time
ageOfUser = input('Date of nasissance (year-month-day-hour):')
localtime = time.localtime()
timeNow = time.strftime("%Y-%m-%d-%H", localtime)
timeNow = timeNow.split('-')
ageOfUser = ageOfUser.split('-')
for i in range(len(timeNow)):
    timeNow[i] = int(timeNow[i])
    ageOfUser[i] = int(ageOfUser[i])
years = (timeNow[0]-ageOfUser[0])*365*24
months = (timeNow[1]-ageOfUser[1])*30*24
days =  (timeNow[2]-ageOfUser[2])*24
ageWithHour = years + months + days
print('Bro you are in this live ',ageWithHour,'Hours, What that mean for you ?')