n, k = [int(_) for _ in input().split()]
#print('n is: ', n, ' k is: ', k)
i = 0
while i < k:
  i+=1
  if (n % 10) == 0:
    n//=10
  else:
    n-=1
  #end if
#end while
print(n)