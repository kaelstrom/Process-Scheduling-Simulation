# Nathan Black, Kyle Johnsen
# Op Sys Project 1
# Process Scheduling Simulation
# 10/20/11

import random

class Process(object):
    def __init__(self, pid, start_time):
        self.start_time = start_time #when process is added to memory
        self.run_progress = 0
        self.pid = pid
        self.time_req = random.randint(500,7500)
        self.priority = random.randint(0,4)
    def run(self, runtime):
        self.run_progress += runtime
    def isDone(self):
        return self.run_progress >= self.time_req