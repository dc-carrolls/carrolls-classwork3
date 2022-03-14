f = open('.\Alan-Turing\c6inputa.txt','r',newline='')



codes = {}
count=0
for line in f:
  temp = line
  #print(temp)
  for c in temp:
    if c in codes:
      codes[c] += 1
    else:
      count+=1
      codes[c] = 1
    #end if
  #next code
#next string
f.close()
print(codes)
print(count)

