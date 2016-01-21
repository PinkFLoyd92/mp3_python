import psutil
import sqlite3
class Process:#https://pythonhosted.org/psutil/
    def __init__(self,name):
        "Initializing process object with dictionaries"
        self.name = name
        self.findProcess(name)
        self.memory_percent=0
        self.memory_info_ex =[]
        self.memory_info=[]
        self.io_counters =0
        self.cpu_percent =0
        self.num_fds = 0
        self.num_ctx_switches = 0

    def findProcess(self,name):
        for proc in psutil.process_iter(): 
            process = psutil.Process(proc.pid)
            pname = process.name()
            cmd = process.cmdline()
            # print(cmd)
            for line in cmd:
                if name in line:
                    # print(cmd)
                    print(process.pid)
                    self.process = process
                    return 1
        self.process = "fail"
        self.name = "fail"
        return -1

    def addMemory_percent(self):
        "Compare physical system memory to process resident memory (RSS) and calculate process memory utilization as a percentage."
        # self.memory_percent = self.process.memory_percent() 

    def printProcess(self):
        print("Proceso %s %d" %(self.name,self.memory_percent))
