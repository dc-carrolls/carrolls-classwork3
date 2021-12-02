gifts = ['a partridge in a pear tree',
         'turtle doves',
         'french hens',
         'calling birds',
         'gold rings',
         'geese a laying',
         'swans a swimming',
         'maids are milking',
         'ladies dancing',
         'lords a leaping',
         'pipers piping',
         'drummers drumming']

days = ['first','second','third','forth','fifth','sixth','seventh','eighth','nineth','tenth','eleventh','twelfth']

def verse(n, gifts):
  for amount in range(n,1,-1):
    print(amount,gifts[amount-1])
  #next amount
  if n !=1: #then
    print('and',gifts[0])
  else:
    print(gifts[0])
  #end if
#end procedure

#main
for n in range(1,13):
  print('On the', days[n-1],'day of Christmas, my true love gave to me:')
  verse(n,gifts)
  _ = input('Press <enter> to continue')
#next n
