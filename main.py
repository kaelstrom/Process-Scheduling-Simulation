# Nathan Black, Kyle Johnsen
# Op Sys Project 1
# Process Scheduling Simulation
# 10/20/11

from algoClass import algoClass
from process import Process
time = [0]
procs = []
numProcs = 20

#holds turnaround, initial wait, and total wait per process
stats = [[0, 0, 0] for i in range(numProcs)]

#outputs useful statistics about the algo
def outputStats(stats):
    turnarounds = [x[0] for x in stats]
    initwaits = [x[1] for x in stats]
    totwaits = [x[2] for x in stats]
    
    print("               Max    Min    Avg")
    print("Turnaround     %dms   %dms   %dms"
        %(max(turnarounds), min(turnarounds), sum(turnarounds)/len(turnarounds)))
    print("Initial Wait   %dms   %dms   %dms"
        %(max(initwaits), min(initwaits), sum(initwaits)/len(initwaits)))
    print("Total Wait     %dms   %dms   %dms"
        %(max(totwaits), min(totwaits), sum(totwaits)/len(totwaits)))

def makeProcs():
    global procs
    procs = [Process(i, 0) for i in range(numProcs)]
    
makeProcs()
    
def runAlgo( algo ):
    global stats
    time[0] = 0
    stats = [[0, 0, 0] for i in range(numProcs)]
    print("Beginning a run of %s" % algo.type)
    while( time[0] < 100000 ):
        algo.checkSwitch()
        algo.run()
    print(stats)
    outputStats(stats)
        

algoFCFS = algoClass("FCFS", procs, time, stats) 
runAlgo(algoFCFS)    
#algoSJF = algoClass("SJF", procs, time, stats)  
#runAlgo(algoSJF)   
#algoPSJF = algoClass("PSJF", procs, time, stats) 
#runAlgo(algoPSJF)    
#algoRR = algoClass("RR", procs, time, stats)   
#runAlgo(algoRR)  
#algoPRI = algoClass("PRI", procs, time, stats)
#runAlgo(algoPRI)


