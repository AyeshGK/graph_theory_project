# use for find shortest path between two nodes


# prerequisites
# the edge weights are should be non negative

# lazy dijkstra algorithm this keeps the algorithm data

import math
import queue as Q


def dijkstra(graph):
    visited = set()
    weight = [math.inf] * len(graph)
    weight[0] = 0
    # use priority queue for add child and get the child in
    #  minimum distant weight (weight,child)
    p_queue = Q.PriorityQueue()
    p_queue.put((0, 0))  # node -> [weight,node]

    while not p_queue.empty():
        node = p_queue.get()  # node -> [weight,node]
        node_weight, node_index = node
        # we can remove some additional nodes reading by
        # the weight of current node might be greater than its weight in weight list
        # this is kind of neat optimization
        if node_weight > weight[node_index]:
            continue

        for child in graph[node[1]]:  # child ->[node,weight]

            if visited.__contains__(child[0]):
                continue

            new_weight = child[1] + node_weight  # get the new weight form current node
            if weight[child[0]] > new_weight:
                weight[child[0]] = new_weight
                p_queue.put((new_weight, child[0]))

        # print("node weight,node index", node)
        visited.add(node_index)  # add current node as visited node

    print(weight)


def find_shortest_path_from_previous_node(graph):
    visited = set()
    previous_node = [None] * len(graph)  # add this line for
    weight = [math.inf] * len(graph)
    previous_node[0] = 0
    weight[0] = 0
    # use priority queue for add child and get the child in
    #  minimum distant weight (weight,child)
    p_queue = Q.PriorityQueue()
    p_queue.put((0, 0))  # node -> [weight,node]

    while not p_queue.empty():
        node = p_queue.get()  # node -> [weight,node]
        node_weight, node_index = node
        # we can remove some additional nodes reading by
        # the weight of current node might be greater than its weight in weight list
        # this is kind of neat optimization
        if node_weight > weight[node_index]:
            continue

        for child in graph[node[1]]:  # child ->[node,weight]

            if visited.__contains__(child[0]):
                continue

            new_weight = child[1] + node_weight  # get the new weight form current node
            if weight[child[0]] > new_weight:
                weight[child[0]] = new_weight
                previous_node[child[0]] = node_index
                p_queue.put((new_weight, child[0]))

        # print("node weight,node index", node)
        visited.add(node_index)  # add current node as visited node

    print(previous_node)
    print(weight)
    return weight, previous_node


def get_shortest_path_for_given_node(graph, start_node, end_node):
    weight, prev = find_shortest_path_from_previous_node(graph)

    if weight[start_node] == math.inf:
        print("Isolated node")
        return

    path = [end_node]
    # for i in prev[start_node:end_node+1]:
    #     path.append(path[])

    while True:
        node = path[-1]
        prev_node = prev[node]
        path.append(prev_node)
        if prev_node == start_node:
            break

    path.reverse()
    print("path ", ' -> '.join(map(str, path)))


# nodes in graph node = 0 -> (adjacency node, weight)
graph = [
    [[1, 4], [2, 1]],
    [[3, 1]],
    [[1, 2], [3, 5]],
    [[4, 3]],
    []
]


# optimization if some node we find then its found then finding is over  early stop

def dijkstra_with_early_stop(graph, find):
    visited = set()
    weight = [math.inf] * len(graph)
    weight[0] = 0
    # use priority queue for add child and get the child in
    #  minimum distant weight (weight,child)
    p_queue = Q.PriorityQueue()
    p_queue.put((0, 0))  # node -> [weight,node]

    while not p_queue.empty():
        node = p_queue.get()  # node -> [weight,node]
        node_weight, node_index = node
        # we can remove some additional nodes reading by
        # the weight of current node might be greater than its weight in weight list
        # this is kind of neat optimization
        if node_weight > weight[node_index]:
            continue

        if find == node_index:
            break

        for child in graph[node[1]]:  # child ->[node,weight]

            if visited.__contains__(child[0]):
                continue

            new_weight = child[1] + node_weight  # get the new weight form current node
            if weight[child[0]] > new_weight:
                weight[child[0]] = new_weight
                p_queue.put((new_weight, child[0]))

        # print("node weight,node index", node)
        visited.add(node_index)  # add current node as visited node

    print(weight)


#
# dijkstra(graph)
# get_shortest_path_for_given_node(graph, 0, 4)
dijkstra_with_early_stop(graph, 3)
