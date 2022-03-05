"""
ID: src.dul1
LANG: PYTHON3
TASK: ride
"""

import pathlib

fin = open (pathlib.Path(__file__).parent.resolve()) / 'ride.in', 'r')
fout = open (pathlib.Path(__file__).parent.resolve() / 'ride.out', 'w')

comet = fin.readline().strip()
group = fin.readline().strip()

comet_no = 1
for c in comet:
  comet_no *= (ord(c)-ord('A')+1)
comet_no %= 47

group_no = 1
for c in group:
  group_no *= (ord(c)-ord('A')+1)
group_no %= 47


if group_no == comet_no:
  fout.write ('GO\n')
else:
  fout.write ('STAY\n')
fout.close()
fin.close()