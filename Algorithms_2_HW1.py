import sys

file = sys.argv[1] 
def alg(file):
    '''Finds strongly connected components (SCCs) of a graph''' 
    class Node:
        def __init__(self, name, points_to, fin_time=0, not_explored=True, leader=0):
            self.name = name
            self.points_to = points_to

    def DFS_loop(graph):
        t = 0
        s = None
        for i in range(len(graph), 0, -1):
            if graph[i].not_explored:
                s = i
                DFS(graph, i)
 

    # create reversed graph (dict of all nodes)
    G = {}

    with open(file) as f:
        for line in f:
            temp = line.rstrip('\n').split(' ')
            temp[0], temp[1] = int(temp[0]), int(temp[1])
            if temp[1] not in G:
                G[temp[1]] = Node(temp[1], points_to=[temp[0]]) 
                if temp[0] not in G:
                    G[temp[0]] = Node(temp[0], [])  
            elif temp[1] in G:
                G[temp[1]].points_to.append(temp[0])

    # reset node pointers
    for node in G:
        print(node, G[node].points_to)
        G[node].points_to = []

    # create forward graph
    with open(file) as f:
        for line in f:
            temp = line.rstrip('\n').split(' ')
            temp[0], temp[1] = int(temp[0]), int(temp[1])
            G[temp[0]].points_to.append(temp[1])

    for node in G:
        print(node, G[node].points_to)

if __name__ == '__main__':
    alg(file)
