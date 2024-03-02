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
            global depthList
            global depth
            depthList.append(depth)
            return None

    #Should return the number of ancestors + itself, as a value. Hence, the size of the "subtree" of the inserted node
    def subtreeSizeRec(self):
        global depth
        #print(f'Depth is: {depth}')    Debugging print
        if self.countChildren() != None:
            depth += 1
            for i in range(len(self.children)):
                #print(f"Found {self.children[i].value} as a child in {self.value}")    Debugging print
                global count
                count += 1
                self.children[i].subtreeSizeRec()
            depth -= 1
    
    def subtreeSize(self):
        global count
        count = 1
        global depthList
        depthList = []
        global depth
        depth = 0
        self.subtreeSizeRec()
        height = max(depthList)
        return f'Size of Subtree is {count} \nHeight of Subtree is: {height}'

def main():
    leafNode1 = Node(3)
    leafNode2 = Node(7)
    leafNode3 = Node(9)
    childNode1 = Node(2, [leafNode1, leafNode2])
    childNode2 = Node(5, [leafNode3])
    rootNode = Node(10, [childNode1, childNode2])
    print(childNode1.subtreeSize())

if __name__ == "__main__":
    main()