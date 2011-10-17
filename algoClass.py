class algoClass()
    def __init__(self, type, procList):
        self.type = type
        self.inMemProcs = []
        self.time = 0
        self.toAddProcs = procList
        
        
    #runs the current process in cpu
    def run(self):
        #if new to CPU, output so
        if self.currentProc.run_progress == 0
            self.output(self.currentProc, "Started")
        self.currentProc.run(1)
        self.time += 1
        
    #outputs information 
    def output(self, outProc, reason)
        pass #possible, CS(Context Switch), Start(New to CPU), Queued(Added to CPU Queue)
    
    #adds a process to memory
    def organizeProcs(self)
        pass
        
    #switches a process into the cpu
    def contextSwitch(self, nextproc):
        pass
        
    #checks if process needs to be switched based on the algorithm
    def checkSwitch(self):
        if self.type == "FCFS":
            self.FCFS()
        elif self.type == "SJF":
            self.SJF()
        elif self.type == "PSJF":
            self.PSJF()
        elif self.type == "RR":
            self.RR()
        elif self.type == "PRI":
            self.PRI()
        else:
            print("error, invalid algorithm\n choices are FCFS SJF PSJF RR PRI\n")