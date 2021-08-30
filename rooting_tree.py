class TreeNode:
    def __init__(self, id, parent, childrens):
        self.id = id
        self.parent = parent
        self.childrens = childrens


def rootTree(graph, rootId=0):
    root = TreeNode(rootId, None, [])
    return buildTree(graph, root, None)


def buildTree(graph, node, parent):
    # building tree first tree node is root node
    # after that node can be any node at that stage node is kind of root
    # graph[node.id] get all childrens id's from graph
    for childId in graph[node.id]:  # iterate through the id
        # parent id
        if parent != None and childId == parent.id:
            continue

        child = TreeNode(childId, node, [])
        node.childrens.append(child)
        buildTree(graph, child, node)
        return node


graph = [
    [1, 2, 5],
    [],
    [3],
    [],
    [],
    [4, 6],
    []
]

tree = rootTree(graph, 0)
