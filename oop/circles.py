'Circle module documemtation is here'
class Circle:
  'My Main Circle Class'
  def __init__(self):
    'My Circle Constructor'
    x=0
    y=0
  #end constructor
  def add(self) -> int:
    'Adds x and y'
    return self.x + self.y
  #end method
#end class


def main():
  'Circle Module main procedure'
  x = Circle()
  x.x=5
  x.y=10
  print(x.add.__doc__)
  print(x.add())
  print(Circle.__doc__)
  print(Circle.__init__.__doc__)
#end procedure main

if __name__ == '__main__':
  main()
#end if