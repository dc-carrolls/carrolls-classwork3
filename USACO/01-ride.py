"""
ID: src.dul1
LANG: PYTHON3
TASK: ride
"""
fin = open ('./USACO/test.in', 'r')
fout = open ('./USACO/test.out', 'w')

comet = fin.readline()
group = fin.readline()

comet_no = 1
for c in comet:
  comet_no *= (ord(c)-64)
comet_no %= 47


# x,y = map(int, fin.readline().split())
# sum = x+y
fout.write (str(comet_no) + '\n')
fout.close()