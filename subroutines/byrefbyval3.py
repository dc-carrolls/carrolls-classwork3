def myFunc(x, y):
  y = y * 2
  x = x + y
  return x, y
#end function

# Main program
n = 2
p = 3
n, r = myFunc(n, p)
print(n, p, r)