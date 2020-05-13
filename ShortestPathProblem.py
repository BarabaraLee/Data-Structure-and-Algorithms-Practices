# Dijkstra's Algorithm: uses Minimum Priority Queue
graph = {'Mountain View':{'San Francisco':51, 'Shanghai':9950, 'Sao Paolo':10375},
         'San Francisco':{'Mountain View':51, 'Shanghai':9900, 'Berlin':9130},
         'London':{'Shanghai':9217, 'Berlin':932, 'Sao Paolo':9471},
         'Shanghai':{'Mountain View':9950, 'San Francisco':9900, 'London':9217},
         'Berlin':{'San Francisco':9130, 'London':932},
         'Sao Paolo':{'Mountain View':10375, 'London':9471}}


def Dijkstra_path(g, start, end):
    prev_node = {}
    shortest_dist = {}
    path = []
    unseen_nodes = graph
    
    for node in graph:
        shortest_dist[node] = float("inf")
    shortest_dist[start] = 0
    
    
    while unseen_nodes:
        # find the next minimum distance node
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_dist[node] < shortest_dist[min_node]:
                min_node = node
        
        # update the distance all the unseen neighbors of the min_node
        for child_node, weight in graph[min_node].items():
            if shortest_dist[min_node]+weight < shortest_dist[child_node]:
                shortest_dist[child_node] = shortest_dist[min_node]+weight
                prev_node[child_node] = min_node
                
        unseen_nodes.pop(min_node)
        
    # save the shortest path in a string
    cur_node = end
    while cur_node != start:
        try:
            path.insert(0, cur_node)
            cur_node = prev_node[cur_node]
        except KeyError:
            print "Path not reachable"
            break
    if shortest_dist[end]!=float("inf"):
        path.insert(0, start)
        print "Shortest Path: {}".format("->".join(path))
        print "Total Distance: {}".format(shortest_dist[end])


Dijkstra_path(graph, "Shanghai", "Berlin")