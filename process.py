# Kyle Johnsen, Jeff Johnston, Brett Kaplan
# Op Sys Project 1
# Process Scheduling Simulation
# 10/20/11
import random

#import process names from a text file, stripping newlines
with open("names.txt") as in_file:
    names = in_file.readlines()
for i in range(len(names)):
    names[i] = names[i].rstrip("\n")

class Process(object):
    def __init__(self, pid, start_time):
        self.start_time = start_time #when process is added to memory
        self.run_progress = 0
        self.name = random.choice(names)
        self.pid = pid
        self.time_req = random.randint(500,7500)
        self.priority = random.randint(0,4)
    def run(self, runtime):
        self.run_progress += runtime
    def isDone(self):
        return self.run_progress >= self.time_req