# Nathan Black, Kyle Johnsen
# Op Sys Project 1
# Process Scheduling Simulation
# 10/20/11

import copy

class algoClass(object):
    def __init__(self, type, procList, rtime):
        self.type = type
        self.inMemProcs = []
        self.time = rtime
        self.toAddProcs = copy.deepcopy(procList)
        self.organizeProcs()
        self.currentProc = self.inMemProcs[0]
        
    #runs the current process in cpu
    def run(self):
        #if new to CPU, output so
        if self.currentProc.run_progress == 0:
            self.output(["started", self.currentProc])
        self.currentProc.run(1)
        self.time[0] += 1
        
    #outputs information 
    def output(self, args):
        #possible, cs(Context Switch), started(New to CPU), created(Added to CPU Queue)
        if args[0] == "created":
            proc = args[1]
            print("[time: %dms] Process %d created (requiring %dms CPU time)" 
                    %(self.time[0], proc.pid, proc.time_req))
        elif args[0] == "started":
            proc = args[1]
            print("[time: %dms] Process %d accessed CPU for the first time (wait time %dms)" 
                    %(self.time[0], proc.pid, (self.time[0] - proc.start_time)))
            
    
    #adds a process to memory
    def organizeProcs(self):
        for proc in self.toAddProcs:
            j = len(self.inMemProcs)
            if proc.start_time <= self.time[0]:
                if self.time[0] != 0:
                    self.output(["created", proc])
                self.inMemProcs.append(proc)
                self.toAddProcs.remove(proc)
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
            if self.findProc(self.currentProc)!=0:
                self.contextSwitch(self.inMemProcs[0])
        elif self.type == "RR":
            self.contextSwitch(self.inMemProcs[1])
        elif self.type == "PRI":
            pass
            #do whatever
        else:
            print("error, invalid algorithm\n choices are FCFS SJF PSJF RR PRI\n")