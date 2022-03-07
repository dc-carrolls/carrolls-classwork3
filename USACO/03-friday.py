"""
ID: src.dul1
LANG: PYTHON3
TASK: friday
"""

import pathlib

def get_leap(year):
  if year % 400 == 0:
    return True
  if year % 100 == 0:
    return False
  if year % 4 == 0:
    return True
  return False



lp_13ths = [12,31,29,31,30,31,30,31,31,30,31,30]

nl_13ths = [12,31,28,31,30,31,30,31,31,30,31,30]


day_count = [0,0,0,0,0,0,0]


fin = open (pathlib.Path(__file__).parent.resolve() / 'friday.in', 'r')
fout = open (pathlib.Path(__file__).parent.resolve() / 'friday.out', 'w')

      
n = int(fin.readline().strip())

year = 1900
end = 1900 + n
days = 1
while year < end:
  
  if get_leap(year):
    for month_days in lp_13ths:
      days += month_days
      day_count[days % 7] += 1
  else:
    for month_days in nl_13ths:
      days += month_days
      day_count[days % 7] += 1
  days += 19
  year += 1

i = 6
while i < 12:
  fout.write (str(day_count[i%7])+' ')
  i+=1
fout.write (str(day_count[5]) + '\n')
# for key, value in givers.items():
#   fout.write (str(key)+' '+str(value)+'\n')


fout.close()
fin.close()
