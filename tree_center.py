# tree is undirect graph

def treeCenter(g):
    n = len(g)
    degree = [0]*n
    leaves = []
    for i in range(n):
        degree[i] = len(g[i])
        # since this undirect graph we can remove the 0 and 1 if there at least one connection between
        # two nodes it is 1 degree case cause of this is undirected graph
        if(degree[i] == 0 or degree[i] == 1):
            leaves.append(i)
            degree[i] == 0

    count = len(leaves)
    while(count < n):
        new_leaves = []
        print(leaves)
        # traverse inside previous outer level nodes
        for node in leaves:
            # get that nodes all childs
            # one of that childs shows different number of degree because
            # of set the degree of child by reducing degree by -1
            for neighbour in g[node]:
                degree[neighbour] -= 1  # reducing the number of degree
                # by this degree of node shows different values at same level because of
                # if that node is at outer level we can remove it so degree change
                # by reducing we can indicate remove that outer level node
                if(degree[neighbour] == 1):
                    new_leaves.append(neighbour)
            degree[node] = 0  # remove that outerlevel node
        # now we selected outer parent node for next level nodes

        leaves = new_leaves  # removing outer level nodes
        # increasing count indicate outerlevel nodes are deleted
        count += len(new_leaves)

    return leaves


g = [
    [1],
    [0, 3, 4],
    [3],
    [1, 2, 6, 7],
    [1, 5, 8],
    [4],
    [3, 9],
    [3],
    [4],
    [6]
]


print(treeCenter(g))
