# bfs is very important alogrithm
# it takes time complexsity O(V+E) in unweighted undirect or directed graph
# it has to traverse all nodes at it has to check the all its neighbours visited or not


# class node for create objects of nodes
class Node:
    def __init__(self, value, neighbours):
        self.value = value
        self.neighbours = neighbours

    def getNeighbours(self):
        return self.neighbours

    def getValue(self):
        return self.value


def bfs(graph):
    visited = set()

    queue = []
    queue.append(graph)

    # python list use for queue cause to the performance due to the reassigning to the list when reamove
    # item from first
    # so i just try to iterate over it
    index = 0
    while(index < len(queue)):
        node = queue[index]
        index += 1

        for neighbour in node.getNeighbours():
            # just add not visited values into queue
            if(neighbour not in visited):
                queue.append(neighbour)

        # after getting all neighbours set the node as visited
        print("printing node value :", node.getValue())
        visited.add(node)


# create sum nodes
node_0 = Node(0, [])
node_1 = Node(1, [])
node_2 = Node(2, [])
node_3 = Node(3, [])
node_4 = Node(4, [])
node_5 = Node(5, [])
node_6 = Node(6, [])
node_7 = Node(7, [])
node_8 = Node(8, [])
node_9 = Node(9, [])
node_10 = Node(10, [])
node_11 = Node(11, [])
node_12 = Node(12, [])

# connecting graph

node_0.neighbours.extend((node_9, node_11, node_7))
node_1.neighbours.extend((node_8, node_10))
node_2.neighbours.extend((node_12, node_3))
node_3.neighbours.extend((node_2, node_7, node_4))
node_4.neighbours.extend((node_3,))
node_5.neighbours.extend((node_6,))
node_6.neighbours.extend((node_7, node_5))
node_7.neighbours.extend((node_3, node_6, node_11))
node_8.neighbours.extend((node_1, node_12))
node_9.neighbours.extend((node_8, node_10))
node_10.neighbours.extend((node_1,))
node_11.neighbours.extend((node_7,))
node_12.neighbours.extend((node_2, node_8))


bfs(node_0)
