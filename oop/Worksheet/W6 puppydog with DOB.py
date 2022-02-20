#W6 Task 1
#class definition for Dog
class Dog():
    
    def __init__(self, myName, myColour):
#In Python, names starting with a double underscore are private
#They are not visible outside the method
#This is data hiding, an important aspect of "encapsulation"
        self.__name = myName
        self.__colour = myColour
        
    def bark(self, barkTimes):
        for n in range (barkTimes):
            print("Woof!")
            
    def setColour(self,myColour):
        self.__colour = myColour
        
    def getColour(self):
        return self.__colour
        
    def getName(self):
        return self.__name
    
    def printDogDetails(self):
        print (self.__name, self.__colour)
    
class Puppy(Dog):
#Puppy inherits attributes and methods from parent class Dog

#In Python, names starting with a double underscore are private
#They are not visible outside the method
#This is data hiding, an important aspect of "encapsulation"
#This class has an extra private attribute __shoesChewed, initialised to 0
    __shoesChewed = 0
#The constructor includes an extra attribute for date of birth called __DOB
    def __init__(self, myName, myColour, myDob):
        super().__init__(myName, myColour)
        self.__dob = myDob

        
    def chewShoe(self, myShoesChewed):      
        self.__shoesChewed = self.__shoesChewed + myShoesChewed

    def getShoesChewed(self):
        return self.__shoesChewed
    
    def getDob(self):
        return self.__dob
        
myDog1 = Dog("Fido", "Black")
myDog2 = Dog ("Bonnie","Golden")
myDog3 = Dog ("Mutt", "Unknown")
myDog4 = Dog ("Jeff", "Unknown")
puppy1 = Puppy("Malla","light brown", "12/08/2016")
myDog3.bark(3)

print("\n")
#if myDog3.getColour() == "Unknown":
#    print("Please enter colour for", myDog3.getName())
#    newColour = input() 
#    myDog3.setColour (newColour)
#print(myDog3.getName(), "is now set to", myDog3.getColour())

print(puppy1.getName(), "is a", puppy1.getColour(),"puppy")
print (puppy1.getName(), "was born", puppy1.getDob())
puppy1.chewShoe(3)
puppy1.chewShoe(1)
print(puppy1.getName(), "has chewed", puppy1.getShoesChewed(), "shoes")

                  