n=int(input())
i=0
while i < n:
  w=input()
  l=len(w)
  if l < 11:
    print(w)
  else:
    print(w[0]+str(l-2)+w[-1])
  #end if
  i+=1
#end while
