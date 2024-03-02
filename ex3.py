class Node:
    def __init__(self, value, children=None):
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

    #Returns number of nodes including self, as size
    #Depth/Height is indexed from 0
    def subtreeSizeRec(self):
        global depth
        #print(f'Depth is: {depth}')                                                    #Debugging print
        if self.countChildren() != None:
            depth += 1
            for i in range(len(self.children)):
                #print(f"Found {self.children[i].value} as a child in {self.value}")    #Debugging print
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
        return f'Showing info for {self.value}:\nSize of Subtree: {count} \nHeight of Subtree: {height}'

#Testing
def main():
    leafNode1 = Node("leaf1")
    leafNode2 = Node("leaf2")
    leafNode3 = Node("leaf3")
    childNode1 = Node("child1", [leafNode1, leafNode2])
    childNode2 = Node("child2", [leafNode3])
    rootNode = Node("root", [childNode1, childNode2])
    print(leafNode2.subtreeSize())

if __name__ == "__main__":
    main()