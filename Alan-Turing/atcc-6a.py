f = open('.\Alan-Turing\c6inputb.txt','r',newline='')



output=""
count=0
for line in f:
  for c in line.strip():
    if c != "0":
      output += c
    #end if
  #next code
#next string
f.close()
print(output)


