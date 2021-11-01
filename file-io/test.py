# f = open('file-io/input.txt','r')
# data = f.read()
# f.close()
# print(data)

# for c in data:
#   print(c)

# f = open('file-io/input.txt','r',newline='')
# for line in f:
#   print(line)
# f.close()

data = 'Test 1\n' \
       'Test 2' + chr(10) + \
       'Test 3\n' \
       'Test 4\n'

# f = open('file-io/output1.txt', 'w')
# f.write(data)
# f.close()

f = open("file-io/output2.txt", 'w')
print(data, file=f)
f.close()