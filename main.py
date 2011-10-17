from algoClass import algoClass
from process import Process
time = 0
procs = []
algoFCFS = algo("FCFS", time)     
algoFCFS = algo("SJF", time)     
algoFCFS = algo("PSJF", time)     
algoFCFS = algo("RR", time)     
algoFCFS = algo("Pri", time)

def makeProcs():
    pass

def runAlgo( algo ):
    global time
    time = 0
    while( time < 100000 ):
        algo.checkSwitch()
        algo.run()
        

        
        
        

        
     
runAlgo(algoFCFS)


