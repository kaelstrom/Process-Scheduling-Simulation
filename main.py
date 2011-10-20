# Nathan Black, Kyle Johnsen
# Op Sys Project 1
# Process Scheduling Simulation
# 10/20/11

from algoClass import algoClass
from process import Process
time = [0]
procs = []

def makeProcs():
    global procs
    procs = [Process(i, 0) for i in range(20)]
    
makeProcs()
    
algoFCFS = algoClass("FCFS", procs, time)     
algoSJF = algoClass("SJF", procs, time)     
algoPSJF = algoClass("PSJF", procs, time)     
algoRR = algoClass("RR", procs, time)     
algoPRI = algoClass("PRI", procs, time)

def runAlgo( algo ):
    time[0] = 0
    print("Beginning a run of %s" % algo.type)
    while( time[0] < 100000 ):
        algo.checkSwitch()
        algo.run()
        
runAlgo(algoFCFS)
runAlgo(algoSJF)
runAlgo(algoPSJF)
runAlgo(algoRR)
runAlgo(algoPRI)


