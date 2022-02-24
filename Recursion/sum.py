def addNums(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n	
  #next n
	return sum
#endfunction

def rAddNums(number):
  if len(number) == 1:
    return number[0]
  else:
    newList=number[1:]
    return number.pop(0) + rAddNums(newList)
  #end if
#end function

marks = [3, 6, 2, 8, 1]
total = addNums(marks)
print(total)
print(rAddNums(marks))
