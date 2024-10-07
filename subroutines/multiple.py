

def multiple(lstart:int,lend:int,lvalue:int,pupilName:str)->None:
  print('Hi', pupilName,'here is your timestable')
  for x in range(lstart,lend + 1):
    print(x, 'x', lvalue, 'is ?')
    ans = int(input())
    if ans == lvalue * x:
      print('Correct')
    else:
      print('Incorrect')
    #endif
  #next x
#end procedure

name = input('What is your name?')
print('enter table, start num and end num')
table = int(input())
startnum = int(input())
endnum = int(input())


multiple(startnum,endnum,table,name)

