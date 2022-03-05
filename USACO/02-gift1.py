"""
ID: src.dul1
LANG: PYTHON3
TASK: gift1
"""

import pathlib

fin = open (pathlib.Path(__file__).parent.resolve() / 'gift1.in', 'r')
fout = open (pathlib.Path(__file__).parent.resolve() / 'gift1.out', 'w')

      
NP = int(fin.readline().strip())
givers={}
i=0
while i<NP:
  givers[fin.readline().strip()]=0
  i+=1
i=0
while i<NP:
  giver = fin.readline().strip()
  i+=1
  gifts, recipients = [int(_) for _ in fin.readline().strip().split()]
  givers[giver]-=gifts
  if gifts != 0:
    gift = gifts // recipients    
    givers[giver]+=gifts%recipients
  else:
    gift=0

  j=0
  while j < recipients:
    givers[fin.readline().strip()] += gift
    j+=1

#fout.write (str(NP) + '\n')
for key, value in givers.items():
  fout.write (str(key)+' '+str(value)+'\n')

fout.close()
fin.close()