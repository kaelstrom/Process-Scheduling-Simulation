class algoClass(object):
    def __init__(self, type, procList, time):
        self.type = type
        self.inMemProcs = []
        self.time = time
        self.toAddProcs = procList
        self.organizeProcs()
        self.currentProc = self.inMemProcs[0]
        
    #runs the current process in cpu
    def run(self):
        #if new to CPU, output so
        if self.currentProc.run_progress == 0:
            self.output(self.currentProc, "Started")
        self.currentProc.run(1)
        self.time += 1
        
    #outputs information 
    def output(self, outProc, reason):
        pass #possible, CS(Context Switch), Start(New to CPU), Queued(Added to CPU Queue)
    
    #adds a process to memory
    def organizeProcs(self):
        j = len(self.inMemProcs)
        for proc in self.toAddProcs:
            if proc.start_time <= self.time:
                if self.time != 0:
                    self.output(proc, "Queued")
                self.inMemProcs[j]= proc
                #delete self.toAddProcs[i], i--
        #if self.type == "FCFS" || self.type == "RR":
        #elif self.type == "SJF" || self.type == "PSFJ":
            #organize by inMemProcs.time_req (think about which one is currentProc
        #elif self.type == "Pri":
            
    #finds the process given in the self.inMemProcs list
    #return -1 if not found
    def findProc(self, givenProc):
    #switches a process into the cpu
        pass
    
    #check if round robin, else just switch and do normally
    def contextSwitch(self, nextproc):
        pass
        
    #checks if process needs to be switched based on the algorithm
    def checkSwitch(self):
        if self.type == "FCFS" or self.type == "SJF":
            return 0;
        elif self.type == "PSJF":
            if self.findProc(currentProc)!=0:
                self.contextSwitch(self.inMemProcs[0])
        elif self.type == "RR":
            self.contextSwitch(self.inMemProcs[1])
        elif self.type == "PRI":
            pass
            #do whatever
        else:
            print("error, invalid algorithm\n choices are FCFS SJF PSJF RR PRI\n")