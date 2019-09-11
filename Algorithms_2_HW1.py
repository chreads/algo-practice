def alg(file):
    '''Finds strongly connected components (SCCs) of a directed acyclic graph (DAG)'''
    class Node:
        def __init__(self, name, fin_time=0, explored=False, leader=0):
            self.name = name
