# Nathan Black, Kyle Johnsen
# Op Sys Project 1
# Process Scheduling Simulation
# 10/20/11
import copy

timeCS = 8
timeSlice = 100

class algoClass(object):
    def __init__(self, type, procList, rtime, stats):
        self.stats = stats
        self.type = type
        self.inMemProcs = []
        self.time = rtime
        self.toAddProcs = copy.deepcopy(procList)
        self.organizeProcs()
        self.currentProc = self.inMemProcs[0]
        self.currentSlice = 0
        
    #runs the current process in cpu
    def run(self):
        #if new to CPU, output so
        if self.currentProc != "IDLE":
            if self.currentProc.run_progress == 0:
                self.output(["started", self.currentProc])
                self.stats[self.currentProc.pid][1] = self.time[0]
            if not self.currentProc.isDone():
                self.currentProc.run(1)
        self.time[0] += 1
        
    #outputs information 
    def output(self, args):
        #possible, cs(Context Switch), started(New to CPU), created(Added to CPU Queue), finished (completed by CPU)
        if args[0] == "created":
            proc = args[1]
            print("[time: %dms] Process %d created (requiring %dms CPU time)" 
                    %(self.time[0], proc.pid, proc.time_req))
        elif args[0] == "started":
            proc = args[1]
            print("[time: %dms] Process %d accessed CPU for the first time (initial wait time %dms)" 
                    %(self.time[0], proc.pid, (self.time[0] - proc.start_time)))
            proc.initwait = (self.time[0] - proc.start_time)
        elif args[0] == "cs":
            proc1 = args[1]
            proc2 = args[2]
            print("[time: %dms] Context switch (swapped out process %d for process %d)" 
                    %(self.time[0], proc1.pid, proc2.pid))
        elif args[0] == "finished":
            proc = args[1]
            print("[time: %dms] Process %d terminated (turnaround time %dms, total wait time %dms)"
                    %(self.time[0], proc.pid, (self.time[0]-proc.start_time), (self.time[0]-proc.start_time-proc.time_req)))
            #proc.totwait = (self.time[0]-proc.start_time-proc.time_req)
            #proc.turnaround = (self.time[0]-proc.start_time)
    
    #adds a process to memory
    def organizeProcs(self):
        for proc in self.toAddProcs:
            if proc.start_time == self.time[0]:
                self.output(["created", proc])
                self.inMemProcs.append(proc)
        self.toAddProcs = []
        if self.type == "FCFS" or self.type == "RR":
            pass
        elif self.type == "SJF" or self.type == "PSFJ":
            self.inMemProcs = sorted(self.inMemProcs, key=lambda Process: Process.time_req - Process.run_progress)
            #organize by inMemProcs.time_req (think about which one is currentProc)
        elif self.type == "PRI":
            self.inMemProcs = sorted(self.inMemProcs, key=lambda Process: Process.priority)
            
    #finds the process given in the self.inMemProcs list
    #return -1 if not found
    def findProc(self, givenProc):
    #switches a process into the cpu
        pass
    
    #check if round robin, else just switch and do normally
    def contextSwitch(self, nextProc):
        if self.currentProc.isDone():
            self.output(["finished", self.currentProc])
        self.output(["cs", self.currentProc, nextProc])
            #if self.type == "RR":
                #tempProc = self.inMemProcs[0]
                #self.inMemProcs.remove(self.inMemProcs[0])
                #self.inMemProcs.append(tempProc)
            #elif self.type == "PSJF"|| self.type =="PRI":
                #self.currentProc = nextProc
        self.currentProc = nextProc
        self.time[0] += timeCS
        
    #checks if process needs to be switched based on the algorithm
    def checkSwitch(self):
        if len(self.inMemProcs) != 0:
            if self.currentProc == "IDLE":
                pass
            elif self.currentProc.isDone():
                #turnaround
                self.stats[self.currentProc.pid][0] = self.time[0] - self.currentProc.start_time
                #total wait
                self.stats[self.currentProc.pid][2] = (self.time[0]  - self.currentProc.start_time) - self.currentProc.time_req
                    
                if len(self.inMemProcs) > 1:
                    self.contextSwitch(self.inMemProcs[1])
                    self.inMemProcs.remove(self.inMemProcs[0])
                else:
                    self.output(["finished", self.currentProc])
                    self.inMemProcs.remove(self.inMemProcs[0])
                    self.currentProc = "IDLE"
                    
            elif self.type == "FCFS" or self.type == "SJF":
                return 0;
            elif self.type == "PSJF":
                if self.findProc(self.currentProc)!=0:
                    self.contextSwitch(self.inMemProcs[0])
            elif self.type == "RR":
                if self.currentSlice >= self.timeSlice:
                    self.contextSwitch(self.inMemProcs[1])
                    self.currentSlice = 0
                else:
                    self.currentSlice += 1
                #if time slice is over
                    #self.contextSwitch(self.inMemProcs[1])
            elif self.type == "PRI":
                self.organizeProcs()
                if self.currentProc != self.inMemProcs[0]:
                    self.contextSwitch(self.inMemProcs[0])
                
            else:
                print("error, invalid algorithm\n choices are FCFS SJF PSJF RR PRI\n")