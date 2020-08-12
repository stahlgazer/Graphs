from util import Queue

def earliest_ancestor(ancestors, starting_node):
    
    q = Queue()
    current_node = starting_node
    connections = {}
    
    for item in ancestors: 
        parent = item[0]
        child = item[1]

        if child not in connections:
            connections[child] = set()
        connections[child].add(parent)

    if starting_node in connections:
        q.enqueue(connections[current_node])
    else:
        return -1

    while True:
        family = q.dequeue()
        current_node = min(family)
        if current_node not in connections:
            return current_node
        else:
            q.enqueue(connections[current_node])