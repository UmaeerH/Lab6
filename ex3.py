class Node:
    def __init__(self, value, children=None):
    # a leaf node has an empty list of children
        if children is None:
            children = []
        self.value = value
        self.children = children

    def countChildren(self):
        if self.children != []:
            return self.children
        else:
            return None

    #Should return the number of ancestors + itself, as a value. Hence, the size of the "subtree" of the inserted node
    def subtreeSizeRec(self):
        if self.countChildren() != None:
            for i in range(len(self.children)):
                print(f"Found {self.children[i].value} as a child in {self.value}")
                global count
                count += 1
                self.children[i].subtreeSizeRec()
    
    def subtreeSize(self):
        global count
        count = 1
        self.subtreeSizeRec()
        return count

def main():
    leafNode1 = Node(3)
    leafNode2 = Node(7)
    leafNode3 = Node(9)
    childNode1 = Node(2, [leafNode1, leafNode2])
    childNode2 = Node(5, [leafNode3])
    rootNode = Node(10, [childNode1, childNode2])
    print(rootNode.subtreeSize())

if __name__ == "__main__":
    main()