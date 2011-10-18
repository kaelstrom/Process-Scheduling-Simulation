from algoClass import algoClass
from process import Process
time = 0
procs = []

def makeProcs():
    procs = [Process(i, 0) for i in range(20)]
    
algoFCFS = algoClass("FCFS", procs)     
algoSJF = algoClass("SJF", procs)     
algoPSJF = algoClass("PSJF", procs)     
algoRR = algoClass("RR", procs)     
algoPRI = algoClass("PRI", procs)

def runAlgo( algo ):
    global time
    time = 0
    while( time < 100000 ):
        algo.checkSwitch()
        algo.run()
        
runAlgo(algoFCFS)


