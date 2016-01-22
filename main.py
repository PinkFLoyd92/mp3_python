import sys
import time
sys.path.append('modules')
from process import Process
def main():
    zookeeper = Process("zookeeper")
    supervisor = Process("supervisor")
    nimbus = Process("nimbus")
    zookeeper.setAll()
    supervisor.setAll()
    nimbus.setAll()
    # nimbus.printProcess()
    # zookeeper.printProcess()
    # supervisor.printProcess()
    # print(nimbus.memory_info[1])
    # print(nimbus.io_counters)
    while(1):
        zookeeper.setAll()
        supervisor.setAll()
        nimbus.setAll()
        nimbus.saveProcess()
        zookeeper.saveProcess()
        supervisor.saveProcess()
        time.sleep(.200)
main()
