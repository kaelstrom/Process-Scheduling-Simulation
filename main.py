# Nathan Black, Kyle Johnsen
# Op Sys Project 1
# Process Scheduling Simulation
# 10/20/11

from algoClass import algoClass
from process import Process
time = [0]
procs = []
numProcs = 20
stats = [[0, 0, 0] for i in range(numProcs)]

def makeProcs():
    global procs
    procs = [Process(i, 0) for i in range(numProcs)]
    
makeProcs()
    

def runAlgo( algo ):
    time[0] = 0
    stats = [[0, 0, 0] for i in range(numProcs)]
    print("Beginning a run of %s" % algo.type)
    while( time[0] < 100000 ):
        algo.checkSwitch()
        algo.run()
        
        

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


