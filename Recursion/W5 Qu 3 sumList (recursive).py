#recursive routine to sum a list of numbers

def addNums1(numbers):
    if len(numbers) == 1:
        return (numbers[0])
    else:
        numbers[0] = numbers[0] + addNums1(numbers[1:])
        print (numbers[0])
    return numbers[0]
	
#ENDSUB

#version 1
marks = [3,6,2,8,1]
print("\n\nVersion 1, list of 5 numbers 3,6,2,8,1")
total = addNums1(marks)
print ("Total v1 = ",total)


#version 2
def addNums2(numbers):
    if len(numbers) > 1:
        numbers[0] = numbers[0] + addNums2(numbers[1:])
    print (numbers[0])
    return numbers[0]
	
#ENDSUB

marks = [3,6,2,8,1]
print("\n\nVersion 2, list of 5 numbers 3,6,2,8,1")
total = addNums2(marks)
print ("Total v2 = ",total)

input("\nPress Enter to exit program ")
