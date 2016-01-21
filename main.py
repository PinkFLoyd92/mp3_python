import sys
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
    print(nimbus.io_counters)
    nimbus.saveProcess()
    # print(nimbus.num_ctx_switches)

main()
