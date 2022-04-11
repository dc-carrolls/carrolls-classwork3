'SRC1 - linked list module'
class LinkedList:
  'Linked list class'
  class Node:
    'Nested Node class for linked list'
    def __init__(self,data :int,ptr :int) -> None:
      self.data = data
      self.ptr = ptr
    #end procedure

    def __repr__(self) -> str:
        return f'(Data: {self.data}; Pointer: {self.ptr})'
    #end function
  #end class



  def __init__(self,size) -> None:
    self.sp = -1
    self.nf = 0
    self.container = [self.Node(None,-1)]
    while size > 1:
      self.container.insert(0,self.Node(None,size-1))
      size -= 1
    #end while
  #end procedure (constructor)

  def insert(self, item :int) -> str:
    #check if full
    if self.nf == -1:
      return 'Full'
    else:
      self.container[self.nf].data = item # Put item in next free node
      if self.sp == -1: #empty list
        self.sp = self.nf
        self.nf = self.container[self.nf].ptr
        self.container[self.sp].ptr = -1
      else: #search list
        cur_ptr = self.sp
        if item < self.container[cur_ptr].data: #insert at front
         # self.container[self.nf-
          self.sp = self.nf  
        else:
          found = False
          while self.container[cur_ptr] != -1 and not found:
            #peek ahead
            if item >= self.container[self.container[cur_ptr].ptr].data:
              cur_ptr=self.container[cur_ptr].ptr
            else:
              found=True
            #end if
          #end while
        #end if
        self.nf = self.container[self.nf].ptr
        self.container[cur_ptr]
      #end if  
    #end if
  #end procedure 



  def __repr__(self) -> str:
    output_str = f'(Start Pointer: {self.sp}; Next free: {self.nf})\n'
    for node in self.container:
      output_str += node.__repr__() + '\n'
    #next node
    return output_str
  #end function

#end class
    


if __name__ == "__main__":
  my_list = LinkedList(5)
  print(my_list)
  my_list.insert(3)
  print(my_list)
  my_list.insert(1)
  print(my_list)
