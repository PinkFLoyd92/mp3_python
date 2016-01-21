import sys
sys.path.append('modules')
from process import Process

def main():
    proceso = Process("zookeeper")
    proceso2 = Process("supervisor")
    proceso3 = Process("nimbus")


main()
