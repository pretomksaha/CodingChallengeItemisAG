import math
import inputList
def timeSchedle(startTime,programtime,program,count):
    'Function that assign every program in time and print a copy'
    'Input:'
    'startTime: When the program will start.'
    'programtime: each program with duration time.'
    'count: represent normal program (1), lunch (2) and Networking Event (3)'
    'Output:'
    'updated starttime'
    'newprogramList: status of the program (done)'
    'updated count'
    newprogramList ='done'
    addTime = round((startTime - int(startTime)) * 100)
    programtime = programtime + addTime
    durationTime = math.ceil(programtime % 60)
    if durationTime == 0:
        endTime= int(startTime) + (programtime/60)
    else:
        endTime = int(startTime) + int(programtime/60) + round(durationTime/100, 2)
    if endTime <= 12:
        print(str(int(startTime)).zfill(2), ':', str(round((startTime - int(startTime)) * 100)).zfill(2), 'AM', ' ', program)
    elif 12 < endTime <= 13:
        endTime = 13
        if count == 1:
            print(12, ':','00', 'PM', ' ', 'Lunch')
            count=count+1
    elif 13 < endTime <= 17:
        print(str(int(startTime%12)).zfill(2), ':', str(round((startTime - int(startTime)) * 100)).zfill(2), 'PM', ' ', program)
    else:
        endTime = 17
        if count == 3:
            print('05', ':','00', 'PM', ' ', 'Networking Event')
            count=count+1
        newprogramList = program
    startTime = round(endTime, 2)
    return startTime, newprogramList, count

def progarmSchedule(programtime,starttime,count):
    'Function that spite the time from every line and call the function to creat schedule.'
    'Input:'
    'startTime: When the program will start.'
    'programtime: each program with duration time.'
    'count: represent normal program (1), lunch (2) and Networking Event (3)'
    'Output:'
    'updated starttime'
    'newprogramList: status of the program (done)'
    'updated count'

    schedule = []
    newprogramList ='done'
    timeTable = [word for word in programtime.split() if ('min' in word) or ('lightning' in word)]
    if ('min' in timeTable[0]):
        if len(timeTable[0]) <= 5:
            schedule.append(int(timeTable[0][:2]))
            starttime, newprogramList,count = timeSchedle(starttime, int(timeTable[0][:2]), programtime,count)
    else:
        schedule.append(5)
        starttime, newprogramList, count = timeSchedle(starttime, int(5), programtime, count)
    return starttime,newprogramList,count

def initialize():
    'function to Initialize the solution for conference track management problem.'
    print('\t\tProblem 2: CONFERENCE TRACK MANAGEMENT \n')
    track= 1 # track for everyday
    programList =inputList.initialize() # call the input function.
    while True:
        starttime = 9 # starting time for every track.
        count = 1
        newprogramList =[]
        print('Track', track)
        for item in programList:
            starttime,newprogram,count = progarmSchedule(item,starttime,count)
            if count == 2:
                starttime,newprogram,count = progarmSchedule(item,starttime,count)
                count = count +1
            if newprogram != 'done':
                newprogramList.append(newprogram)

        programList = newprogramList
        track = track +1
        print('\n')
        if len(programList) < 1:
            break