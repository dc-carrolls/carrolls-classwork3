def myFunc(x, y):
  y = y * 2
  x[0] = x[0] + y
  return (y)
#end function

# Main program
n = [2]
p = 3
r = myFunc (n, p)
print(n[0], p, r)
