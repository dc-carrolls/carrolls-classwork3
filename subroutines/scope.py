city = 'Paris'

def print_city():
  global city
  city = 'London'
  print(city)
#end procedure

#main
print_city()
print(city)