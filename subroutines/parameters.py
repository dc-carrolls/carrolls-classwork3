def proc1 (x,y):
	x = x - 2
	y = 0
#end procedure

def proc2 (x,y):
	x = x - 2
	y[0] = 0
#end procedure


def proc3 (x,y):
	x = (x[0] - 2,)
	y[0] = 0
#end procedure

#main program

m = 8
n = 10
proc1(m, n)
print (m, n)

m = 8
n = [10]
proc2(m, n)
print (m, n)

m = (8,) 
n = [10]
proc3(m, n)
print (m[0], n[0])