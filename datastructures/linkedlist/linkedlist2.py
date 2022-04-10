'SRC1 - linked list module'
class Node:
  'Node class for linked list'
  def __init__(self,data :int,ptr :int) -> None:
    self.data = data
    self.ptr = ptr
  #end procedure

  def __repr__(self) -> str:
      return f'(Data: {self.data}; Pointer: {self.ptr})'
  #end function
#end class

class LinkedList:
  'Linked list class'
  def __init__(self,size) -> None:
    self.sp = -1
    self.nf = 0
    self.container = [Node(None,-1)]
    while size > 1:
      self.container.insert(0,Node(None,size-1))
      size -= 1
    #end while
  #end procedure (constructor)

  def __repr__(self) -> str:
    output_str = f'(Start Pointer: {self.sp}; Next free: {self.nf})\n'
    for node in self.container:
      output_str += f'{node.__repr__()}\n'
    #next node
    return output_str
  #end function

#end class
    


if __name__ == "__main__":
  my_node = Node(-1,-1)
  print(my_node)
  my_list = LinkedList(5)
  print(my_list)