def min_heapify(heap, i, graph):
    left = 2*i + 1
    right = 2*i + 2
    smallest = i

    if left < len(heap) and heap[left].key < heap[smallest].key:
        smallest = left

    if right < len(heap) and heap[right].key < heap[smallest].key:
        smallest = right

    if smallest != i:
        temp = heap[smallest]
        heap[smallest] = heap[i]
        graph[heap[smallest].name].heap_index = smallest
        heap[i] = temp
        graph[heap[i].name].heap_index = i
        min_heapify(heap, smallest, graph)

def bubble_up(heap, i, graph):
    parent = (i-1)//2
    if parent >= 0 and heap[i].key < heap[parent].key:
        temp = heap[i]
        heap[i] = heap[parent]
        graph[heap[i].name].heap_index = i
        heap[parent] = temp
        graph[heap[parent].name].heap_index = parent
        bubble_up(heap, parent, graph)

def heap_delete(heap, i, graph):
    if i != len(heap)-1:
        heap[i] = heap.pop()
        graph[heap[i].name].heap_index = i
        min_heapify(heap, i, graph)
        bubble_up(heap, i, graph)
    elif i == len(heap)-1:
        heap.pop()

def heap_extract(heap, graph):
    if len(heap) > 1:
        min_node = heap[0]
        heap[0] = heap.pop()
        graph[heap[0].name].heap_index = 0
        min_heapify(heap, 0, graph)
        return min_node
    else:
        return heap.pop()
    
def heap_insert(heap, node, graph):
    heap.append(node)
    i = len(heap) - 1
    graph[heap[i].name].heap_index = i
    bubble_up(heap, i, graph)        
