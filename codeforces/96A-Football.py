def football():
  players=list(input())
  count = 1
  p1=players.pop(0)
  for p in players:
    if p == p1:
      count+=1
      if count>6:
        return 'YES'
    else:
      p1 = p
      count = 1
    #end if
  #next p
  return 'NO'
  
print(football())
