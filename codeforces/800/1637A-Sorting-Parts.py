t=int(input())
tc=0
while tc < t:
  tc+=1
  n=int(input())
  a = [int(_) for _ in input().split()]
  i = 0
  sorted = True
  while (i < (n-1)) and sorted:
    if a[i] > a[i+1]:
      sorted = False
    #end if
    i+=1
  #end while
  if not sorted:
    print('YES')
  else:
    print('NO')
  #end if
#end while
