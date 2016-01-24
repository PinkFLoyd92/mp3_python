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
    try:
        zookeeper.setAll()
        zookeeper.saveProcess()
    except:
        print("Error, demonio de zookeeper está muerto.")
    try:
        supervisor.setAll()
        supervisor.saveProcess()
    except:
        print("Demonio del supervisor está muerto.")
    try:
        nimbus.setAll()
        nimbus.saveProcess()
    except:
        print("Error, demonio de nimbus está muerto.")


    
"""   while(1):
        zookeeper.setAll()
        supervisor.setAll()
        nimbus.setAll()
        nimbus.saveProcess()
        zookeeper.saveProcess()
        supervisor.saveProcess()
        # time.sleep(.200)"""


main()
