class Node:
    def __init__(self, value, childrens):
        self.value = value
        self.childrens = childrens

    def getChildrens(self):
        return self.childrens

    def getValue(self):
        return self.value


def leafSum(node):

    if(node == None):
        return 0

    if(isLeaf(node)):
        print("node value", node.value)
        return node.getValue()

    tot = 0
    for childNode in node.getChildrens():
        tot += leafSum(childNode)

    return tot


def isLeaf(node):
    return len(node.getChildrens()) == 0


def height(node):
    if(node == None):
        return -1

    if(isLeaf(node)):
        return 0

    list = []
    for child in node.getChildrens():
        list.append(height(child))

    return max(list)+1


node_E = Node(12, [])
node_D = Node(13, [])
node_C = Node(2, [])
node_B = Node(5, [])
node_A = Node(1, [])

node_A.childrens.append(node_B)
node_A.childrens.append(node_C)
node_B.childrens.append(node_E)
node_C.childrens.append(node_D)

print(leafSum(node_A))
