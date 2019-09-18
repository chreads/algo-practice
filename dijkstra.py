from node_heap import *
import sys

file = sys.argv[1] 

class Node:
    def __init__(self, name, adjacent, heap_index, key=1000000):
        self.name = name
        self.adjacent = adjacent 
        self.key = key
        self.heap_index = heap_index

def process_input(file):

    def create_nodes():
        with open(file) as f:
            for i, line in enumerate(f):
                temp = line.rstrip('\n').split()
                G[int(temp[0])] = Node(name=int(temp[0]), adjacent={}, heap_index=i-1)
                add_connected_nodes(temp)

    def add_connected_nodes(temp):
        for conn_node in temp[1:]:
            data = conn_node.split(',')
            G[int(temp[0])].adjacent[int(data[0])] = int(data[1])

    G = {}
    create_nodes()
    return G

def main():

    def dijkstra(G):
        '''Computes shortest distance between node 1 and all other vertices, given an undirected graph with positive edge lengths'''
        X = {1}
        A = [0 for i in range(len(G))]
        V = set(G.keys())
        min_heap = [G[i] for i in range(2, len(G)+1)]
        while X != V:
            for X_node in X:
                for node, length in G[X_node].adjacent.items():
                    if node in V - X:
                        heap_delete(min_heap, G[node].heap_index, G)                
                        G[node].key = min(A[X_node-1] + length, G[node].key) 
                        heap_insert(min_heap, G[node], G)
            w = heap_extract(min_heap, G)
            X.add(w.name)
            A[w.name-1] = w.key
        A = [num if num is not 0 else 1000000 for num in A]
        for path in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
            print(A[path-1])
    G = process_input(file)
    dijkstra(G)

if __name__ == "__main__":
    main()
