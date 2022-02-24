import random
class Dog():
	legs = 4
	#name as string
	#colour as string
	def __init__(self, myName, myColour):
		self.name = myName #Private
		self.colour = myColour
		#end if
	#end procedure
	
	def get_colour(self): #Public
		return self.colour
	#end function

	def set_colour(self,myColour): #Public
		if myColour == 'unknown':
			self.colour = input('Enter a colour')
		else:
			self.colour = myColour
		#end if
	#end procedure

	def bark(self,barkTimes):
		for n in range(barkTimes):
			print ("Woof!")
		#next n
	#end procedure

	def getName(self):
		return self.name
	#end function
#end class

class Puppy(Dog): #inherited Dog
	#private shoesChewed = 0
	def __init__ (self,myName, myColour, myDob='01/12/2022'):
		super().__init__(myName, myColour)
		self.dob = myDob
		self.shoesChewed = 0
	#end procedure

	def bark(self,barkTimes):
		for n in range(barkTimes):
			print ("Yap")
			super().bark(1)
		#next n
	#end procedure


	def chewShoes(self, numShoes):
		self.shoesChewed = self.shoesChewed + numShoes
	#end procedure 

	def getChewedShoes(self):
		return self.shoesChewed
	#end function
#end class

#main
myFirstPuppy = Puppy('Sam','Grey','12/12/2021')
print(myFirstPuppy.getName(), 'has chewed', myFirstPuppy.getChewedShoes(), 'shoes')

for n in range(5):
	num = random.randint(0,4)
	print(num, 'chewed')
	myFirstPuppy.chewShoes(num)

print(myFirstPuppy.getName(), 'has chewed', myFirstPuppy.getChewedShoes(), 'shoes')
myFirstPuppy.bark(3)
Dog.legs=3
print(Dog.legs)
myFirstDog = Dog('Fido','Brown')
print(myFirstDog.legs)
# myFirstDog.set_colour('Pink')
# print(myFirstDog.get_colour())

# myDog3 = Dog('Mutton','unknown')

# print(myDog3.get_colour())
# myDog3.set_colour('unknown')
# print(myDog3.get_colour())

