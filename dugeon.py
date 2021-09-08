def printGraph(graph):
    for i in range(len(graph)):
        print(graph[i])


def addQueue(r, c, graph, queue):
    if(graph[r][c] == "e"):
        print("Find ending point ")
        return 1

    r_size = len(graph)
    c_size = len(graph[0])

    dr = [-1, +1, 0, 0]
    dc = [0, 0, -1, +1]

    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        if (rr < 0 or rr >= r_size or cc < 0 or cc >= c_size):
            continue

        if(graph[rr][cc] == "#"):
            continue

        queue.append((rr, cc))

    return 0


def dugeon(graph):

    queue = []
    queue.append((0, 0))
    i = 0
    while(i < len(queue)):
        # print(queue)
        r, c = queue[i]

        if(addQueue(r, c, graph, queue)):
            break

        graph[r][c] = "#"
        i += 1
        # print(r, c)

    printGraph(graph)


graph = [
    ["s", ".", ".", "#", ".", "."],
    [".", "#", ".", ".", ".", "."],
    ["#", ".", ".", ".", "#", "."],
    [".", ".", "#", "#", ".", "."],
    [".", ".", ".", ".", ".", "."],
    ["#", ".", ".", "#", ".", "."],
    [".", ".", "e", ".", ".", "."],
]
dugeon(graph)
