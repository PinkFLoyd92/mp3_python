import psutil
import sqlite3
#http://stackoverflow.com/questions/20499074/run-local-python-script-on-remote-server
class Process:#https://pythonhosted.org/psutil/
    def __init__(self,name):
        "Initializing process object with dictionaries"
        self.name = name
        self.findProcess(name)
        self.memory_percent=0
        self.memory_info_ex =[]
        self.memory_info=[]
        self.net_io_counters = ()
        self.io_counters =()
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
        self.memory_percent = self.process.memory_percent() 

    def printProcess(self):
        print("Process %s \nMemory Percent:%d \nio_counters:%d" %(self.name,self.memory_percent, self.io_counters))

    def saveProcess(self):
        pass
    
    def addCpu_percent(self):
        "Return a float representing the current system-wide CPU utilization as a percentage. When interval is > 0.0 compares system CPU times elapsed before and after the interval (blocking). When interval is 0.0 or None compares system CPU times elapsed since last call or module import, returning immediately."
        self.cpu_percent = self.process.cpu_percent(interval=None)

    def addMemory_info(self):
        self.memory_info = self.process.memory_info()

    def addIo_counters(self):
        self.io_counters = self.process.io_counters()

        
    def addFds(self):
        self.num_fds = self.process.num_fds()

    def add_ctx_switches(self):
        "The number voluntary and involuntary context switches performed by this process."
        self.num_ctx_switches = self.process.num_ctx_switches()

    def addMemory_info_ex(self):
        self.memory_info_ex = self.process.memory_info_ex()

    def addNet_io_counters(self):
        self.net_io_counters = psutil.net_io_counters(pernic=False)

    def setAll(self):
        self.addMemory_percent()
        self.addCpu_percent()
        self.addMemory_info()
        self.addFds()
        self.add_ctx_switches()
        self.addMemory_info_ex()
        self.addNet_io_counters()
        self.addIo_counters()

