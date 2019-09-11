import sys

file = sys.argv[1] 
def alg(file):
    '''Finds strongly connected components (SCCs) of a graph''' 
    class Node:
        def __init__(self, name, points_to, fin_time=0, explored=False, leader=0):
            self.name = name
            self.points_to = points_to

    # create dict of all nodes
    G = {}

    with open(file) as f:
        for line in f:
            temp = line.rstrip('\n').split(' ')
            print(temp[0], temp[1])
            if temp[0] not in G:
                G[temp[0]] = Node(temp[0], points_to=[temp[1]]) 
                if temp[1] not in G:
                    G[temp[1]] = Node(temp[1], [])  
            elif temp[0] in G:
                G[temp[0]].points_to.append(temp[1])
    for i in G:
        print(i, G[i].points_to)

if __name__ == '__main__':
    alg(file)
