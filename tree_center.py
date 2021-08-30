class Node:
    def __init__(self, value, childrens):
        self.value = value
        self.childrens = childrens

    def getChildrens(self):
        return self.childrens

    def getNumofChildrens(self):
        return len(self.childrens)


def treeCenter(g):
    n = len(g)
    degree = []*n
    for i in (0, n):
        degree[i] = g[i]


g = [
    [2, 3],
    [],
    [],
    [],
    []
]
