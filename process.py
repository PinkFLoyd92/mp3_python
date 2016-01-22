import psutil
import csv
import os
#http://stackoverflow.com/questions/20499074/run-local-python-script-on-remote-server
class Process:#https://pythonhosted.org/psutil/
    def __init__(self,name):
        "Initializing process object with dictionaries"
        self.name = name
        self.findProcess(name)
        self.memory_percent=0
        self.memory_info_ex =()
        self.memory_info=[] #tuple(rss,vms)
        self.net_io_counters = ()#snetio(bytes_sent, bytes_recv, packets_sent, packets_recv, errin=0, errout=0, dropin=0, dropout=0)

        self.io_counters =()#pio(read_count, write_count, read_bytes, write_bytes)

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
        print("Process %s \nMemory Percent:%d\nCPU percent: %d" %(self.name,self.memory_percent, self.cpu_percent))
        print(self.memory_info)
        print(self.num_fds)

    
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

    def saveProcess(self):
        with open(self.name+'.csv', 'a', newline='') as f:
            fieldNames = ['memory_percent','rss','vms','bytes_sent','bytes_recv','packets_sent','packets_recv','errin','errout','dropout','read_count','write_count','read_bytes','write_bytes','cpu_percent','num_fds','num_ctx_switchesVoluntary','num_ctx_switchesInvoluntary']
            writer = csv.DictWriter(f, fieldnames=fieldNames)
            if os.stat(self.name+".csv").st_size == 0:
                writer.writeheader()
            writer.writerow({'memory_percent':self.memory_percent , 'rss':self.memory_info[0], 'vms':self.memory_info[1], 'bytes_sent':self.net_io_counters[0], 'bytes_recv':self.net_io_counters[1], 'packets_sent':self.net_io_counters[2], 'packets_recv':self.net_io_counters[3], 'errin':self.net_io_counters[4], 'errout':self.net_io_counters[5], 'dropout':self.net_io_counters[6], 'read_count':self.io_counters[0], 'write_count':self.io_counters[1],'read_bytes':self.io_counters[2],'write_bytes':self.io_counters[3],'cpu_percent':self.cpu_percent,'num_fds':self.num_fds,'num_ctx_switchesVoluntary':self.num_ctx_switches[0],'num_ctx_switchesInvoluntary':self.num_ctx_switches[1]})
