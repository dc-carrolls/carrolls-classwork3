f = open('.\Alan-Turing\input5.txt','r',newline='')

ptext = ""
for line in f:
  temp = line.strip().split(' ')
  print(temp)
  for code in temp:
    num = int('0x'+code,0)
    if num > 31 and num <123:
      ptext = ptext + chr(num)
    #end if
    num = int('0x' +code[::-1],0)
    if num > 31 and num <123:
      ptext = ptext + chr(num)
    #end if
  #next code
#next string
f.close()
print(ptext)

