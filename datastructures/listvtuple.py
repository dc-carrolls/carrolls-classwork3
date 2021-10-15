my_list = (1,2,3,4)
print(len(my_list))
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
for item in my_list:
  print(item)
#next item
index = 0
while index < len(my_list):
  print(my_list[index])
  index = index + 1
#end while
#my_list[0] = 10
my_list.append(50)
#my_list = (10,2,3,4)
for item in my_list:
  print(item)
#next item

