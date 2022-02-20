n=int(input())
i=0
sum=0
while i < n:
  a,b,c = [int(_) for _ in input().split()]
  if a+b+c > 1:
    sum += 1
  #end if
  i+=1
#end while
print(sum)