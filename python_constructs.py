A = (100,)
b=1
a=100
print(id(a))
def times_table():
    global a
    while True:
        print(b)
        print(a, 'times 5 equals',a*5)
        print(id(a))
        a=a+1
        print(id(a))
        if (a > 12):
            break
        #endif    
    #end while
    print(a)
#end procedure


times_table()
print(A)
