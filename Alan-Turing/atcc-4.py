#f = open('.\Alan-Turing\input4.txt','r')
f = open('.\Alan-Turing\input4.txt','r',newline='')



codes = {}
for line in f:
  temp = line.strip().split(' ')
  print(temp)
  for code in temp:
    if code in codes:
      codes[code] += 1
    else:
      codes[code] = 1
    #end if
  #next code
#next string
f.close()
print(codes)

