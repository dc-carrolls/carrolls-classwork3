cnum = 1
pnum = 1
total = 0
while cnum < 4000000:
  ncnum = cnum + pnum
  pnum = cnum
  cnum = ncnum
  if ncnum % 2 == 0:
    total += ncnum
  #end if
#end while
print(total)