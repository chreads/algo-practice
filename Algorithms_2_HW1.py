import sys, threading, resource
sys.setrecursionlimit(800000)
threading.stack_size(97108864)

file = sys.argv[1] 
def alg(file):
    '''Finds strongly connected components (SCCs) of a graph''' 
    class Node:
        def __init__(self, name, points_to, pointed_by, fin_time=0, not_explored=True, leader=0):
            self.name = name
            self.points_to = points_to
            self.pointed_by = pointed_by
            self.fin_time = fin_time
            self.not_explored = not_explored
            self.leader = leader

    def DFS_loop1(graph):
        def DFS(graph, i):
            graph[i].not_explored = False
            for node in graph[i].pointed_by:
                if graph[node].not_explored:
                    DFS(graph, node)
            global t
            t += 1
            graph[i].fin_time = t
        global t
        t = 0
        for i in range(len(graph), 0, -1):
            if graph[i].not_explored:
                DFS(graph, i)

    def DFS_loop2(graph):
        def DFS(graph, i):
            graph[i].not_explored = False
            graph[i].leader = s
            for node in graph[i].points_to:
                if graph[node].not_explored:
                    DFS(graph, node)
        global s 
        s = None
        for i in range(len(graph), 0, -1):
            if graph[G_by_fin_time[i]].not_explored:
                s = G_by_fin_time[i]
                DFS(graph, G_by_fin_time[i])

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
    DFS_loop1(G)
    
    # make fin_time to name dict
    G_by_fin_time = {}     
    for node in range(len(G), 0, -1):
        G[node].not_explored = True
        G_by_fin_time[G[node].fin_time] = G[node].name

    DFS_loop2(G)

    count_dict = {}

    for node in G:
        if G[node].leader in count_dict:
            count_dict[G[node].leader] += 1
        else:
            count_dict[G[node].leader] = 1
    #    print(G[node].name, "leader=", G[node].leader)
    print(list(sorted(count_dict.values(), reverse=True))[:5])

if __name__ == '__main__':
    thread = threading.Thread(target=alg, args=(file,))
    thread.start()
