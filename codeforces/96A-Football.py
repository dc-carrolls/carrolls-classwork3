def football():
  players=list(input())
  count = 1
  max_count = 1
  p1=players.pop(0)
  while len(players) > 0 and max_count < 7:
    p = players.pop(0)
    if p == p1:
      count+=1
      if count > max_count:
        max_count = count
    else:
      p1 = p
      count = 1
    #end if
  #next p
  if max_count == 7:
    return 'YES'
  return 'NO'

def football3():
  players=input()
  count = 1
  max_count = 1
  p1=players[0]
  i=1
  while i < len(players) and max_count < 7:
    p = players[i]
    i+=1
    if p == p1:
      count+=1
      if count > max_count:
        max_count = count
    else:
      p1 = p
      count = 1
    #end if
  #next p
  if max_count == 7:
    return 'YES'
  return 'NO'

def football4():
  players=input()
  if '0000000' in players or '1111111' in players:
    return 'YES'
  return 'NO'
  
print(football4())
