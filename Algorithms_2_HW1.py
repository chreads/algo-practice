import sys

file = sys.argv[1] 
def alg(file):
    '''Finds strongly connected components (SCCs) of a directed acyclic graph (DAG)'''
    class Node:
        def __init__(self, name, fin_time=0, explored=False, leader=0):
            self.name = name

    with open(file) as f:
        for line in f:
            temp = line.rstrip('\n').split(' ')
            print(temp) 

if __name__ == '__main__':
    alg(file)
