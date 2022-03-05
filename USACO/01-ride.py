"""
ID: src.dul1
LANG: PYTHON3
TASK: ride
"""

import pathlib

#print(pathlib.Path(__file__).parent.resolve()) 

fin = open (str(pathlib.Path(__file__).parent.resolve())+'/test.in', 'r')
fout = open (str(pathlib.Path(__file__).parent.resolve())+'/test.out', 'w')

comet = fin.readline().strip()
group = fin.readline().strip()

comet_no = 1
for c in comet:
  comet_no *= (ord(c)-64)
comet_no %= 47

group_no = 1
for c in group:
  group_no *= (ord(c)-64)
group_no %= 47


# x,y = map(int, fin.readline().split())
# sum = x+y

if group_no == comet_no:
  fout.write ('GO\n')
else:
  fout.write ('STAY\n')
fout.close()
fin.close()