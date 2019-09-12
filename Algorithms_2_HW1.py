import sys

file = sys.argv[1] 
def alg(file):
    '''Finds strongly connected components (SCCs) of a graph''' 
    class Node:
        def __init__(self, name, points_to, pointed_by, fin_time=0, not_explored=True, leader=0):
            self.name = name
            self.points_to = points_to
            self.pointed_by = pointed_by

    def DFS_loop1(graph):
        def DFS(graph, i):
            graph[i].not_explored = False
            graph[i].leader = s
            for node in graph[i].points_to:
                if graph[node].not_explored:
                    DFS(graph, node)
            t += 1
            graph[i].fin_time = t
        t = 0
        s = None
        for i in range(len(graph), 0, -1):
            if graph[i].not_explored:
                s = i
                DFS(graph, i)

    def DFS_loop2(graph):
        def DFS(graph, i):
            graph[i].not_explored = False
            graph[i].leader = s
            for node in graph[i].points_to:
                if graph[node].not_explored:
                    DFS(graph, node)
            t += 1
            graph[i].fin_time = t
        t = 0
        s = None
        for i in range(len(graph), 0, -1):
            if graph[graph[i].fin_time].not_explored:
                s = i
                DFS(graph, i)

    # create graph (dict of all nodes)
    G = {}

    with open(file) as f:
        for line in f:
            temp = line.rstrip('\n').split(' ')
            temp[0], temp[1] = int(temp[0]), int(temp[1])
            if temp[0] not in G:
                G[temp[0]] = Node(temp[0], points_to=[temp[1]], pointed_by=[]) 
            elif temp[0] in G:
                G[temp[0]].points_to.append(temp[1])
            if temp[1] not in G:
                G[temp[1]] = Node(temp[1], points_to=[], pointed_by=[temp[0]])
            elif temp[1] in G:
                G[temp[1]].pointed_by.append(temp[0])

    # first pass
    #DFS_loop(G)
    for node in G:
        print(node, "pointed by:", G[node].pointed_by)
        print(node, "points to:", G[node].points_to)
    # reset nodes
    for node in G:
        G[node].not_explored = True


#    DFS_loop(G)

if __name__ == '__main__':
    alg(file)
