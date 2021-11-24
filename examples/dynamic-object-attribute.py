class Student:
  age = None
  def __init__(self, name):
    self.name = name
  #endif
#end class

barry = Student('Barry')
tom = Student('Tom')
Student.age = 16

print(tom.age) 
print(barry.age)

a = 100
b = 100
while a is b:
  a+=1
  b+=1
  print('a',id(a))
  print('b',id(b))
print(a)
x = 100
a = x + 50
b = x + 50

print(id(a))
print(id(b))
print(a is b)

num=543
# units = num % 10
# print(units)
# num = num // 10
# tens = num % 10
# print(tens)
# num = num //10
# print(num)
x = num//10
y=num//100
print(x%10)
print(y % 10)
print((num % 10) % 10)