a = 42
b = 52
a ^= b
b ^= a
a ^= b

print('a:',a,'b',b)

x = [42]
y = x

y[0],x[0] = x[0],y[0]
print('x',x[0],'x',y[0])

x[0] ^= y[0]
y[0] ^= x[0]
x[0] ^= y[0]

print('x',x[0],'x',y[0])