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


cc=nl[0]
if cc == 'w':
  cc='b'
sp=0
np=0
ep=1
l = ep-sp
lmax=l
while sp < n and (ep-sp) < n:
  c = nl[ep%n] 
  if c=='w':
    c=cc 
  if (c==cc) or (c=='w'): 
    l=ep-sp
    if l > lmax:
      lmax = l
    #  print('max:',lmax,'sp:',sp,'ep:',ep)
    #end if
  else:
    cc=c
    sp=np
    np=ep
  #end if
  ep+=1
#end while
print(n)
print(nl)
print('start:',sp,'end:',ep)
print(lmax)

fout.write ('STAY\n')
fout.close()
fin.close()