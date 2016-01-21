import sys
sys.path.append('modules')
from process import Process

def main():
    zookeeper = Process("zookeeper")
    supervisor = Process("supervisor")
    nimbus = Process("nimbus")


main()
