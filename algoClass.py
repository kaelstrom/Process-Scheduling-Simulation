# Nathan Black, Kyle Johnsen
# Op Sys Project 1
# Process Scheduling Simulation
# 10/20/11
import copy

timeCS = 8
timeSlice = 100

class algoClass(object):
    def __init__(self, type, procList, rtime, stats):
        self.stats = copy.deepcopy(stats)
        self.type = type
        self.inMemProcs = []
        self.time = rtime
        self.toAddProcs = copy.deepcopy(procList)
        self.currentSlice = 0
        
    def start(self):
        self.organizeProcs()
        self.currentProc = self.inMemProcs[0]
        
    #runs the current process in cpu
    def run(self):
        #if new to CPU, output so
        if self.currentProc != "IDLE":
            if self.currentProc.run_progress == 0:
                self.output(["started", self.currentProc])
            if not self.currentProc.isDone():
                self.currentProc.run(1)
        self.time[0] += 1
        
    def allDone(self):
        maxStartTime = max([x.start_time for x in self.toAddProcs])
        return self.time[0] > maxStartTime and len(self.inMemProcs) == 0
        
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
            #track initial wait time
            self.stats[self.currentProc.pid][1] = self.time[0] - proc.start_time
        elif args[0] == "cs":
            proc1 = args[1]
            proc2 = args[2]
            print("[time: %dms] Context switch (swapped out process %d for process %d)" 
                    %(self.time[0], proc1.pid, proc2.pid))
        elif args[0] == "finished":
            proc = args[1]
            print("[time: %dms] Process %d terminated (turnaround time %dms, total wait time %dms)"
                    %(self.time[0], proc.pid, (self.time[0]-proc.start_time), (self.time[0]-proc.start_time-proc.time_req)))
            #track turnaround time
            self.stats[self.currentProc.pid][0] = self.time[0] - self.currentProc.start_time
            #track total wait time
            self.stats[self.currentProc.pid][2] = (self.time[0]  - self.currentProc.start_time) - self.currentProc.time_req
    
    #sorts ready queue by the current algorithm
    def organizeProcs(self):
    
        #adds jobs to queue as they arrive
        for proc in self.toAddProcs:
            if proc.start_time == self.time[0]:
                self.output(["created", proc])
                self.inMemProcs.append(proc)
                
                
        if self.type == "FCFS" or self.type == "RR":
            pass
            
        #sorting according to what the algo cares about, shortest remaining run time or priority
        elif self.type == "SJF" or self.type == "PSJF":
            self.inMemProcs = sorted(self.inMemProcs, key=lambda Process: Process.time_req - Process.run_progress)
        elif self.type == "PRI":
            self.inMemProcs = sorted(self.inMemProcs, key=lambda Process: Process.priority)
            
    #finds the process given in the self.inMemProcs list
    #return -1 if not found
    def findProc(self, givenProc):  
        for i in range(0, len(self.inMemProcs)):
            if self.inMemProcs[i].pid == givenProc.pid:
                return i
        return -1
    
    #switch from current process to the next
    def contextSwitch(self, nextProc):
    
        #display a process termination
        if self.currentProc.isDone():
            self.output(["finished", self.currentProc])
            
        #display a context switch
        self.output(["cs", self.currentProc, nextProc])
            
        #go to the next process, increment the time
        self.currentProc = nextProc
        self.time[0] += timeCS
        
    #checks if process needs to be switched based on the algorithm
    def checkSwitch(self):
        #only do stuff if there are processes in the ready queue
        if len(self.inMemProcs) != 0:
            if self.currentProc == "IDLE":
                pass
            elif self.currentProc.isDone():
                    
                #switch to the next best thing, or go idle if there isnt one
                if len(self.inMemProcs) > 1:
                    self.contextSwitch(self.inMemProcs[1])
                    self.inMemProcs.remove(self.inMemProcs[0])
                else:
                    self.output(["finished", self.currentProc])
                    self.inMemProcs.remove(self.inMemProcs[0])
                    self.currentProc = "IDLE"
                    
            elif self.type == "FCFS" or self.type == "SJF":
                return;
                
            #round robin wait till the time slice expires to force a context switch
            elif self.type == "RR":
                if self.currentSlice >= timeSlice and len(self.inMemProcs)>1:
                    self.contextSwitch(self.inMemProcs[1])
                    self.currentSlice = 0
                    
                    #round robin cycles the list
                    tempProc = self.inMemProcs[0]
                    self.inMemProcs.remove(self.inMemProcs[0])
                    self.inMemProcs.append(tempProc)
                else:
                    self.currentSlice += 1
            
            #if something more important tops the list, the preempt out the current process
            elif self.type == "PRI" or self.type == "PSJF":
                if self.currentProc != self.inMemProcs[0]:
                    self.contextSwitch(self.inMemProcs[0])
                
            else:
                print("error, invalid algorithm\n choices are FCFS SJF PSJF RR PRI\n")