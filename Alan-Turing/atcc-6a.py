f = open('.\Alan-Turing\c6inputb.txt','r',newline='')



output={}
count=0
for line in f:
  for c in line:
    if c in output:
      output[c] += 1
    else:
      output[c] = 1
    #end if
  #next code
#next string
f.close()
print(output)


