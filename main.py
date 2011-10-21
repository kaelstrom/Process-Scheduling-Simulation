# Nathan Black, Kyle Johnsen
# Op Sys Project 1
# Process Scheduling Simulation
# 10/20/11

from algoClass import algoClass
from process import Process
import random
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
    
    print("               Max        Min        Avg")
    print("Turnaround     %dms       %dms       %.3fms"
        %(max(turnarounds), min(turnarounds), float(sum(turnarounds))/len(turnarounds)))
    print("Initial Wait   %dms       %dms       %.3fms"
        %(max(initwaits), min(initwaits), float(sum(initwaits))/len(initwaits)))
    print("Total Wait     %dms       %dms       %.3fms"
        %(max(totwaits), min(totwaits), float(sum(totwaits))/len(totwaits)))

def makeProcs():
    global procs
    #all processes come in at time 0
    #procs = [Process(i, 0) for i in range(numProcs)]
    
    #75% of processes come in at random times
    procs = [Process(i, 0) for i in range(numProcs/4)] + [Process(i + numProcs/4, random.randint(100,2500)) for i in range(3*numProcs/4)]
    
    
makeProcs()
    
def runAlgo( algo, stats ):
    time[0] = 0
    print("Beginning a run of %s" % algo.type)
    algo.start()
    while( not algo.allDone() ):
        algo.run()
        algo.organizeProcs()
        algo.checkSwitch()
    outputStats(algo.stats)
    time[0] = 0
        

algoFCFS = algoClass("FCFS", procs, time, stats) 
runAlgo(algoFCFS, stats)
#algoSJF = algoClass("SJF", procs, time, stats)  
#runAlgo(algoSJF, stats)   
#algoPSJF = algoClass("PSJF", procs, time, stats) 
#runAlgo(algoPSJF, stats)    
#algoRR = algoClass("RR", procs, time, stats)   
#runAlgo(algoRR, stats)  
#algoPRI = algoClass("PRI", procs, time, stats)
#runAlgo(algoPRI, stats)


