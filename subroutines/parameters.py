def proc1 (x,y):
	x = (x[0] - 2,)
	y[0] = 0
#end procedure

#main program
m = (8,) 
n = [10]
proc1(m, n)
print (m[0], n[0])