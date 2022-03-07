"""
ID: src.dul1
LANG: PYTHON3
TASK: beads
"""

import pathlib
from re import L

fin = open (pathlib.Path(__file__).parent.resolve() / 'beads.in', 'r')
fout = open (pathlib.Path(__file__).parent.resolve() / 'beads.out', 'w')

n = int(fin.readline().strip())
nl = fin.readline().strip()

lmax=1
l = 1

cc=nl[0]
change = 0
i=1
while i < 2*n:
  c = nl[i%n]
  if change < 2:
    if (c == cc) or (c=='w'): 
      l+=1
      if l > lmax:
        lmax = l
      #end if
    else:
      change+=1
      cc=c
    #end if
  else:
    l=1
    change=0
  #end if
  i+=1
#end while
print(n)
print(nl)
print(lmax)

fout.write ('STAY\n')
fout.close()
fin.close()