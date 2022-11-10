class NodeType:
    def __init__(self):
        self.name = ""
        self.pointer = -1
    #end constructor
#end class

x = NodeType()
x.name = "Ava"
x.pointer = 0
print(x.name, x.pointer)

myList = [NodeType() for _ in range(50)]

for node in myList:
    print(node.pointer)