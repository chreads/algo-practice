import sys

file = sys.argv[1] 
def alg(file):
    '''Finds strongly connected components (SCCs) of a directed acyclic graph (DAG)'''
    class Node:
        def __init__(self, name, points_to, fin_time=0, explored=False, leader=0):
            self.name = name

    G = {}

    with open(file) as f:
        for line in f:
            temp = line.rstrip('\n').split(' ')
            if temp[0] not in G:
                G[temp[0]] = Node(temp[1]) 

if __name__ == '__main__':
    alg(file)
