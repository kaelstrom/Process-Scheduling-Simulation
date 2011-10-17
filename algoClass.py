
class algoClass()
    def __init__(self, type, time):
        self.type = type
        self.procs = []
        self.time = time
        self.currentproc
        
    #runs the current process in cpu
    def run(self):
        pass
        
    #adds a process to memory
    def addProc(self, proc)
        self.procs.append(proc)
    
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