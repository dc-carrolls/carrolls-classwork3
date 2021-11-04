

def multiple(lstart,lend,lvalue,pupilName):
  print('Hi', pupilName,'here is your timestable')
  for x in range(lstart,lend + 1):
    print(x, 'x', lvalue, 'is', x * lvalue)
  #next x
#end procedure

name = input('What is your name?')
print('enter table, start num and end num')
table = int(input())
startnum = int(input())
endnum = int(input())


multiple(startnum,endnum,table,name)

