def multiply(x:int,y:int)->None:
	print('Product:')
	print(x*y)
#endprocedure

#main program 	
multiply(2,5)

def multiply2(x:int,y:int)->int:
	return x*y
#endfunction

#main program
print('Product:', multiply2(2,5))
