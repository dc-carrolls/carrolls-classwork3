class NodeType:
    def __init__(self,pname,ppointer):
        self.name = pname
        self.pointer = ppointer
    #end constructor

    def __repr__(self):
      return f'(Name: {self.name}; Pointer: {self.pointer})'
    #end function

#end class

test = "test"
x = NodeType("Bob",-1)
x.name = "Ava"
x.pointer = 0
print(x.name, x.pointer)

myList = [NodeType("",x+1) for x in range(9)]
myList.append(NodeType("",-1))

for node in myList:
    print(node.pointer)