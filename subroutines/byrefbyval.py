x = 0


def fuchun (y):
  global x
  x = x - 2
  y[0] = 0
#endprocedure

#main program
m = 8 
n = [10]
fuchun( n)
print ( n[0])
print(x)