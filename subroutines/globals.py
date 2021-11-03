def print_city():
  # global city
  city = 'London'
  print(city)
#end procedure

def print_cities():
  #global cities
  cities[0] = 'Lisbon'
  print(cities)
#end procedure

# Main Program
city = 'Paris'
cities = ['Berlin','Madrid','Rome']
print_city()
print(city)
print_cities()
print(cities)

